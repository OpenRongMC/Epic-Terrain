# Epic Terrain

[简体中文](./README.md) · English

A world-generation port that retains stepped rivers, waterfalls and river terrain. Compatibility adjustments make it easier to combine with biome mods, but each world-generation stack still needs testing.

## Download and installation

- Version · [v26.3-port.1](https://github.com/OpenRongMC/Epic-Terrain/releases/tag/v26.3-port.1) (Release)
- Release asset · `rongmc-epic-terrain-26.3-port.1.jar`
- Runtime · Minecraft Java 26.3, Fabric, Java 25
- Fabric Loader · `>=0.20.1`
- Fabric mod ID · `rongmc_epic_terrain`
- Dependencies declared by the JAR · [Fabric API](https://modrinth.com/mod/fabric-api) (`fabric-resource-loader-v1`)

Place the release JAR in the instance’s `mods/` directory. The release supplies a Fabric JAR. Versioned data-pack directories are also in the source tree. Enable one copy of the terrain rules per world. Generation runs on the server in multiplayer. Follow the pack’s client requirements.

## How to try it

Create two test worlds with the same seed and compare riverbanks and elevation changes with and without the pack. Existing chunks retain their terrain, so newly generated areas may have seams.

## Development

See [`port-26.3.py`](./port-26.3.py) for the build entry point. Check its workspace paths and dependencies before running it.

## Documentation and support

- [Minecraft 26.3 data-pack source](./versions/26.3)
- [Previous README (historical guide, contributors and credits)](https://github.com/OpenRongMC/Epic-Terrain/blob/e27232b44bb7463bfd6729de85fdde8a7ba36a14/README.md)
- [Upstream project and documentation](https://github.com/wonderfulaichen/Epic-Terrain)
- [Report a RongMC port issue](https://github.com/OpenRongMC/Epic-Terrain/issues) · Include the game version, client and server JAR names, reproduction steps and relevant logs.

## License and credits

See this repository’s [LICENSE](./LICENSE) and the original project’s license, credits and third-party asset notices.
