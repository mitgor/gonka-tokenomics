# Coding Conventions

**Analysis Date:** 2026-01-26

## Naming Patterns

**Files:**
- kebab-case for Node.js scripts and utility files (`.js` extension)
- Example: `gsd-check-update.js`, `gsd-statusline.js`

**Functions:**
- camelCase for function and variable names
- Descriptive names indicating purpose (e.g., `spawnChild`, `readVersionFile`)
- Single-word or multi-word combinations that describe action/intent

**Variables:**
- camelCase for all variable declarations (const, let, var)
- Uppercase for version strings and file paths when appropriate
- Mnemonic names: `cacheDir`, `cacheFile`, `projectVersionFile`, `installed`, `latest`
- Single letter variables used only in tight loops (rare in these files)

**Types:**
- No TypeScript in codebase; plain JavaScript
- Comment-based type hints for clarity (e.g., paths as strings, configs as objects)

## Code Style

**Formatting:**
- No formatter detected (eslint/prettier not configured)
- 2-space indentation (consistent across both files)
- Unix-style line endings (LF)
- Line length: typically 80-100 characters, longer for string literals and paths

**Linting:**
- No eslint or prettier configuration found
- No pre-commit hooks enforcing style
- Style follows Node.js/JavaScript conventions implicitly

**Comments:**
- Single-line comments with `//` for inline documentation
- Shebang line present: `#!/usr/bin/env node` (executable scripts)
- Comments appear before logical blocks to explain purpose
- Example: `// Ensure cache directory exists` (line 19, `gsd-check-update.js`)
- Example: `// Run check in background...` (line 24, `gsd-check-update.js`)

## Import Organization

**Module Loading:**
- CommonJS `require()` syntax (not ES modules)
- Built-in Node.js modules imported first: `fs`, `path`, `os`, `child_process`
- No external npm dependencies
- Imports grouped logically by purpose (filesystem, path utilities, process management)

**Import Order (observed pattern):**
1. Built-in modules: `const fs = require('fs');`
2. Built-in modules continued: `const path = require('path');`
3. Built-in modules continued: `const os = require('os');`
4. Built-in modules continued: `const { spawn } = require('child_process');`

## Error Handling

**Patterns:**
- Try-catch blocks for risky operations (file reads, external commands)
- Silent failures with empty catch blocks when appropriate: `catch (e) {}`
- Example: Line 35-41 in `gsd-check-update.js` - attempts to read version file with fallback
- Example: Line 44-46 - execSync wrapped in try-catch to handle npm CLI failure gracefully
- Errors are logged silently to avoid breaking parent processes
- Fallback values provided: `installed = '0.0.0'`, `latest = null`

**Error Recovery:**
- Graceful degradation when version check fails
- Process continues with safe defaults rather than crashing
- stdin parsing wrapped in try-catch (line 14-82 in `gsd-statusline.js`) with silent fail comment

## Process Management

**Spawning Child Processes:**
- Use `spawn()` from `child_process` for background processes
- Configuration with `stdio: 'ignore'` to detach from parent (line 57)
- `windowsHide: true` for Windows compatibility (lines 58, 45)
- Child process unref'd to allow parent to exit: `child.unref()` (line 61)

## String Handling

**Template Literals:**
- Backticks used for multiline strings with embedded code
- JSON.stringify used for embedding objects in template literals
- Example: Line 25-56 in `gsd-check-update.js` - complex string passed to spawn

**Path Handling:**
- `path.join()` for cross-platform path construction (never hardcoded `/` or `\`)
- Example: `path.join(cwd, '.claude', 'get-shit-done', 'VERSION')`

## File Operations

**Synchronous I/O:**
- Primarily synchronous operations: `fs.readFileSync()`, `fs.existsSync()`, `fs.writeFileSync()`
- Used in initialization and cache writing contexts where async not critical
- Example: Line 36-40 in `gsd-check-update.js` - checking version files synchronously

**Asynchronous I/O:**
- stdin event handling (line 11-13 in `gsd-statusline.js`) - async data collection
- Process spawn is non-blocking (line 25)

## JSON Handling

**Parsing:**
- `JSON.parse()` with try-catch protection
- Embedded in catch-all error handler to prevent crashes
- Example: Line 15 in `gsd-statusline.js` - input stream parsed with error handling

**Serialization:**
- `JSON.stringify()` for creating cache files
- Used with `JSON.stringify(result)` pattern for objects

## Conditional Logic

**Null/Undefined Checks:**
- Loose equality checks: `latest && installed !== latest` (line 49)
- Explicit null checks: `if (remaining != null)` (line 23, `gsd-statusline.js`)
- Fallback patterns: `data.model?.display_name || 'Claude'` (optional chaining with fallback)

## Array Operations

**Filtering and Sorting:**
- `.filter()` for file selection: `files.filter(f => f.startsWith(session) && ...)`
- `.map()` for transformations: mapping filenames to objects with mtime
- `.sort()` for ordering: `sort((a, b) => b.mtime - a.mtime)` (reverse chronological)

## Constants and Configuration

**Configuration Paths:**
- Home directory resolved: `os.homedir()`
- Cache directory: `path.join(homeDir, '.claude', 'cache')`
- Project-specific paths: `path.join(cwd, '.claude', 'get-shit-done', 'VERSION')`

**Constants:**
- Hardcoded strings for known directories (`.claude`, `get-shit-done`)
- Default version: `'0.0.0'` when no version found
- Cache filename: `'gsd-update-check.json'`

## Executable Scripts

**Shebang:**
- All files start with `#!/usr/bin/env node` for direct execution
- Makes scripts executable without explicit `node` command
- Example: Both `gsd-check-update.js` and `gsd-statusline.js`

**Entry Point Pattern:**
- Main logic in script scope or within event handlers
- No class-based structure in these utility scripts
- Functions inlined within logical flow for simplicity

---

*Convention analysis: 2026-01-26*
