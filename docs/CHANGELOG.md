# Changelog / 更新日志

本文件记录 PyAniParser 各版本的重要变化。每个版本包含内容对应的简体中文与英文说明。

All notable changes to PyAniParser are documented here, with matching Simplified Chinese and English notes for each version.

本格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，本项目遵循[语义化版本控制](https://semver.org/lang/zh-CN/)。

This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

## 📘 Versions / 版本

- [🚀 Release v0.7.0 — New Group Parsers & .NET 11 Support / 新字幕组解析与 .NET 11 支持](#release-v070)
- [🚀 Release v0.6.1 — Native Library Packaging Fix / Native 库打包修复](#release-v061)
- [🚀 Release v0.6.0 — 三明治摆烂组 Parser Support / 三明治摆烂组解析支持](#release-v060)
- [🚀 Release v0.5.0 — EnumSource & Windows ARM64 Support / EnumSource 与 Windows ARM64 支持](#release-v050)
- [🚀 Release v0.4.0 — Enhanced Group Reliability & New Subtitle Support / 字幕组匹配可靠性增强与新字幕支持](#release-v040)
- [🚀 Release v0.3.0 — Metadata Fields & Regex Performance / 元数据字段与正则性能增强](#release-v030)

<a id="release-v070"></a>

## 🚀 Release v0.7.0 — New Group Parsers & .NET 11 Support / 新字幕组解析与 .NET 11 支持

[简体中文](#简体中文-v070) | [English](#english-v070)

Release Date / 发布日期：2026-11-26

### 简体中文 v0.7.0

此版本将底层核心引擎升级至 **Banned.AniParser v0.7.0**，随附的 Native 库新增三组解析支持，并引入 `JpEng` 语言枚举。

#### ✨ 新增

- 随附的 Native 核心现在可通过上游引擎识别三个新发布组：「晚街与灯 / 晚街與燈」（汉化组）、ToonsHub 与 Nix-Raws（搬运组）。`parse()` / `parse_batch()` 及 `get_*_parser_list()` 系列方法会自动包含它们。
- 绿茶字幕组（StudioGreenTea）的多集标题识别已升级（如 `[01-10]`、`[01-12 修正合集 v3]`）。
- 新增 **`EnumLanguage.JpEng`**（值为 `12`，日语 + 英语，对应 ToonsHub 的 `JP&EN` 标签）。`EnumLanguage` 现在从顶层 `pyaniparser` 包导出；已有成员的数字值保持不变。

#### 🔧 变更

- **破坏性变更（仅类型覆盖范围）**：`ParseResult.language` 现在可能返回 `EnumLanguage.JpEng`。若代码假定语言取值集合是封闭的，需要兼容该新成员；已有枚举值均未改变。
- Native 核心改为以 **.NET 11** 为目标构建；wheel ABI（`py3-none-*`）与 Python API 不变。

### English v0.7.0

This release upgrades the underlying core engine to **Banned.AniParser v0.7.0**. The bundled native core gains three new release groups and a `JpEng` language enum value.

#### ✨ Added

- Bundled native core now recognizes three new groups via the upstream engine: **晚街与灯 / 晚街與燈** (translation), **ToonsHub** and **Nix-Raws** (transfer). Available automatically through `parse()` / `parse_batch()` and the `get_*_parser_list()` helpers.
- Upgraded StudioGreenTea multi-episode recognition (e.g. `[01-10]`, `[01-12 修正合集 v3]`) in the native core.
- **`EnumLanguage.JpEng`** (value `12`, Japanese + English, from ToonsHub's `JP&EN` tag). `EnumLanguage` is now exported from the top-level `pyaniparser` package; existing members keep their numeric values.

#### 🔧 Changed

- **Breaking (type coverage only)**: `ParseResult.language` may now be `EnumLanguage.JpEng`. Code that assumes a closed set of language values should handle the new member. No existing integer value changed.
- Native core is now built targeting **.NET 11**; the wheel ABI (`py3-none-*`) and Python API are unchanged.

<a id="release-v061"></a>

## 🚀 Release v0.6.1 — Native Library Packaging Fix / Native 库打包修复

[简体中文](#简体中文-v061) | [English](#english-v061)

Release Date / 发布日期：2026-07-30

### 简体中文 v0.6.1

#### 🐞 修复

- 恢复各平台专用 wheel 中捆绑的 NativeAOT 库（`.dll`、`.so` 与 `.dylib`）。
- 修复 Hatchling 打包配置问题——该问题导致 v0.5.0 与 v0.6.0 的 wheel 遗漏了 Native 库。
- 各平台 wheel 重新做到开箱即用，用户无需再手动提供 Native 库。

### English v0.6.1

#### 🐞 Fixed

- Restored the bundled NativeAOT libraries (`.dll`, `.so`, and `.dylib`) in platform-specific wheels.
- Fixed a Hatchling packaging configuration issue that caused the native libraries to be omitted from the v0.5.0 and v0.6.0 wheels.
- Platform wheels are once again self-contained and no longer require users to provide the native library manually.

<a id="release-v060"></a>

## 🚀 Release v0.6.0 — 三明治摆烂组 Parser Support / 三明治摆烂组解析支持

[简体中文](#简体中文-v060) | [English](#english-v060)

Release Date / 发布日期：2026-06-26

### 简体中文 v0.6.0

此版本将底层核心引擎升级至 **Banned.AniParser v0.6.0**。

#### ✨ 新增

- 通过随附的 Native 核心新增对 **三明治摆烂组** 发布的解析支持。
- 新增对 smzase `.ass` 字幕文件名的支持，包括 `zh-hans` 与 `zh-hant`。
- 新增对使用 `CHS_JPN`、`CHT_JPN` 与 `CHI_JPN` 语言标签的 smzase 视频文件名的支持。

#### 🔧 变更

- `smzase` 与 `三明治摆烂组` 发布标签统一规范化为 `三明治摆烂组`。
- 三明治摆烂组发布中的 `H264` / `H265` 编码标签规范化为 `AVC` / `HEVC`。

### English v0.6.0

Upgraded underlying core engine to **Banned.AniParser v0.6.0**.

#### ✨ Added

- Added parser support for **三明治摆烂组** releases through the bundled native core.
- Added support for smzase `.ass` subtitle file names, including `zh-hans` and `zh-hant`.
- Added support for smzase video file names using `CHS_JPN`, `CHT_JPN`, and `CHI_JPN` language tags.

#### 🔧 Changed

- `smzase` and `三明治摆烂组` release tags are normalized to `三明治摆烂组`.
- `H264` / `H265` codec tags in 三明治摆烂组 releases are normalized to `AVC` / `HEVC`.

<a id="release-v050"></a>

## 🚀 Release v0.5.0 — EnumSource & Windows ARM64 Support / EnumSource 与 Windows ARM64 支持

[简体中文](#简体中文-v050) | [English](#english-v050)

Release Date / 发布日期：2026-06-16

### 简体中文 v0.5.0

此版本将底层核心引擎升级至 **Banned.AniParser v0.5.0**。

#### ✨ 新增

- **`EnumSource` 枚举**：`ParseResult.source` 由原始字符串改为 `EnumSource` 枚举，成员包括 `WEB_DL`、`WEBRip`、`BDRip`、`TVRip`、`DVDRip` 与 `Unknown`。
- **Windows ARM64 wheel**：CI 构建矩阵新增 `windows-arm64` 平台，产出 `py3-none-win_arm64` wheel。

#### 🔧 变更

- **破坏性变更**：`ParseResult.source` 类型由 `str` 改为 `EnumSource`。此前将 `source` 与字符串字面量比较的代码（如 `result.source == "WEB-DL"`）应改用枚举比较（如 `result.source == EnumSource.WEB_DL`）。
- **`EnumSource` 现在从顶层 `pyaniparser` 包导出**，与 `ParseResult` 和 `AniParser` 并列。

#### 🚀 核心引擎升级

- 升级至 **Banned.AniParser v0.5.0**，其中包括：
  - TSDM字幕组 解析支持。
  - 可选的并行批量解析支持。
  - 基于 `Span` 的语言／字幕检测性能优化。
  - 多项解析器可靠性修复（来源传播、字幕检测、VCB-Studio 色彩位深等）。

### English v0.5.0

Upgraded underlying core engine to **Banned.AniParser v0.5.0**.

#### ✨ Added

- **`EnumSource` Enum**: `ParseResult.source` is now an `EnumSource` enum instead of a raw string, with members: `WEB_DL`, `WEBRip`, `BDRip`, `TVRip`, `DVDRip`, `Unknown`.
- **Windows ARM64 Wheel**: Added `windows-arm64` platform to the CI matrix, building wheels for `py3-none-win_arm64`.

#### 🔧 Changed

- **Breaking**: `ParseResult.source` type changed from `str` to `EnumSource`. Existing code that compared `source` against string literals (e.g., `result.source == "WEB-DL"`) should switch to enum comparison (e.g., `result.source == EnumSource.WEB_DL`).
- **`EnumSource` is now exported** from the top-level `pyaniparser` package alongside `ParseResult` and `AniParser`.

#### 🚀 Core Engine Upgrade

- Upgraded to **Banned.AniParser v0.5.0**, which includes:
  - TSDM字幕组 parser support.
  - Parallel batch parsing support.
  - Span-based language/subtitle detection performance optimizations.
  - Multiple parser reliability fixes (source propagation, subtitle detection, VCB-Studio color bit depth, etc.).

<a id="release-v040"></a>

## 🚀 Release v0.4.0 — Enhanced Group Reliability & New Subtitle Support / 字幕组匹配可靠性增强与新字幕支持

[简体中文](#简体中文-v040) | [English](#english-v040)

Release Date / 发布日期：2026-02-18

### 简体中文 v0.4.0

此版本将底层核心引擎升级至 **Banned.AniParser v0.4.0**。

#### ✨ 新增

- **新字幕组支持**：新增针对 **S1百综字幕组（S1YURICON）** 的专用解析规则。

#### 🐞 修复

- 改进可选发布组量词逻辑，在元数据标签缺失时匹配更稳定。
- 修复解析绿茶字幕组（StudioGreenTea）发布时反复出现的失败。

### English v0.4.0

Upgraded underlying core engine to **Banned.AniParser v0.4.0**.

#### ✨ Added

- **New Subtitle Group Support**: Added dedicated parsing rules for **S1百综字幕组 (S1YURICON)**.

#### 🐞 Fixed

- Improved optional group quantifier logic for more robust matching when metadata tags are missing.
- Resolved recurring failures when parsing 绿茶字幕组 (StudioGreenTea) releases.

<a id="release-v030"></a>

## 🚀 Release v0.3.0 — Metadata Fields & Regex Performance / 元数据字段与正则性能增强

[简体中文](#简体中文-v030) | [English](#english-v030)

Release Date / 发布日期：2026-01-11

### 简体中文 v0.3.0

此版本将底层核心引擎升级至 **Banned.AniParser v0.3.0**。

#### 🚀 核心引擎升级

- 上游迁移至 **Source Generated Regex** 并优化内存使用，解析速度显著提升。

#### ✨ 新增

- **`ParseResult` 新增元数据字段并暴露给 Python**：
  - `video_codec`：视频流格式（如 HEVC、AVC）。
  - `audio_codec`：音频流格式（如 AAC、FLAC）。
  - `color_bit_depth`：色彩位深（如 8-bit、10-bit）。
  - `original_title`：原始标题字符串。
  - `titles`：从文件名解析出的本地化标题列表。
- **新解析器支持**：新增 **Orion（猎户发布组）** 解析规则。

#### 🔧 变更

- **类型提示**：更新类型定义以包含新的元数据字段，改善 IDE 自动补全体验。

### English v0.3.0

Upgraded underlying core engine to **Banned.AniParser v0.3.0**.

#### 🚀 Core Engine Upgrade

- **Performance**: Significant parsing speed improvements due to the upstream migration to **Source Generated Regex** and optimized memory usage.

#### ✨ Added

- **New Metadata Fields**: Exposed new fields in the `ParseResult` object to Python:
  - `video_codec`: Video stream format (e.g., HEVC, AVC).
  - `audio_codec`: Audio stream format (e.g., AAC, FLAC).
  - `color_bit_depth`: Color bit depth (e.g., 8-bit, 10-bit).
  - `original_title`: The raw title string.
  - `titles`: A list of localized titles parsed from the filename.
- **New Parser Support**: Added support for **Orion (猎户发布组)** parsing rules.

#### 🔧 Changed

- **Type Hints**: Updated type definitions to include the new metadata fields for better IDE autocomplete support.
