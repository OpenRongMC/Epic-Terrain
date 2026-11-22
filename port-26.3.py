"""Convert the RongMC 1.21.11 datapack using the vanilla 26.3 schemas."""
import json
import shutil
import sys
from pathlib import Path
from zipfile import ZipFile

root = Path(__file__).resolve().parent
source = root / 'versions/1.21.11'
target = root / 'versions/26.3'
vanilla = ZipFile(sys.argv[1])

def write(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def base(relative):
    return json.loads(vanilla.read('data/minecraft/' + relative + '.json'))

def density(value):
    if isinstance(value, list):
        return [density(item) for item in value]
    if not isinstance(value, dict):
        return value
    d = {key: density(item) for key, item in value.items()}
    kind = d.get('type')
    if kind == 'minecraft:y_clamped_gradient':
        return {'type': 'minecraft:gradient', 'axis': 'y', 'from_coordinate': d['from_y'],
                'to_coordinate': d['to_y'], 'from_value': d['from_value'], 'to_value': d['to_value']}
    if kind == 'minecraft:invert':
        return {'type': 'minecraft:div', 'left': 1, 'right': d['argument']}
    if kind in ('minecraft:abs', 'minecraft:square', 'minecraft:cube', 'minecraft:squeeze',
                'minecraft:half_negative', 'minecraft:quarter_negative', 'minecraft:blend_density'):
        d['input'] = d.pop('argument')
    if kind in ('minecraft:add', 'minecraft:mul', 'minecraft:min', 'minecraft:max'):
        d['left'], d['right'] = d.pop('argument1'), d.pop('argument2')
    if kind in ('minecraft:flat_cache', 'minecraft:cache_once', 'minecraft:cache_2d'):
        return {'type': 'minecraft:cache', 'input': d['argument']}
    if kind == 'minecraft:shifted_noise':
        d['type'] = 'minecraft:noise'
    if kind == 'minecraft:interpolated':
        d = {'type': kind, 'input': d['argument'], 'cell_size_xz': 4, 'cell_size_y': 8}
    if d.get('noise') == 'etn:r/magma_caves':
        return {'type': 'minecraft:negate', 'input': d}
    return d

shutil.copytree(source, target, dirs_exist_ok=True)
for path in source.glob("data/*/worldgen/configured_feature/*.json"):
    relative = path.relative_to(source)
    old_feature = target / relative
    new_feature = old_feature.parent.parent / "feature" / path.name
    new_feature.parent.mkdir(exist_ok=True)
    old_feature.rename(new_feature)
write(target / 'pack.mcmeta', {'pack': {'description': 'Epic Terrain 26.3', 'min_format': [121, 0], 'max_format': [121, 0]}})
for path in target.glob('data/*/worldgen/noise/**/*.json'):
    old = json.loads(path.read_text())
    amps = old['amplitudes']
    if path.name == 'magma_caves.json':
        amps = [abs(amplitude) for amplitude in amps]
    write(path, {'base_octave': old['firstOctave'], 'octave_count': len(amps),
                 'base_amplitude': 1.0, 'amplitude_modifiers': amps})
for path in target.glob('data/*/worldgen/density_function/**/*.json'):
    write(path, density(json.loads(path.read_text())))

config = target / 'data/minecraft/worldgen/noise_settings/overworld.json'
old = json.loads(config.read_text())
new = base('worldgen/noise_settings/overworld')
new['noise'] = {key: old['noise'][key] for key in ('height', 'min_y')}
for key in new['noise_router'].keys() & old['noise_router'].keys():
    new['noise_router'][key] = density(old['noise_router'][key])
new['noise_router']['chunk_surface_level'] = {
    'type': 'minecraft:interpolated', 'cell_size_xz': 16, 'cell_size_y': 1,
    'input': density(old['noise_router']['preliminary_surface_level']),
}
for key in new['aquifers'].keys() & old['noise_router'].keys():
    new['aquifers'][key] = density(old['noise_router'][key])
write(config, new)

config = target / 'data/minecraft/dimension_type/overworld.json'
old = json.loads(config.read_text())
new = base('dimension_type/overworld')
for key in ('height', 'min_y', 'logical_height'):
    new[key] = old[key]
write(config, new)

lake = target / 'data/etn/worldgen/feature/lake_water.json'
old = json.loads(lake.read_text())['config']

def states(value):
    if isinstance(value, list):
        return [states(item) for item in value]
    if not isinstance(value, dict):
        return value
    return { {'Name': 'id', 'Properties': 'properties'}.get(key, key): states(item)
             for key, item in value.items() }

new = base('worldgen/feature/lake_lava')
new['fluid'] = states(old['fluid']['state'])
new['barrier'] = states(old['barrier'])
new["barrier"]["type"] = "minecraft:weighted"
write(lake, new)
