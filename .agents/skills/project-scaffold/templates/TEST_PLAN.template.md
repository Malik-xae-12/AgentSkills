# Comprehensive Test Plan

Define what "working" actually means before calling a feature complete.

---

## 1. Automated Testing Matrix
- **Type Checking**: Run `npm run typecheck` or `mypy .`
- **Linting**: Run `npm run lint` or `ruff check .`
- **Unit Tests**: Run `npm test` or `pytest tests/unit/`
- **Integration Tests**: Run integration test suite covering API endpoints and DB operations

## 2. Feature Acceptance Criteria

### Authentication
- [ ] User can register with valid credentials
- [ ] Invalid registration displays clear validation feedback
- [ ] User can log in and receives auth tokens/session cookie
- [ ] Unauthenticated requests to protected routes redirect to login
- [ ] Logged-out user cannot access dashboard or sensitive APIs

### Core Domain ({{CORE_ENTITY}})
- [ ] User can create {{CORE_ENTITY}}
- [ ] User can view list of own entities
- [ ] User can update existing entity
- [ ] User can delete entity with confirmation
- [ ] User cannot access or mutate entities owned by another user

## 3. Responsive UI Breakpoints
Verify layout and usability at:
- [ ] **Mobile**: `375px` (navigation drawer, stacked cards, full-width inputs)
- [ ] **Tablet**: `768px` (compact grid, collapsible sidebar)
- [ ] **Desktop**: `1440px` (full layout, standard spacing, multi-column tables)

