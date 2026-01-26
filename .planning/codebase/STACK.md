# Technology Stack

**Analysis Date:** 2026-01-26

## Overview

This repository is a **documentation and planning repository** for the Gonka Network tokenomics project. It contains no production code implementation, only:
- Tokenomics documentation
- GSD (Get Shit Done) framework configuration
- Project planning templates

## Languages

**Primary:**
- Markdown - Documentation and project planning
- JSON - Configuration files

**Scripting:**
- JavaScript (Node.js) - GSD framework hooks only

## Runtime

**Environment:**
- Node.js (for GSD framework hooks)

**Package Manager:**
- npm (inferred from GSD JavaScript hooks)

**Lockfile:**
- Not present in repository

## Frameworks & Tools

**Development Framework:**
- GSD (Get Shit Done) - Project planning and orchestration framework
  - Location: `.claude/get-shit-done/`
  - Configuration: `.claude/get-shit-done/templates/config.json`

**Build/Dev Tools:**
- Git - Version control
- Claude AI integration - GSD hooks via `.claude/settings.json`

## Key Dependencies

**Framework Only:**
- Node.js runtime (for hook execution)

**No external package dependencies detected** - This is a documentation-only repository

## Configuration

**GSD Configuration:**
- Config file: `.planning/codebase/config.json`
- Settings: `.claude/settings.json`
- Hooks: `.claude/hooks/`
  - `gsd-check-update.js` - Update checking
  - `gsd-statusline.js` - Status reporting

**Hook System:**
- SessionStart hooks configured
- Status line command integration

## Platform Requirements

**Development:**
- Git repository
- Claude AI integration (via .claude/)
- Node.js (for hook execution)

**Production:**
- Not applicable - documentation repository

## Repository Structure

```
gonka-tokenomics/
├── .claude/                    # GSD framework integration
│   ├── hooks/
│   │   ├── gsd-check-update.js
│   │   └── gsd-statusline.js
│   ├── settings.json
│   └── get-shit-done/
│       └── templates/config.json
├── .planning/
│   └── codebase/              # Planning documents directory (empty)
├── .git/                       # Version control
└── Gonka_Tokenomics_Explained.md  # Main documentation
```

## Documentation Format

**Tokenomics Documentation:**
- Format: Markdown (.md)
- Location: `Gonka_Tokenomics_Explained.md`
- Content: Network economics, incentive mechanisms, token distribution

---

*Stack analysis: 2026-01-26*

**Note:** This repository serves as a planning and documentation hub for the Gonka Network project. Actual implementation code exists in separate repositories. The technology stack detected here reflects the documentation and planning infrastructure only.
