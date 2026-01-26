# Codebase Structure

**Analysis Date:** 2026-01-26

## Directory Layout

```
gonka-tokenomics/
├── .claude/                      # Claude Codebase AI framework (Get Shit Done)
│   ├── agents/                   # GSD agent definitions
│   ├── commands/gsd/             # GSD command implementations
│   ├── get-shit-done/            # GSD core framework
│   └── hooks/                    # Git hooks and status monitoring
├── .planning/                    # Planning and codebase documentation
│   └── codebase/                 # Architecture analysis documents
├── .git/                         # Git version control
├── Gonka_Tokenomics_Explained.md # Core project documentation
└── README (implicit)             # Project setup documentation needed
```

## Directory Purposes

**`.claude/` (Project Framework):**
- Purpose: Contains Claude AI automation framework for project management
- Contains: GSD (Get Shit Done) agent definitions and workflow templates
- Key files:
  - `agents/gsd-codebase-mapper.md`: Codebase analysis agent
  - `agents/gsd-executor.md`: Phase execution agent
  - `agents/gsd-planner.md`: Phase planning agent
  - `agents/gsd-debugger.md`: Issue debugging agent
- Note: Framework directory, not source code

**`.planning/codebase/` (Documentation Repository):**
- Purpose: Centralized location for architecture and structure analysis documents
- Contains: ARCHITECTURE.md, STRUCTURE.md, CONVENTIONS.md, TESTING.md, CONCERNS.md
- These documents are consumed by GSD agents when planning and executing phases
- Pattern: Write analysis documents here before implementing features

**Project Root:**
- Purpose: Main documentation and configuration
- Key files: `Gonka_Tokenomics_Explained.md` - comprehensive tokenomics and system design

## Key File Locations

**Entry Points:**
- `Gonka_Tokenomics_Explained.md`: Main system specification and economic model (currently the only comprehensive documentation)

**Configuration:**
- `.planning/codebase/`: Where architecture decisions are documented
- `.claude/get-shit-done/`: Framework configuration templates

**Core Logic:**
- Not yet implemented - architecture phase complete, awaiting development phase

**Testing:**
- Not yet implemented - development phase TBD

## Naming Conventions

**Files:**
- Documentation: UPPERCASE.md (e.g., ARCHITECTURE.md, TESTING.md)
- Implementation files: camelCase.ts for source files (when implemented)
- Test files: camelCase.test.ts or camelCase.spec.ts (when implemented)

**Directories:**
- Feature directories: kebab-case (e.g., `src/consensus`, `src/pricing-engine`, `src/api`)
- Test directories: `__tests__` or `tests/` (when implemented)

## Where to Add New Code

**New Feature - Host/Mining System:**
- Primary code: `src/mining/` (Sprint mechanism, PoC calculation)
- Tests: `src/mining/__tests__/` or `tests/mining/`
- Configuration: `.env` for mining parameters

**New Feature - Developer API:**
- Implementation: `src/api/` (OpenAI-compatible endpoint)
- Route handlers: `src/api/routes/`
- Tests: `src/api/__tests__/`

**New Feature - Pricing Engine:**
- Implementation: `src/pricing/` (Dynamic pricing logic)
- State management: `src/pricing/state.ts`
- Tests: `src/pricing/__tests__/`

**New Feature - Token Management:**
- Implementation: `src/tokens/` (Mining rewards, vesting, distribution)
- Smart contracts (if blockchain-based): `contracts/Token.sol`
- Tests: `src/tokens/__tests__/`

**Utilities:**
- Shared helpers: `src/utils/` (Math utilities, validators, formatters)
- Constants: `src/constants.ts` (Network parameters, pricing ranges, thresholds)
- Types: `src/types/` (TypeScript interfaces for all major entities)

## Special Directories

**`.claude/` (Framework):**
- Purpose: Contains Claude AI automation workflows
- Generated: Partially - created by GSD framework setup
- Committed: Yes - part of project structure
- Usage: Do NOT modify agent definitions unless updating GSD framework itself

**`.planning/` (Analysis Documents):**
- Purpose: Stores codebase analysis documents consumed by planning agents
- Generated: By gsd:map-codebase command
- Committed: Yes - essential for multi-agent workflows
- Usage: Update when architecture decisions change

## Implementation Strategy

### Phase 1: Core Infrastructure (Not Yet Started)
When implementing, start with:
1. `src/types/` - Define core entities (Host, Developer, Task, Token, etc.)
2. `src/constants.ts` - Network parameters from tokenomics document
3. `src/mining/` - Proof of Compute and Sprint mechanism
4. `src/pricing/` - Dynamic pricing engine

### Phase 2: Host System
1. `src/mining/sprint.ts` - 10-minute PoC competition logic
2. `src/mining/rewards.ts` - Emission schedule and reward distribution
3. `src/mining/validation.ts` - Task verification and fraud detection
4. `tests/mining/` - Unit tests for mining subsystem

### Phase 3: Developer API
1. `src/api/` - OpenAI-compatible REST API
2. `src/api/routes/` - Inference request routing
3. `src/api/auth.ts` - Token-based authentication
4. `tests/api/` - Integration tests for API endpoints

### Phase 4: Token Economics
1. `src/tokens/` - GNK token management
2. `src/tokens/vesting.ts` - Reward vesting schedule
3. `src/tokens/community-pool.ts` - Pool governance and conversions
4. `tests/tokens/` - Token economics tests

### Phase 5: Persistence & Database
1. `src/db/` - Database models and queries
2. Database choice: TBD (likely PostgreSQL for reliability)
3. Migrations: `src/db/migrations/`

### Phase 6: Full Integration & Deployment
1. `src/index.ts` - Main entry point
2. `docker/` - Containerization files (if deploying containerized)
3. `scripts/` - Deployment and maintenance scripts
4. `config/` - Environment-specific configuration

## Key System Dependencies (To Be Determined)

When implementation begins, consider:
- Runtime: Node.js with TypeScript (likely, given framework context)
- Database: PostgreSQL or similar for persistent state
- Smart Contracts: Ethereum or compatible chain (if blockchain-integrated)
- API Framework: Express or Fastify for REST API
- Testing: Jest or Vitest for unit/integration tests

## Documentation Strategy

**Before Implementation:**
1. Tokenomics document (existing)
2. Architecture analysis (ARCHITECTURE.md)
3. Structure guide (STRUCTURE.md)
4. Conventions document (when development starts)
5. Testing strategy (when development starts)

**During Implementation:**
1. Keep code comments focused on WHY, not WHAT
2. Update CONVENTIONS.md as patterns emerge
3. Add test examples to TESTING.md
4. Document any deviations in CONCERNS.md

**After Implementation:**
1. Record discovered technical debt
2. Update architecture if major changes made
3. Maintain current documentation in commit messages

---

*Structure analysis: 2026-01-26*
