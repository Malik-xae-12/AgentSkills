# Project Task Matrix (TASKS.md)

Always work on **one atomic task at a time**. Check off completed tasks and update `MEMORY.md`.

## Phase 1: Environment & Project Setup
- [ ] TASK-101: Initialize repository and Git version control
- [ ] TASK-102: Scaffold directory tree and install core dependencies
- [ ] TASK-103: Configure TypeScript, Tailwind CSS, and linter rules
- [ ] TASK-104: Configure `.env.example` and environment validation

## Phase 2: Core Infrastructure & Design Tokens
- [ ] TASK-201: Setup base layout, theme providers, and font configurations
- [ ] TASK-202: Create shared UI primitives (`Button`, `Input`, `Card`, `Modal`, `Spinner`)
- [ ] TASK-203: Setup API client wrapper with interceptors and error handling

## Phase 3: Authentication Feature
- [ ] TASK-301: Create login and signup UI forms with validation
- [ ] TASK-302: Implement authentication API hooks / service integration
- [ ] TASK-303: Implement session persistence & route guards / middleware
- [ ] TASK-304: Verify auth flow with unit & integration tests

## Phase 4: Core Domain Features (Vertical Slices)
- [ ] TASK-401: Create database models & migration for {{CORE_ENTITY}}
- [ ] TASK-402: Implement repository & service CRUD logic
- [ ] TASK-403: Implement API endpoints with request/response schemas
- [ ] TASK-404: Build feature UI components with loading, empty, and error states
- [ ] TASK-405: Wire UI to React Query mutation/query hooks

## Phase 5: Verification & Production Readiness
- [ ] TASK-501: Execute test plan and verify responsive viewports (375px, 768px, 1440px)
- [ ] TASK-502: Audit security controls (CORS, secrets, input validation)
- [ ] TASK-503: Verify production build passes cleanly

