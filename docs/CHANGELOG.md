# Changelog

All notable changes to this project will be documented in this file.  

This format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  and this project adheres to [Semantic Versioning](https://semver.org/).+

## 📘 Versions

[[0.3.0] - 2026-01-11](#030---2026-01-11)

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