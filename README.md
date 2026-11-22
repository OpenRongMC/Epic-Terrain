# Epic-Terrain 1.21.11（单套）

基于 [wonderfulaichen/Epic-Terrain](https://github.com/wonderfulaichen/Epic-Terrain) 的 `versions/1.20.5-1.21.4`（v0.1.4）移植到 **Minecraft 1.21.11**。

## 本套包含什么

- **保留**：原版阶梯河（Stepped river）、瀑布/落差（waterfall）相关地形与河系。
- **兼容修复**（来自 Compatible 思路，不是官方无瀑布那套河系）：
  - **不覆盖** `minecraft:dimension/overworld`（不写死 multi_noise 群系表，便于 Terrablender / 加群系模组）。
  - 气候槽 `temperature` / `vegetation` 改为原版式 `shifted_noise`，减少对群系分布噪声的劫持。
- **1.21.11**：`pack_format` 94.1、`preliminary_surface_level`、`dimension_type` / biome `attributes`。

## 交付物

| 文件 | 用法 |
|------|------|
| `dist/Epic-Terrain-1.21.11.zip` | 数据包：新建世界时启用，或放入 `saves/<世界>/datapacks/` |
| `dist/epic-terrain-1.21.11.jar` | Fabric 模组：放入 `mods/`（需 Fabric API / `fabric-resource-loader-v0`） |

**二选一即可**（zip 或 jar），不要同时启用两份相同内容。

## 取舍

去掉 dimension 群系表后，原版靠该表铺开的 `etn:zenith_lake` 等自定义群系点位**不会再被本包强制生成**。群系定义文件仍保留在包内，供其他方式引用。

世界生成包需在**创建新世界**时生效；对已生成区块无效。

## 推荐依赖

- [WorldgenFeatureFix](https://modrinth.com/mod/worldgenfeaturefix)（1.21+ `minecraft:lake` 相关问题）

## 许可

上游 GitHub 树为 MIT（见 `LICENSE`）。官方 Modrinth 上部分发行标注 ARR；本移植基于 GitHub MIT 源。

---

## RongMC · Minecraft 26.3 Fabric 移植说明

本仓库是 RongMC 维护的 **Minecraft 26.3 / Fabric / Java 25** 移植构建，不是上游官方发行渠道。

### 与原版的主要差异
- 在原 1.21.11 移植说明基础上，继续提供 **Minecraft 26.3** Fabric jar。
- Fabric id：`rongmc_epic_terrain`（provides `epic_terrain`）。
- 仍遵循原移植取舍：不覆盖 overworld dimension 群系表，气候槽用 shifted_noise。

### 已知问题 / 限制
- 去掉强制群系表后，原依赖该表铺开的自定义群系点位不会被本包强制生成。
- 世界生成改动对**已生成区块无效**，需新建世界或只影响新区块。
- 建议配合 WorldgenFeatureFix（见原 README）；未装时部分湖泊特征可能异常。

### 构建与安装
- Fabric mod id：`rongmc_epic_terrain`（`provides`：`epic_terrain`，旧依赖名一般仍可解析）
- Release 产物见本仓库 Releases（jar 名带 `rongmc-` 前缀）
- 许可证：本仓以 **GPL-3.0** 发布（见 `LICENSE`）；请同时尊重上游原作者条款与署名

