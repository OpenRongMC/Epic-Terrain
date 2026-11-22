# Epic Terrain

[简体中文](./README.md) · English


Epic Terrain shapes the Overworld with stepped riverbeds, waterfalls and sharper elevation changes. This version comes from [wonderfulaichen’s Epic Terrain](https://github.com/wonderfulaichen/Epic-Terrain) and retains the waterfall terrain rules.

## Terrain and biome compatibility

- The mod retains stepped rivers, waterfalls and river terrain.
- The vanilla Overworld dimension definition remains available to biome mods such as TerraBlender integrations.
- Temperature and vegetation use vanilla-style shifted noise.
- Biomes such as `etn:zenith_lake` remain defined. Their previous forced placement depended on the old dimension biome table.
- Changes apply to newly generated chunks.

## What changed in the RongMC 26.3 port

The 26.3 data pack uses the updated pack and world-generation schemas. It retains stepped rivers and waterfalls and leaves the vanilla Overworld dimension definition available to other world-generation mods.

## Installation

Download **v26.3-port.1** from [GitHub Releases](https://github.com/OpenRongMC/Epic-Terrain/releases/tag/v26.3-port.1) for Minecraft Java **26.3** on **Fabric** with **Java 25**. Dependencies include [Fabric API](https://modrinth.com/mod/fabric-api). The release supplies a Fabric JAR. Versioned data-pack directories are also in the source tree. Enable one copy of the terrain rules per world. Generation runs on the server in multiplayer; follow the pack’s client requirements.

Place the Fabric release JAR in `mods/`. For a standalone data pack, package the contents of [the 26.3 data-pack directory](./versions/26.3). Enable one of the two in each world.

## License

This port is based on the MIT-licensed GitHub source. See [LICENSE](./LICENSE) and the upstream project.
