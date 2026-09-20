# Next.js App Router Feature-Based Architecture

This specification outlines the exact enterprise-ready, feature-based architecture for Next.js (App Router). It is designed to scale to large teams and complex domains while preserving clean separation between routing, business domains, shared infrastructure, and UI.

---

## Directory Tree Specification

```text
frontend/
│
├── app/                                          # Next.js App Router (Routing Layer)
│   ├── layout.tsx                                # Root layout (HTML, Body, Providers, Fonts)
│   ├── loading.tsx                               # Global loading UI while pages load
│   ├── error.tsx                                 # Global error boundary
│   ├── not-found.tsx                             # 404 page
│   ├── page.tsx                                  # Home page (/)
│   │
│   ├── (public)/                                 # Public route group (doesn't appear in URL)
│   │   ├── layout.tsx                            # Layout for public pages
│   │   ├── page.tsx                              # Landing page
│   │   ├── about/page.tsx                        # /about
│   │   └── contact/page.tsx                      # /contact
│   │
│   ├── (auth)/                                   # Authentication pages
│   │   ├── layout.tsx                            # Auth layout
│   │   ├── login/page.tsx                        # /login (renders LoginForm)
│   │   ├── register/page.tsx                     # /register
│   │   ├── forgot-password/page.tsx              # /forgot-password
│   │   └── reset-password/page.tsx               # /reset-password
│   │
│   ├── (dashboard)/                              # Protected user pages
│   │   ├── layout.tsx                            # Dashboard layout
│   │   ├── dashboard/page.tsx                    # /dashboard
│   │   ├── profile/page.tsx                      # /profile
│   │   ├── settings/page.tsx                     # /settings
│   │   └── reports/page.tsx                      # /reports
│   │
│   ├── (admin)/                                  # Admin-only routes
│   │   ├── layout.tsx                            # Admin layout
│   │   ├── dashboard/page.tsx                    # /dashboard (admin)
│   │   ├── users/page.tsx                        # /users
│   │   ├── roles/page.tsx                        # /roles
│   │   └── permissions/page.tsx                  # /permissions
│   │
│   └── api/                                      # Optional Next.js API/BFF routes
│       └── auth/
│           └── route.ts                          # API endpoint if needed
│
├── features/                                     # Business modules (Feature-Based Architecture)
│   │
│   ├── auth/                                     # Authentication feature
│   │   ├── components/                           # Auth-specific UI
│   │   │   ├── LoginForm.tsx                     # Login form
│   │   │   ├── RegisterForm.tsx                  # Registration form
│   │   │   ├── ForgotPasswordForm.tsx            # Forgot password form
│   │   │   ├── ResetPasswordForm.tsx             # Reset password form
│   │   │   └── SocialLogin.tsx                   # Google/GitHub login
│   │   │
│   │   ├── hooks/                                # Auth business logic
│   │   │   ├── useAuth.ts                        # Authentication state hook
│   │   │   ├── useLogin.ts                       # Login logic
│   │   │   └── useRegister.ts                    # Registration logic
│   │   │
│   │   ├── api/                                  # Auth API communication
│   │   │   ├── auth.service.ts                   # Axios functions (login, logout)
│   │   │   ├── auth.query.ts                     # React Query GET hooks
│   │   │   └── auth.mutation.ts                  # React Query POST/PUT/DELETE hooks
│   │   │
│   │   ├── store/                                # Zustand/Redux auth state
│   │   │   ├── auth.store.ts                     # Auth state
│   │   │   ├── auth.actions.ts                   # State actions
│   │   │   └── auth.selectors.ts                 # State selectors
│   │   │
│   │   ├── context/                              # Auth Context Provider (optional)
│   │   │   └── AuthProvider.tsx
│   │   │
│   │   ├── validation/                           # Zod/Yup validation schemas
│   │   │   ├── login.schema.ts
│   │   │   └── register.schema.ts
│   │   │
│   │   ├── utils/                                # Auth helper functions
│   │   │   └── auth.helper.ts
│   │   │
│   │   ├── types/                                # Auth TypeScript types
│   │   │   └── auth.types.ts
│   │   │
│   │   ├── constants/                            # Auth constants
│   │   │   └── auth.constants.ts
│   │   │
│   │   ├── tests/                                # Unit tests
│   │   │   └── login.test.tsx
│   │   │
│   │   └── index.ts                              # Barrel exports
│   │
│   ├── dashboard/                                # Dashboard feature
│   │   ├── components/                           # Dashboard widgets/cards
│   │   ├── hooks/                                # Dashboard logic
│   │   ├── api/                                  # Dashboard API
│   │   ├── store/                                # Dashboard state
│   │   ├── utils/                                # Dashboard helpers
│   │   ├── types/                                # Dashboard models
│   │   ├── constants/                            # Dashboard constants
│   │   └── index.ts                              # Exports
│   │
│   ├── profile/                                  # User profile feature
│   │   ├── components/                           # Profile UI
│   │   ├── hooks/                                # Profile hooks
│   │   ├── api/                                  # Profile API
│   │   ├── store/                                # Profile state
│   │   ├── validation/                           # Profile validation
│   │   ├── utils/                                # Profile helpers
│   │   ├── types/                                # Profile models
│   │   └── index.ts
│   │
│   ├── settings/                                 # Application settings
│   │   ├── components/                           # Settings forms
│   │   ├── hooks/                                # Settings logic
│   │   ├── api/                                  # Settings API
│   │   ├── store/                                # Settings state
│   │   ├── utils/                                # Helpers
│   │   ├── types/                                # Models
│   │   └── index.ts
│   │
│   ├── users/                                    # User management feature
│   │   ├── components/                           # User list/forms
│   │   ├── hooks/                                # User logic
│   │   ├── api/                                  # User API
│   │   ├── store/                                # User state
│   │   ├── utils/                                # User helpers
│   │   ├── types/                                # User models
│   │   └── index.ts
│   │
│   └── reports/                                  # Reporting feature
│       ├── components/                           # Charts/Tables
│       ├── hooks/                                # Report logic
│       ├── api/                                  # Report API
│       ├── store/                                # Report state
│       ├── utils/                                # Report helpers
│       ├── types/                                # Report models
│       └── index.ts
│
├── components/                                   # Shared reusable UI
│   ├── ui/                                       # Generic UI components
│   │   ├── Button/
│   │   ├── Input/
│   │   ├── Card/
│   │   ├── Modal/
│   │   ├── Table/
│   │   ├── Select/
│   │   ├── Badge/
│   │   ├── Spinner/
│   │   └── index.ts
│   │
│   ├── common/                                   # Shared functional components
│   │   ├── Loader/
│   │   ├── EmptyState/
│   │   ├── ErrorMessage/
│   │   ├── ConfirmDialog/
│   │   └── index.ts
│   │
│   └── layout/                                   # Layout components
│       ├── Navbar/
│       ├── Sidebar/
│       ├── Footer/
│       ├── Header/
│       └── index.ts
│
├── services/                                     # Shared infrastructure
│   ├── api/
│   │   ├── axios.ts                              # Axios instance
│   │   ├── endpoints.ts                          # API endpoint constants
│   │   ├── interceptors.ts                       # Request/Response interceptors
│   │   └── apiClient.ts                          # API wrapper
│   │
│   ├── websocket.ts                              # WebSocket connection
│   └── firebase.ts                               # Firebase configuration
│
├── hooks/                                        # Global reusable hooks
│   ├── useDebounce.ts
│   ├── useLocalStorage.ts
│   ├── useWindowSize.ts
│   ├── usePrevious.ts
│   └── useMediaQuery.ts
│
├── store/                                        # Global application state
│   ├── index.ts                                  # Store configuration
│   ├── rootStore.ts                              # Root reducer/store
│   └── global.store.ts                           # Global app state
│
├── lib/                                          # Third-party library setup
│   ├── queryClient.ts                            # React Query client
│   ├── auth.ts                                   # Authentication helpers
│   ├── cookies.ts                                # Cookie helpers
│   ├── logger.ts                                 # Logging utility
│   └── date.ts                                   # Date utility wrappers
│
├── context/                                      # Global React Context Providers
│   ├── ThemeProvider.tsx                         # Theme context
│   ├── NotificationProvider.tsx                  # Notifications
│   └── AppProvider.tsx                           # Root provider wrapper
│
├── utils/                                        # Shared helper functions
│   ├── formatDate.ts
│   ├── formatCurrency.ts
│   ├── downloadFile.ts
│   ├── debounce.ts
│   └── helpers.ts
│
├── constants/                                    # Application-wide constants
│   ├── routes.ts
│   ├── roles.ts
│   ├── permissions.ts
│   └── app.constants.ts
│
├── config/                                       # Configuration
│   ├── env.ts                                    # Environment variables
│   ├── app.config.ts                             # Application config
│   └── auth.config.ts                            # Auth configuration
│
├── types/                                        # Shared TypeScript types
│   ├── api.types.ts
│   ├── common.types.ts
│   └── global.d.ts
│
├── styles/                                       # Global styling
│   ├── globals.css
│   ├── variables.css
│   ├── theme.css
│   └── tailwind.css
│
├── assets/                                       # Imported static assets
│   ├── images/
│   ├── icons/
│   ├── fonts/
│   └── animations/
│
├── public/                                       # Publicly served files
│   ├── images/
│   ├── icons/
│   ├── favicon.ico
│   └── robots.txt
│
├── tests/                                        # Project-wide tests
│   ├── setup.ts                                  # Test configuration
│   ├── mocks/                                    # Mock API/data
│   └── e2e/                                      # End-to-end tests
│
├── middleware.ts                                 # Route protection and middleware
├── Dockerfile                                    # Docker build instructions
├── .dockerignore                                 # Files excluded from Docker
├── .env.local                                    # Local environment variables
├── .env.production                               # Production environment variables
├── next.config.js                                # Next.js configuration
├── tsconfig.json                                 # TypeScript configuration
├── package.json                                  # Project dependencies and scripts
└── README.md                                     # Project documentation
```

---

## Architectural Invariants & Rules

1. **Routing Layer (`app/`) is Thin**:
   - `page.tsx` files should solely import and render feature components (e.g. `features/auth/components/LoginForm.tsx`), coordinate layout context, and handle route-level metadata.
   - Do NOT write business logic, direct complex form handlers, or styling directly in `app/**/page.tsx`.
2. **Feature Encapsulation (`features/`)**:
   - Every domain (e.g., `auth`, `dashboard`, `users`) is self-contained.
   - External code imports from a feature through its barrel export `features/<name>/index.ts`.
   - Feature-specific UI components belong in `features/<name>/components/`, while reusable generic components belong in `components/ui/`.
3. **API & Data Fetching**:
   - API endpoints are declared in `services/api/endpoints.ts`.
   - Data fetching uses React Query hooks (`*.query.ts` for queries, `*.mutation.ts` for mutations) wrapped over service functions.
4. **State Management**:
   - Local state: `useState` or `useReducer`.
   - Server state: TanStack Query (`queryClient.ts`).
   - Global client state: Zustand stores (`features/**/store/` and global `store/global.store.ts`).
5. **Security & Validation**:
   - All forms and payloads are validated with Zod (`validation/*.schema.ts`).
   - Protected routes are guarded via `middleware.ts` evaluating session cookies or JWT tokens.

