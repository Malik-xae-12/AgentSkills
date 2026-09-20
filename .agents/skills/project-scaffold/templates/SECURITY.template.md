# Security Requirements & Audit Checklist

---

## 1. Authentication & Session Management
- [ ] Passwords hashed using bcrypt / argon2 (never stored plaintext)
- [ ] JWT tokens signed with strong secrets, configured with short expiration
- [ ] Refresh tokens securely rotated or stored in `HttpOnly`, `Secure`, `SameSite=Lax` cookies
- [ ] All protected routes enforce token/session validation before handling business logic

## 2. Authorization (RBAC)
- [ ] Resource access checks ownership (User A cannot read/update User B's records)
- [ ] Admin routes guarded by role checks at the middleware or route dependency level

## 3. Data Validation & Injection Prevention
- [ ] Client input validated at server boundaries using schema validators (Zod / Pydantic)
- [ ] SQL injection prevented via ORM parameterized queries (SQLAlchemy / Prisma)
- [ ] XSS prevented by escaping outputs in UI templates

## 4. Secret Management
- [ ] Zero secrets, keys, or credentials stored in repository
- [ ] Local environment uses `.env.local` or `.env` which is in `.gitignore`
- [ ] Repository contains only `.env.example` with blank keys

## 5. File Uploads (If applicable)
- [ ] File extensions validated against an allowlist (e.g. `.png`, `.jpg`, `.pdf`)
- [ ] Maximum file size strictly enforced
- [ ] Uploaded file content verified (magic numbers) to prevent executable execution

