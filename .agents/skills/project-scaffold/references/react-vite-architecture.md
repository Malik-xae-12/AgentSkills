# React (Vite) Feature-Based Architecture

This specification outlines the exact modern, feature-based architecture for React applications powered by Vite. It provides clean separation of concerns, modularized feature packages, reusable atomic UI components, and standard configuration files.

---

## Directory Tree Specification

```text
my-react-app/
│
├── public/
│   ├── favicon.ico
│   ├── robots.txt
│   └── manifest.json
│
├── src/
│   │
│   ├── assets/
│   │   ├── images/
│   │   │   └── logo.svg
│   │   ├── icons/
│   │   │   └── arrow.svg
│   │   └── fonts/
│   │       └── Inter.woff2
│   │
│   ├── components/
│   │   ├── ui/
│   │   │   ├── Button/
│   │   │   │   ├── Button.jsx
│   │   │   │   ├── Button.module.css
│   │   │   │   ├── Button.test.jsx
│   │   │   │   └── index.js
│   │   │   ├── Input/
│   │   │   │   ├── Input.jsx
│   │   │   │   ├── Input.module.css
│   │   │   │   └── index.js
│   │   │   ├── Modal/
│   │   │   │   ├── Modal.jsx
│   │   │   │   ├── Modal.module.css
│   │   │   │   └── index.js
│   │   │   ├── Spinner/
│   │   │   │   ├── Spinner.jsx
│   │   │   │   └── index.js
│   │   │   └── Badge/
│   │   │       ├── Badge.jsx
│   │   │       └── index.js
│   │   │
│   │   ├── shared/
│   │   │   ├── Navbar/
│   │   │   │   ├── Navbar.jsx
│   │   │   │   ├── Navbar.module.css
│   │   │   │   └── index.js
│   │   │   ├── Footer/
│   │   │   │   ├── Footer.jsx
│   │   │   │   └── index.js
│   │   │   ├── Sidebar/
│   │   │   │   ├── Sidebar.jsx
│   │   │   │   └── index.js
│   │   │   └── ErrorBoundary/
│   │   │       ├── ErrorBoundary.jsx
│   │   │       └── index.js
│   │   │
│   │   └── layout/
│   │       ├── AuthLayout.jsx
│   │       ├── DashboardLayout.jsx
│   │       └── PublicLayout.jsx
│   │
│   ├── features/
│   │   │
│   │   ├── auth/
│   │   │   ├── components/
│   │   │   │   ├── LoginForm.jsx
│   │   │   │   ├── SignupForm.jsx
│   │   │   │   └── ForgotPasswordForm.jsx
│   │   │   ├── hooks/
│   │   │   │   ├── useAuth.js
│   │   │   │   └── useLoginForm.js
│   │   │   ├── api/
│   │   │   │   └── authApi.js
│   │   │   ├── types/
│   │   │   │   └── auth.types.ts
│   │   │   ├── store/
│   │   │   │   └── authSlice.js
│   │   │   ├── utils/
│   │   │   │   └── validateAuth.js
│   │   │   ├── context/
│   │   │   │   └── AuthContext.jsx
│   │   │   └── index.js
│   │   │
│   │   ├── dashboard/
│   │   │   ├── components/
│   │   │   │   ├── StatsCard.jsx
│   │   │   │   ├── ActivityFeed.jsx
│   │   │   │   └── ChartPanel.jsx
│   │   │   ├── hooks/
│   │   │   │   └── useDashboardData.js
│   │   │   ├── api/
│   │   │   │   └── dashboardApi.js
│   │   │   ├── types/
│   │   │   │   └── dashboard.types.ts
│   │   │   ├── store/
│   │   │   │   └── dashboardSlice.js
│   │   │   ├── utils/
│   │   │   │   └── calculateMetrics.js
│   │   │   ├── context/
│   │   │   │   └── DashboardFilterContext.jsx
│   │   │   └── index.js
│   │   │
│   │   ├── profile/
│   │   │   ├── components/
│   │   │   │   ├── ProfileForm.jsx
│   │   │   │   └── AvatarUpload.jsx
│   │   │   ├── hooks/
│   │   │   │   └── useProfile.js
│   │   │   ├── api/
│   │   │   │   └── profileApi.js
│   │   │   ├── types/
│   │   │   │   └── profile.types.ts
│   │   │   ├── store/
│   │   │   │   └── profileSlice.js
│   │   │   ├── utils/
│   │   │   │   └── profileValidators.js
│   │   │   └── index.js
│   │   │
│   │   └── settings/
│   │       ├── components/
│   │       │   ├── NotificationSettings.jsx
│   │       │   └── SecuritySettings.jsx
│   │       ├── hooks/
│   │       │   └── useSettings.js
│   │       ├── api/
│   │       │   └── settingsApi.js
│   │       ├── types/
│   │       │   └── settings.types.ts
│   │       ├── store/
│   │       │   └── settingsSlice.js
│   │       ├── utils/
│   │       │   └── settingsHelpers.js
│   │       └── index.js
│   │
│   ├── hooks/
│   │   ├── useDebounce.js
│   │   ├── useFetch.js
│   │   ├── useLocalStorage.js
│   │   └── useWindowSize.js
│   │
│   ├── context/
│   │   ├── ThemeContext.jsx
│   │   └── NotificationContext.jsx
│   │
│   ├── services/
│   │   ├── api/
│   │   │   ├── axiosClient.js
│   │   │   └── endpoints.js
│   │   ├── firebase.js
│   │   └── socket.js
│   │
│   ├── store/
│   │   ├── index.js
│   │   ├── rootReducer.js
│   │   └── slices/
│   │       └── globalSlice.js
│   │
│   ├── types/
│   │   ├── api.types.ts
│   │   ├── user.types.ts
│   │   └── global.d.ts
│   │
│   ├── utils/
│   │   ├── formatDate.js
│   │   ├── formatCurrency.js
│   │   └── validators.js
│   │
│   ├── constants/
│   │   ├── routes.js
│   │   ├── roles.js
│   │   └── apiConstants.js
│   │
│   ├── config/
│   │   ├── env.js
│   │   └── appConfig.js
│   │
│   ├── routes/
│   │   ├── AppRoutes.jsx
│   │   ├── PrivateRoute.jsx
│   │   └── routesConfig.js
│   │
│   ├── styles/
│   │   ├── globals.css
│   │   ├── variables.css
│   │   └── theme.js
│   │
│   ├── lib/
│   │   └── queryClient.js
│   │
│   ├── tests/
│   │   ├── setupTests.js
│   │   └── mocks/
│   │       └── handlers.js
│   │
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── .env
├── .env.example
├── .gitignore
├── .eslintrc.cjs
├── .prettierrc
├── package.json
├── README.md
├── tsconfig.json
└── vite.config.js
```

---

## Architectural Rules & Conventions

1. **Self-Contained Features (`src/features/`)**:
   - Every business module (`auth`, `dashboard`, `profile`, `settings`) holds its own UI components, hooks, api clients, store slice, and validators.
   - Cross-feature access should always go through the feature's barrel `index.js`.
2. **Component Granularity**:
   - `src/components/ui/`: Atomic, highly reusable presentation components (Buttons, Inputs, Modals, Badges, Spinners). Each component has its own folder containing component code, module styles, test, and an `index.js` export.
   - `src/components/shared/`: Shared functional components like Navigation, Footers, Sidebars, and Error Boundaries.
   - `src/components/layout/`: Routing layouts (`AuthLayout`, `DashboardLayout`, `PublicLayout`) that accept children or render an `<Outlet />`.
3. **Routing Architecture (`src/routes/`)**:
   - Centralized route definitions in `routesConfig.js`.
   - `AppRoutes.jsx` sets up React Router DOM tree.
   - `PrivateRoute.jsx` intercepts unauthenticated requests and redirects to login with return URLs.
4. **State Management**:
   - Global slice (`store/slices/globalSlice.js`) combined in `store/rootReducer.js`.
   - Domain state isolated to feature slices (e.g. `authSlice.js`, `dashboardSlice.js`).
   - Server state handled via TanStack React Query (`lib/queryClient.js`).
5. **Services Layer (`src/services/`)**:
   - Centralized Axios instance with request/response interceptors (`axiosClient.js`) and API URLs (`endpoints.js`).
   - External SDKs (Firebase, Socket.IO) isolated in their own service wrappers.

