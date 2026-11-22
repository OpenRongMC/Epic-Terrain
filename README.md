# Epic Terrain · 史诗地形

简体中文 · [English](./README.en.md)


基于 [wonderfulaichen/Epic-Terrain](https://github.com/wonderfulaichen/Epic-Terrain) 的 `versions/1.20.5-1.21.4`（v0.1.4）移植到 **Minecraft 26.3**。

## 本套包含什么

- **保留**：原版阶梯河（Stepped river）、瀑布/落差（waterfall）相关地形与河系。
- **兼容修复**（来自 Compatible 思路，不是官方无瀑布那套河系）：
  - **不覆盖** `minecraft:dimension/overworld`（不写死 multi_noise 群系表，便于 Terrablender / 加群系模组）。
  - 气候槽 `temperature` / `vegetation` 改为原版式 `shifted_noise`，减少对群系分布噪声的劫持。

## RongMC 26.3 版本的改动

26.3 数据包使用新的包格式和世界生成结构。保留阶梯河与瀑布，同时沿用移植版不覆盖原版主世界维度定义的做法。

## 安装

在 [GitHub Releases](https://github.com/OpenRongMC/Epic-Terrain/releases/tag/v26.3-port.1) 下载 **v26.3-port.1**。使用 Minecraft Java **26.3**、**Fabric** 和 **Java 25**。 依赖 [Fabric API](https://modrinth.com/mod/fabric-api)。 发布的是 Fabric JAR。源码树另含各版本的数据包目录；同一世界只启用一份相同地形规则。多人由服务端生成，确认客户端包是否要求携带相同模组。

发布版 Fabric JAR 放入 `mods/`。手动使用数据包时，可打包 [26.3 数据包目录](./versions/26.3)。一个世界只启用其中一份。

## 取舍

去掉 dimension 群系表后，原版靠该表铺开的 `etn:zenith_lake` 等自定义群系点位**不会再被本包强制生成**。群系定义文件仍保留在包内，供其他方式引用。

世界生成包需在**创建新世界**时生效；对已生成区块无效。

## 推荐依赖

- [WorldgenFeatureFix](https://modrinth.com/mod/worldgenfeaturefix)（1.21+ `minecraft:lake` 相关问题）

## 许可

上游 GitHub 树为 MIT（见 `LICENSE`）。官方 Modrinth 上部分发行标注 ARR；本移植基于 GitHub MIT 源。
