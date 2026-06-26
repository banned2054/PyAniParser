# Changelog

All notable changes to this project will be documented in this file.

This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  and this project adheres to [Semantic Versioning](https://semver.org/).

## 📘 Versions

- [🚀 Release v0.6.0 — 三明治摆烂组 Parser Support](#-release-v060--三明治摆烂组-parser-support)
- [🚀 Release v0.5.0 — EnumSource & Windows ARM64 Support](#-release-v050--enumsource--windows-arm64-support)
- [🚀 Release v0.4.0 — Enhanced Group Reliability & New Subtitle Support](#-release-v040--enhanced-group-reliability--new-subtitle-support)
- [[0.3.0] - 2026-01-11](#030---2026-01-11)

## 🚀 Release v0.6.0 — 三明治摆烂组 Parser Support

Release Date: 2026-06-26

Upgraded underlying core engine to **Banned.AniParser v0.6.0**.

### ✨ Added

- Added parser support for **三明治摆烂组** releases through the bundled native core.
- Added support for smzase `.ass` subtitle file names, including `zh-hans` and `zh-hant`.
- Added support for smzase video file names using `CHS_JPN`, `CHT_JPN`, and `CHI_JPN` language tags.

### 🔧 Changed

- `smzase` and `三明治摆烂组` release tags are normalized to `三明治摆烂组`.
- `H264` / `H265` codec tags in 三明治摆烂组 releases are normalized to `AVC` / `HEVC`.

## 🚀 Release v0.5.0 — EnumSource & Windows ARM64 Support

Release Date: 2026-06-16

Upgraded underlying core engine to **Banned.AniParser v0.5.0**.

### ✨ Added

- **`EnumSource` Enum**: `ParseResult.source` is now an `EnumSource` enum instead of a raw string, with members: `WEB_DL`, `WEBRip`, `BDRip`, `TVRip`, `DVDRip`, `Unknown`.
- **Windows ARM64 Wheel**: Added `windows-arm64` platform to the CI matrix, building wheels for `py3-none-win_arm64`.

### 🔧 Changed

- **Breaking**: `ParseResult.source` type changed from `str` to `EnumSource`. Existing code that compared `source` against string literals (e.g., `result.source == "WEB-DL"`) should switch to enum comparison (e.g., `result.source == EnumSource.WEB_DL`).
- **`EnumSource` is now exported** from the top-level `pyaniparser` package alongside `ParseResult` and `AniParser`.

### 🚀 Core Engine Upgrade

- Upgraded to **Banned.AniParser v0.5.0**, which includes:
  - TSDM 字幕组 parser support.
  - Parallel batch parsing support.
  - Span-based language/subtitle detection performance optimizations.
  - Multiple parser reliability fixes (source propagation, subtitle detection, VCB-Studio color bit depth, etc.).

## 🚀 Release v0.4.0 — Enhanced Group Reliability & New Subtitle Support

Release Date: 2026-02-18

Upgraded underlying core engine to **Banned.AniParser v0.4.0**.

### ✨ Added

- **New Subtitle Group Support**: Added dedicated parsing rules for **S1百综字幕组 (S1YURICON)**.

### 🐞 Fixed

- Improved optional group quantifier logic for more robust matching when metadata tags are missing.
- Resolved recurring failures when parsing 绿茶字幕组 (StudioGreenTea) releases.

## [0.3.0] - 2026-01-11

### 🚀 Core Engine Upgrade
- Upgraded underlying core engine to **Banned.AniParser v0.3.0**.
- **Performance**: Significant parsing speed improvements due to the upstream migration to **Source Generated Regex** and optimized memory usage.

### ✨ Added
- **New Metadata Fields**: Exposed new fields in the `ParseResult` object to Python:
  - `video_codec`: Video stream format (e.g., HEVC, AVC).
  - `audio_codec`: Audio stream format (e.g., AAC, FLAC).
  - `color_bit_depth`: Color bit depth (e.g., 8-bit, 10-bit).
  - `original_title`: The raw title string.
  - `titles`: A list of localized titles parsed from the filename.
- **New Parser Support**: Added support for **Orion (猎户发布组)** parsing rules.

### 🔧 Changed
- **Type Hints**: Updated type definitions to include the new metadata fields for better IDE autocomplete support.
