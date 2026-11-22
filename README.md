# 史诗地形

简体中文 · [English](./README.en.md)

世界生成移植版，保留阶梯河、瀑布与河系生成特征。兼容性调整让地形与其他群系模组更容易共存，但不同世界生成组合仍需试跑。

## 下载与安装

- 版本 · [v26.3-port.1](https://github.com/OpenRongMC/Epic-Terrain/releases/tag/v26.3-port.1) (已发布)
- 下载文件 · `rongmc-epic-terrain-26.3-port.1.jar`
- 运行环境 · Minecraft Java 26.3, Fabric, Java 25
- Fabric Loader · `>=0.20.1`
- Fabric 模组 ID · `rongmc_epic_terrain`
- JAR 声明的依赖 · [Fabric API](https://modrinth.com/mod/fabric-api) (`fabric-resource-loader-v1`)

把发行 JAR 放入对应实例的 `mods/` 目录。发布的是 Fabric JAR。源码树另含各版本的数据包目录。同一世界只启用一份相同地形规则。多人由服务端生成，确认客户端包是否要求携带相同模组。

## 如何验证

用同一个种子创建两个测试世界，检查有无地形包时的河岸和落差。已有区块不会重新生成，旧图边界可能出现接缝。

## 开发

构建入口见 [`port-26.3.py`](./port-26.3.py)。运行前检查脚本需要的工作区目录与依赖。

## 文档与反馈

- [Minecraft 26.3 数据包源文件](./versions/26.3)
- [原 README（旧版指南、贡献者与署名）](https://github.com/OpenRongMC/Epic-Terrain/blob/e27232b44bb7463bfd6729de85fdde8a7ba36a14/README.md)
- [上游项目与文档](https://github.com/wonderfulaichen/Epic-Terrain)
- [报告 RongMC 移植问题](https://github.com/OpenRongMC/Epic-Terrain/issues) · 请附游戏版本、两端 JAR 文件名、复现步骤和相关日志。

## 许可与署名

请参阅本仓库的 [LICENSE](./LICENSE) 及原项目的许可、署名和第三方资源说明。
