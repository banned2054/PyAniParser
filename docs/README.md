# PyAniParser

[**中文文档**](https://github.com/banned2054/PyAniParser/blob/master/Docs/README.md) | [**English Doc**](https://github.com/banned2054/PyAniParser/blob/master/README.md)

**PyAniParser** 是 [Banned.AniParser](https://github.com/banned2054/Banned.AniParser) 的高性能 Python 封装，专为解析动画文件名而设计。它基于 **.NET 10 Native AOT** 构建，能够快速且准确地从复杂的文件命名规则中提取元数据（如标题、集数、分辨率等）。

> **注意**：本解析器目前针对 **中文动漫/字幕组命名习惯**（例如 VCB-Studio、喵萌奶茶屋、桜都字幕组）进行了特别优化。

## 功能特性

- **高性能**: 基于 .NET Native AOT 构建，速度快且效率高。
- **解析鲁棒性强**: 专门处理来自不同发布组的复杂命名格式。
- **批量处理**: 针对大批量文件列表的处理进行了优化。
- **全球化支持**: 内置繁体中文到简体中文的转换功能。
- **类型提示 (Type Hinting)**: 完全类型化，提供更好的 IDE 支持和开发体验。

## 安装

```bash
pip install pyaniparser
```

## 使用方法

### 基础用法

```python
from pyaniparser import AniParser

# 初始化解析器
parser = AniParser()

# 解析单个文件
result = parser.parse("[Nekomoe] Anime Title - 01 [1080p].mp4")
if result:
    print(f"Title: {result.title}")
    print(f"Episode: {result.episode}")

# 批量解析文件（处理列表时推荐使用）
files = ["File1.mp4", "File2.mp4"]
results = parser.parse_batch(files)

for item in results:
    print(item.title)
```

### 高级配置（全球化/繁简转换）

您可以在初始化时配置解析器，使其自动将繁体中文标题转换为简体中文（反之亦然）：

```python
# 选项: "Simplified" (简体), "Traditional" (繁体), 或 "NotChange" (默认不更变)
parser = AniParser(globalization="Simplified")

result = parser.parse("[Group] 繁體標題 - 01.mp4")
print(result.title) # 输出将被转换为简体中文
```

### 获取支持的发布组

您可以通过编程方式获取当前支持的字幕组和发布组列表：

```python
parser = AniParser()
groups = parser.get_parser_list()
print(groups)
```

## 支持的发布组

PyAniParser 内置支持许多主流发布组，包括但不限于：

- ANi
- 北宇治字幕组
- 喵萌奶茶屋
- 桜都字幕组
- Vcb-Studio

如需查看完整的支持列表，请参阅 [上游文档](https://github.com/banned2054/Banned.AniParser/blob/master/Docs/SupportedGroups.md)。

## 许可证

本项目采用 Apache-2.0 许可证。详情请参阅 [LICENSE](https://github.com/banned2054/PyAniParser/blob/master/LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request！

由于这是一个封装库 (wrapper)，关于**解析逻辑**的问题请反馈至 [核心 .NET 仓库](https://github.com/banned2054/Banned.AniParser/issues)，而关于 **Python 绑定**的问题可以在本项目中反馈。