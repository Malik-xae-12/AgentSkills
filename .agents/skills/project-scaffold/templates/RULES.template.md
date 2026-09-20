# AI Development Rules & Constraints

## 1. General Principles
- **Strict Typing**: Always use TypeScript or Python type annotations. No `any` types without explicit justification.
- **Single Responsibility**: Keep components and functions small (<50 lines where feasible). Extract reusable logic into hooks or utility functions.
- **Never Modify Unrelated Files**: Only touch files directly required for the current task. Do not reformat or reorganize surrounding code.
- **Preserve Existing Code**: Preserve comments, existing conventions, and test setups.

## 2. Architecture & Code Organization
- Follow the designated folder structure strictly.
- Never write database queries directly inside UI components or HTTP route handlers.
- UI components belong in `components/` (shared) or `features/<feature>/components/` (domain-specific).
- All external API communication must flow through the central services/api client.

## 3. Security
- Never hardcode API keys, secrets, JWT tokens, or passwords in source code.
- Always read secrets from environment variables (`.env`).
- Always validate incoming client input on the server side using Zod or Pydantic schemas.
- Protect all private routes with authentication and authorization checks.

## 4. Verification & Testing
- Before completing any task, run type checking and linting.
- If unit tests exist for the feature area, ensure they execute and pass.
- Fix all introduced compiler errors, lint errors, or broken tests before proceeding to the next task.

## 5. Version Control Hygiene
- Make small, atomic commits matching the format: `type(scope): message` (e.g. `feat(auth): add login form validation`).

