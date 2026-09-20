#!/usr/bin/env python3
"""
Project Scaffolding Tool for Antigravity & Vibe Coding
Scaffolds exact, production-ready directory trees for:
- Next.js (App Router, Feature-Based Architecture)
- FastAPI (Clean Modular Architecture: Router -> Service -> Repository -> Models)
- React + Vite (Feature-Based Architecture)
- Fullstack (Next.js Frontend + FastAPI Backend)
- Complete Project Documentation Suite (PRD, Architecture, Design, Rules, Tasks, etc.)
"""

import argparse
import os
import sys
from pathlib import Path


def create_file(path: Path, content: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"  + Created: {path}")


def scaffold_docs(base_path: Path, project_name: str, stack: str) -> None:
    docs_dir = base_path / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    templates_dir = Path(__file__).parent.parent / "templates"

    templates = {
        "PRD.md": "PRD.template.md",
        "ARCHITECTURE.md": "ARCHITECTURE.template.md",
        "DESIGN.md": "DESIGN.template.md",
        "RULES.md": "RULES.template.md",
        "TASKS.md": "TASKS.template.md",
        "DECISIONS.md": "DECISIONS.template.md",
        "MEMORY.md": "MEMORY.template.md",
        "TEST_PLAN.md": "TEST_PLAN.template.md",
        "SECURITY.md": "SECURITY.template.md",
    }

    print(f"\n--- Generating Documentation Framework in {docs_dir} ---")
    for doc_file, tmpl_file in templates.items():
        tmpl_path = templates_dir / tmpl_file
        if tmpl_path.exists():
            with open(tmpl_path, "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace("{{PROJECT_NAME}}", project_name)
            content = content.replace("{{TECH_STACK_SUMMARY}}", stack)
            content = content.replace("{{FRONTEND_TECH}}", "Next.js 14+ (App Router)" if stack in ["nextjs", "fullstack"] else "React (Vite)")
            content = content.replace("{{BACKEND_TECH}}", "FastAPI (Python)" if stack in ["fastapi", "fullstack"] else "Next.js Server Actions / API Routes")
            content = content.replace("{{CORE_ENTITY}}", "Item")
            create_file(docs_dir / doc_file, content)
        else:
            create_file(docs_dir / doc_file, f"# {doc_file}\n\nDocumentation for {project_name}")

    env_tmpl = templates_dir / "env.example.template"
    if env_tmpl.exists():
        with open(env_tmpl, "r", encoding="utf-8") as f:
            create_file(base_path / ".env.example", f.read())
    else:
        create_file(base_path / ".env.example", "# Environment variables template\n")

    create_file(
        base_path / "README.md",
        f"""# {project_name}

Production project initialized with the **Vibe Coding** methodology and enterprise architecture.

## Documentation
- Product Requirements: [`docs/PRD.md`](docs/PRD.md)
- System Architecture: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- Design System: [`docs/DESIGN.md`](docs/DESIGN.md)
- AI Coding Rules: [`docs/RULES.md`](docs/RULES.md)
- Tasks Matrix: [`docs/TASKS.md`](docs/TASKS.md)
- Active Memory State: [`docs/MEMORY.md`](docs/MEMORY.md)
- Test Plan: [`docs/TEST_PLAN.md`](docs/TEST_PLAN.md)
- Security Checklist: [`docs/SECURITY.md`](docs/SECURITY.md)

## Getting Started
Follow the instructions in `docs/TASKS.md` for vertical-slice implementation.
""",
    )


def scaffold_nextjs(base_path: Path, project_name: str) -> None:
    print(f"\n--- Scaffolding Next.js (App Router) Architecture in {base_path} ---")

    # 1. App Router
    app_files = [
        "app/layout.tsx",
        "app/loading.tsx",
        "app/error.tsx",
        "app/not-found.tsx",
        "app/page.tsx",
        "app/(public)/layout.tsx",
        "app/(public)/page.tsx",
        "app/(public)/about/page.tsx",
        "app/(public)/contact/page.tsx",
        "app/(auth)/layout.tsx",
        "app/(auth)/login/page.tsx",
        "app/(auth)/register/page.tsx",
        "app/(auth)/forgot-password/page.tsx",
        "app/(auth)/reset-password/page.tsx",
        "app/(dashboard)/layout.tsx",
        "app/(dashboard)/dashboard/page.tsx",
        "app/(dashboard)/profile/page.tsx",
        "app/(dashboard)/settings/page.tsx",
        "app/(dashboard)/reports/page.tsx",
        "app/(admin)/layout.tsx",
        "app/(admin)/dashboard/page.tsx",
        "app/(admin)/users/page.tsx",
        "app/(admin)/roles/page.tsx",
        "app/(admin)/permissions/page.tsx",
        "app/api/auth/route.ts",
    ]

    for f in app_files:
        create_file(base_path / f, f"// {f}\nexport default function Page() {{\n  return <div>{f}</div>;\n}}\n")

    # 2. Features
    features = ["auth", "dashboard", "profile", "settings", "users", "reports"]
    for feat in features:
        feat_dir = f"features/{feat}"
        if feat == "auth":
            create_file(base_path / f"{feat_dir}/components/LoginForm.tsx", "'use client';\nexport function LoginForm() { return <form>Login Form</form>; }")
            create_file(base_path / f"{feat_dir}/components/RegisterForm.tsx", "'use client';\nexport function RegisterForm() { return <form>Register Form</form>; }")
            create_file(base_path / f"{feat_dir}/components/ForgotPasswordForm.tsx", "'use client';\nexport function ForgotPasswordForm() { return <form>Forgot Password</form>; }")
            create_file(base_path / f"{feat_dir}/components/ResetPasswordForm.tsx", "'use client';\nexport function ResetPasswordForm() { return <form>Reset Password</form>; }")
            create_file(base_path / f"{feat_dir}/components/SocialLogin.tsx", "'use client';\nexport function SocialLogin() { return <div>Social Login</div>; }")
            create_file(base_path / f"{feat_dir}/hooks/useAuth.ts", "export function useAuth() { return { user: null, isAuthenticated: false }; }")
            create_file(base_path / f"{feat_dir}/hooks/useLogin.ts", "export function useLogin() { return { login: async () => {} }; }")
            create_file(base_path / f"{feat_dir}/hooks/useRegister.ts", "export function useRegister() { return { register: async () => {} }; }")
            create_file(base_path / f"{feat_dir}/api/auth.service.ts", "export const authService = {};")
            create_file(base_path / f"{feat_dir}/api/auth.query.ts", "export const useAuthQuery = () => {};")
            create_file(base_path / f"{feat_dir}/api/auth.mutation.ts", "export const useLoginMutation = () => {};")
            create_file(base_path / f"{feat_dir}/store/auth.store.ts", "export const useAuthStore = () => {};")
            create_file(base_path / f"{feat_dir}/store/auth.actions.ts", "export const authActions = {};")
            create_file(base_path / f"{feat_dir}/store/auth.selectors.ts", "export const authSelectors = {};")
            create_file(base_path / f"{feat_dir}/context/AuthProvider.tsx", "export function AuthProvider({ children }: { children: React.ReactNode }) { return <>{children}</>; }")
            create_file(base_path / f"{feat_dir}/validation/login.schema.ts", "import { z } from 'zod';\nexport const loginSchema = z.object({ email: z.string().email(), password: z.string().min(6) });")
            create_file(base_path / f"{feat_dir}/validation/register.schema.ts", "import { z } from 'zod';\nexport const registerSchema = z.object({ email: z.string().email(), password: z.string().min(6) });")
            create_file(base_path / f"{feat_dir}/utils/auth.helper.ts", "export const formatAuthToken = (token: string) => `Bearer ${token}`;")
            create_file(base_path / f"{feat_dir}/types/auth.types.ts", "export interface User { id: string; email: string; }")
            create_file(base_path / f"{feat_dir}/constants/auth.constants.ts", "export const AUTH_TOKEN_KEY = 'auth_token';")
            create_file(base_path / f"{feat_dir}/tests/login.test.tsx", "// Auth unit tests")
            create_file(base_path / f"{feat_dir}/index.ts", "export * from './components/LoginForm';\nexport * from './hooks/useAuth';\nexport * from './types/auth.types';")
        else:
            create_file(base_path / f"{feat_dir}/components/index.ts", f"// {feat} components")
            create_file(base_path / f"{feat_dir}/hooks/use{feat.capitalize()}.ts", f"export function use{feat.capitalize()}() {{ return {{}}; }}")
            create_file(base_path / f"{feat_dir}/api/{feat}.service.ts", f"export const {feat}Service = {{}};")
            create_file(base_path / f"{feat_dir}/store/{feat}.store.ts", f"export const use{feat.capitalize()}Store = () => {{}};")
            create_file(base_path / f"{feat_dir}/utils/{feat}.helper.ts", f"export const {feat}Helper = {{}};")
            create_file(base_path / f"{feat_dir}/types/{feat}.types.ts", f"export interface {feat.capitalize()}Model {{ id: string; }}")
            create_file(base_path / f"{feat_dir}/constants/{feat}.constants.ts", f"export const {feat.upper()}_KEY = '{feat}';")
            create_file(base_path / f"{feat_dir}/index.ts", f"export * from './types/{feat}.types';")

    # 3. Components
    ui_elements = ["Button", "Input", "Card", "Modal", "Table", "Select", "Badge", "Spinner"]
    for el in ui_elements:
        create_file(base_path / f"components/ui/{el}/index.ts", f"export function {el}() {{ return <div>{el}</div>; }}")
    create_file(base_path / "components/ui/index.ts", "\n".join([f"export * from './{el}';" for el in ui_elements]))

    common_elements = ["Loader", "EmptyState", "ErrorMessage", "ConfirmDialog"]
    for el in common_elements:
        create_file(base_path / f"components/common/{el}/index.ts", f"export function {el}() {{ return <div>{el}</div>; }}")
    create_file(base_path / "components/common/index.ts", "\n".join([f"export * from './{el}';" for el in common_elements]))

    layout_elements = ["Navbar", "Sidebar", "Footer", "Header"]
    for el in layout_elements:
        create_file(base_path / f"components/layout/{el}/index.ts", f"export function {el}() {{ return <header>{el}</header>; }}")
    create_file(base_path / "components/layout/index.ts", "\n".join([f"export * from './{el}';" for el in layout_elements]))

    # 4. Services, Hooks, Store, Lib, Context, Utils, Constants, Config, Types, Styles
    create_file(base_path / "services/api/axios.ts", "import axios from 'axios';\nexport const apiClient = axios.create();")
    create_file(base_path / "services/api/endpoints.ts", "export const API_ENDPOINTS = { AUTH: { LOGIN: '/auth/login', REGISTER: '/auth/register' } };")
    create_file(base_path / "services/api/interceptors.ts", "export const setupInterceptors = () => {};")
    create_file(base_path / "services/api/apiClient.ts", "export * from './axios';")
    create_file(base_path / "services/websocket.ts", "export const socket = null;")
    create_file(base_path / "services/firebase.ts", "export const firebaseApp = null;")

    hooks = ["useDebounce.ts", "useLocalStorage.ts", "useWindowSize.ts", "usePrevious.ts", "useMediaQuery.ts"]
    for h in hooks:
        create_file(base_path / f"hooks/{h}", f"export function {h.replace('.ts', '')}() {{ return null; }}")

    create_file(base_path / "store/index.ts", "export * from './global.store';")
    create_file(base_path / "store/rootStore.ts", "export const rootStore = {};")
    create_file(base_path / "store/global.store.ts", "export const useGlobalStore = () => {};")

    create_file(base_path / "lib/queryClient.ts", "export const queryClient = {};")
    create_file(base_path / "lib/auth.ts", "export const auth = {};")
    create_file(base_path / "lib/cookies.ts", "export const getCookie = (name: string) => null;")
    create_file(base_path / "lib/logger.ts", "export const logger = console;")
    create_file(base_path / "lib/date.ts", "export const formatDateString = (d: Date) => d.toISOString();")

    create_file(base_path / "context/ThemeProvider.tsx", "export function ThemeProvider({ children }: { children: React.ReactNode }) { return <>{children}</>; }")
    create_file(base_path / "context/NotificationProvider.tsx", "export function NotificationProvider({ children }: { children: React.ReactNode }) { return <>{children}</>; }")
    create_file(base_path / "context/AppProvider.tsx", "export function AppProvider({ children }: { children: React.ReactNode }) { return <>{children}</>; }")

    utils = ["formatDate.ts", "formatCurrency.ts", "downloadFile.ts", "debounce.ts", "helpers.ts"]
    for u in utils:
        create_file(base_path / f"utils/{u}", f"export const {u.replace('.ts', '')} = () => {{}};")

    create_file(base_path / "constants/routes.ts", "export const ROUTES = { HOME: '/', DASHBOARD: '/dashboard', LOGIN: '/login' };")
    create_file(base_path / "constants/roles.ts", "export const ROLES = { ADMIN: 'ADMIN', USER: 'USER' };")
    create_file(base_path / "constants/permissions.ts", "export const PERMISSIONS = { READ: 'READ', WRITE: 'WRITE' };")
    create_file(base_path / "constants/app.constants.ts", "export const APP_NAME = 'NextApp';")

    create_file(base_path / "config/env.ts", "export const env = { API_URL: process.env.NEXT_PUBLIC_API_URL };")
    create_file(base_path / "config/app.config.ts", "export const appConfig = {};")
    create_file(base_path / "config/auth.config.ts", "export const authConfig = {};")

    create_file(base_path / "types/api.types.ts", "export interface ApiResponse<T> { success: boolean; data: T; message?: string; }")
    create_file(base_path / "types/common.types.ts", "export type ID = string | number;")
    create_file(base_path / "types/global.d.ts", "declare global {}")

    create_file(base_path / "styles/globals.css", "@tailwind base;\n@tailwind components;\n@tailwind utilities;")
    create_file(base_path / "styles/variables.css", ":root { --primary: #4F46E5; }")
    create_file(base_path / "styles/theme.css", "/* Theme definitions */")
    create_file(base_path / "styles/tailwind.css", "/* Tailwind imports */")

    # Assets & Public
    for asset_dir in ["images", "icons", "fonts", "animations"]:
        create_file(base_path / f"assets/{asset_dir}/.gitkeep")
    for public_dir in ["images", "icons"]:
        create_file(base_path / f"public/{public_dir}/.gitkeep")
    create_file(base_path / "public/favicon.ico")
    create_file(base_path / "public/robots.txt", "User-agent: *\nAllow: /\n")

    # Tests
    create_file(base_path / "tests/setup.ts", "// Jest / Vitest setup")
    create_file(base_path / "tests/mocks/server.ts", "// Mock service worker / API mocks")
    create_file(base_path / "tests/e2e/auth.spec.ts", "// Playwright e2e tests")

    # Root config files
    create_file(base_path / "middleware.ts", "import { NextResponse } from 'next/server';\nexport function middleware() { return NextResponse.next(); }")
    create_file(base_path / "Dockerfile", "FROM node:20-alpine AS runner\nWORKDIR /app\nCOPY . .\nCMD [\"npm\", \"start\"]")
    create_file(base_path / ".dockerignore", "node_modules\n.next\n.git\n")
    create_file(base_path / ".env.local", "NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1\n")
    create_file(base_path / ".env.production", "NEXT_PUBLIC_API_URL=https://api.example.com/api/v1\n")
    create_file(base_path / "next.config.js", "/** @type {import('next').NextConfig} */\nconst nextConfig = {};\nmodule.exports = nextConfig;")
    create_file(base_path / "tsconfig.json", '{\n  "compilerOptions": {\n    "target": "es5",\n    "lib": ["dom", "dom.iterable", "esnext"],\n    "baseUrl": ".",\n    "paths": { "@/*": ["*"] }\n  }\n}')
    create_file(base_path / "package.json", f'{{\n  "name": "{project_name}-frontend",\n  "version": "0.1.0",\n  "scripts": {{\n    "dev": "next dev",\n    "build": "next build",\n    "start": "next start",\n    "lint": "next lint"\n  }}\n}}')
    print(f"Finished Next.js scaffolding in {base_path}")


def scaffold_fastapi(base_path: Path, project_name: str) -> None:
    print(f"\n--- Scaffolding FastAPI (Modular Clean Architecture) in {base_path} ---")

    # 1. Main & Factory
    create_file(base_path / "app/main.py", 'from app.app_factory import create_app\n\napp = create_app()\n\nif __name__ == "__main__":\n    import uvicorn\n    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)\n')
    create_file(
        base_path / "app/app_factory.py",
        """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMSMiddleware
from app.core.config import settings
from app.modules.auth.router import router as auth_router
from app.modules.users.router import router as users_router
from app.modules.items.router import router as items_router

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
    app.include_router(users_router, prefix="/api/v1/users", tags=["users"])
    app.include_router(items_router, prefix="/api/v1/items", tags=["items"])
    
    return app
""",
    )

    # 2. Core
    create_file(
        base_path / "app/core/config.py",
        """from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Backend"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./app.db"
    JWT_SECRET: str = "change-me-secret-key-32-characters"
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"

settings = Settings()
""",
    )
    create_file(base_path / "app/core/security.py", "def hash_password(p: str) -> str: return p\ndef verify_password(p: str, h: str) -> bool: return p == h\n")
    create_file(base_path / "app/core/logging.py", "import logging\nlogger = logging.getLogger('app')\n")
    create_file(base_path / "app/core/events.py", "async def startup_handler(): pass\nasync def shutdown_handler(): pass\n")
    create_file(base_path / "app/core/exceptions.py", "from fastapi import HTTPException\nclass DomainException(HTTPException): pass\n")

    # 3. DB Layer
    create_file(base_path / "app/db/base.py", "from sqlalchemy.orm import DeclarativeBase\n\nclass Base(DeclarativeBase):\n    pass\n")
    create_file(
        base_path / "app/db/session.py",
        """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
""",
    )
    create_file(
        base_path / "app/db/models_import.py",
        """from app.db.base import Base
from app.modules.users.models.user import User
from app.modules.items.models.item import Item
""",
    )

    # 4. Modules: auth, users, items
    # Auth module
    create_file(base_path / "app/modules/auth/router.py", "from fastapi import APIRouter\nrouter = APIRouter()\n\n@router.post('/login')\ndef login(): return {'token': 'dummy'}\n")
    create_file(base_path / "app/modules/auth/service.py", "class AuthService:\n    def authenticate(self, u, p): return True\n")
    create_file(base_path / "app/modules/auth/schema.py", "from pydantic import BaseModel\nclass LoginRequest(BaseModel):\n    username: str\n    password: str\n")
    create_file(base_path / "app/modules/auth/dependency.py", "def get_current_user(): return {'id': 1}\n")
    create_file(base_path / "app/modules/auth/models/__init__.py", "# Auth models\n")

    # Users module
    create_file(base_path / "app/modules/users/router.py", "from fastapi import APIRouter\nrouter = APIRouter()\n")
    create_file(base_path / "app/modules/users/service.py", "class UserService:\n    def __init__(self, repo): self.repo = repo\n")
    create_file(base_path / "app/modules/users/schema.py", "from pydantic import BaseModel\nclass UserCreate(BaseModel): email: str\nclass UserResponse(BaseModel): id: int; email: str\n")
    create_file(base_path / "app/modules/users/repository.py", "class UserRepository:\n    def __init__(self, db): self.db = db\n")
    create_file(base_path / "app/modules/users/models/user.py", "from app.db.base import Base\nfrom sqlalchemy import Column, Integer, String\n\nclass User(Base):\n    __tablename__ = 'users'\n    id = Column(Integer, primary_key=True)\n    email = Column(String, unique=True)\n")
    create_file(base_path / "app/modules/users/models/profile.py", "from app.db.base import Base\nfrom sqlalchemy import Column, Integer, String\n\nclass Profile(Base):\n    __tablename__ = 'profiles'\n    id = Column(Integer, primary_key=True)\n")
    create_file(base_path / "app/modules/users/models/role.py", "from app.db.base import Base\nfrom sqlalchemy import Column, Integer, String\n\nclass Role(Base):\n    __tablename__ = 'roles'\n    id = Column(Integer, primary_key=True)\n")
    create_file(base_path / "app/modules/users/models/__init__.py", "from .user import User\nfrom .profile import Profile\nfrom .role import Role\n")

    # Items module
    create_file(base_path / "app/modules/items/router.py", "from fastapi import APIRouter\nrouter = APIRouter()\n")
    create_file(base_path / "app/modules/items/service.py", "class ItemService:\n    def __init__(self, repo): self.repo = repo\n")
    create_file(base_path / "app/modules/items/schema.py", "from pydantic import BaseModel\nclass ItemCreate(BaseModel): title: str\nclass ItemResponse(BaseModel): id: int; title: str\n")
    create_file(base_path / "app/modules/items/repository.py", "class ItemRepository:\n    def __init__(self, db): self.db = db\n")
    create_file(base_path / "app/modules/items/models/item.py", "from app.db.base import Base\nfrom sqlalchemy import Column, Integer, String\n\nclass Item(Base):\n    __tablename__ = 'items'\n    id = Column(Integer, primary_key=True)\n    title = Column(String)\n")
    create_file(base_path / "app/modules/items/models/category.py", "from app.db.base import Base\nfrom sqlalchemy import Column, Integer, String\n\nclass Category(Base):\n    __tablename__ = 'categories'\n    id = Column(Integer, primary_key=True)\n")
    create_file(base_path / "app/modules/items/models/__init__.py", "from .item import Item\nfrom .category import Category\n")

    # 5. Shared & Globals
    create_file(base_path / "app/shared/responses.py", "def standard_response(data=None, message='Success'): return {'success': True, 'data': data, 'message': message}\n")
    create_file(base_path / "app/shared/pagination.py", "class PageParams:\n    def __init__(self, page: int = 1, size: int = 20): self.page = page; self.size = size\n")
    create_file(base_path / "app/shared/constants.py", "DEFAULT_PAGE_SIZE = 20\n")
    create_file(base_path / "app/dependencies.py", "# Global dependency providers\nfrom app.db.session import get_db\n")
    create_file(base_path / "app/middleware.py", "# Custom middleware definitions\n")

    # 6. Tests, Alembic, Docker, Requirements
    create_file(base_path / "tests/unit/test_services.py", "def test_service_dummy(): assert True\n")
    create_file(base_path / "tests/integration/test_api.py", "def test_api_dummy(): assert True\n")
    create_file(base_path / "alembic/alembic.ini", "# Alembic configuration\n")
    create_file(base_path / "requirements.txt", "fastapi>=0.110.0\nuvicorn>=0.28.0\nsqlalchemy>=2.0.0\npydantic>=2.6.0\npydantic-settings>=2.2.0\nalembic>=1.13.0\npytest>=8.0.0\n")
    create_file(base_path / "Dockerfile", "FROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nCMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n")
    print(f"Finished FastAPI scaffolding in {base_path}")


def scaffold_react(base_path: Path, project_name: str) -> None:
    print(f"\n--- Scaffolding React + Vite Feature Architecture in {base_path} ---")

    # 1. Public
    create_file(base_path / "public/favicon.ico")
    create_file(base_path / "public/robots.txt", "User-agent: *\nAllow: /\n")
    create_file(base_path / "public/manifest.json", '{"short_name": "App", "name": "React App"}\n')

    # 2. Assets
    create_file(base_path / "src/assets/images/logo.svg", "<svg></svg>")
    create_file(base_path / "src/assets/icons/arrow.svg", "<svg></svg>")
    create_file(base_path / "src/assets/fonts/Inter.woff2")

    # 3. Components
    ui_components = ["Button", "Input", "Modal", "Spinner", "Badge"]
    for comp in ui_components:
        comp_dir = f"src/components/ui/{comp}"
        create_file(base_path / f"{comp_dir}/{comp}.jsx", f"export function {comp}() {{ return <div className='{comp.lower()}'>{comp}</div>; }}")
        if comp in ["Button", "Input", "Modal"]:
            create_file(base_path / f"{comp_dir}/{comp}.module.css", f".{comp.lower()} {{ /* style */ }}")
            create_file(base_path / f"{comp_dir}/{comp}.test.jsx", f"// test for {comp}")
        create_file(base_path / f"{comp_dir}/index.js", f"export * from './{comp}';")

    shared_components = ["Navbar", "Footer", "Sidebar", "ErrorBoundary"]
    for comp in shared_components:
        comp_dir = f"src/components/shared/{comp}"
        create_file(base_path / f"{comp_dir}/{comp}.jsx", f"export function {comp}() {{ return <div>{comp}</div>; }}")
        if comp == "Navbar":
            create_file(base_path / f"{comp_dir}/{comp}.module.css", ".navbar { /* style */ }")
        create_file(base_path / f"{comp_dir}/index.js", f"export * from './{comp}';")

    create_file(base_path / "src/components/layout/AuthLayout.jsx", "export function AuthLayout({ children }) { return <div>{children}</div>; }")
    create_file(base_path / "src/components/layout/DashboardLayout.jsx", "export function DashboardLayout({ children }) { return <div>{children}</div>; }")
    create_file(base_path / "src/components/layout/PublicLayout.jsx", "export function PublicLayout({ children }) { return <div>{children}</div>; }")

    # 4. Features: auth, dashboard, profile, settings
    features = ["auth", "dashboard", "profile", "settings"]
    for feat in features:
        feat_dir = f"src/features/{feat}"
        if feat == "auth":
            create_file(base_path / f"{feat_dir}/components/LoginForm.jsx", "export function LoginForm() { return <form>Login</form>; }")
            create_file(base_path / f"{feat_dir}/components/SignupForm.jsx", "export function SignupForm() { return <form>Signup</form>; }")
            create_file(base_path / f"{feat_dir}/components/ForgotPasswordForm.jsx", "export function ForgotPasswordForm() { return <form>Forgot</form>; }")
            create_file(base_path / f"{feat_dir}/hooks/useAuth.js", "export function useAuth() { return { user: null }; }")
            create_file(base_path / f"{feat_dir}/hooks/useLoginForm.js", "export function useLoginForm() { return {}; }")
            create_file(base_path / f"{feat_dir}/api/authApi.js", "export const authApi = {};")
            create_file(base_path / f"{feat_dir}/types/auth.types.ts", "export interface AuthUser { id: string; }")
            create_file(base_path / f"{feat_dir}/store/authSlice.js", "export const authSlice = {};")
            create_file(base_path / f"{feat_dir}/utils/validateAuth.js", "export const validateAuth = () => true;")
            create_file(base_path / f"{feat_dir}/context/AuthContext.jsx", "export const AuthContext = null;")
            create_file(base_path / f"{feat_dir}/index.js", "export * from './components/LoginForm';")
        elif feat == "dashboard":
            create_file(base_path / f"{feat_dir}/components/StatsCard.jsx", "export function StatsCard() { return <div>Stats</div>; }")
            create_file(base_path / f"{feat_dir}/components/ActivityFeed.jsx", "export function ActivityFeed() { return <div>Feed</div>; }")
            create_file(base_path / f"{feat_dir}/components/ChartPanel.jsx", "export function ChartPanel() { return <div>Chart</div>; }")
            create_file(base_path / f"{feat_dir}/hooks/useDashboardData.js", "export function useDashboardData() { return {}; }")
            create_file(base_path / f"{feat_dir}/api/dashboardApi.js", "export const dashboardApi = {};")
            create_file(base_path / f"{feat_dir}/types/dashboard.types.ts", "export interface DashboardMetrics {}")
            create_file(base_path / f"{feat_dir}/store/dashboardSlice.js", "export const dashboardSlice = {};")
            create_file(base_path / f"{feat_dir}/utils/calculateMetrics.js", "export const calculateMetrics = () => ({});")
            create_file(base_path / f"{feat_dir}/context/DashboardFilterContext.jsx", "export const DashboardFilterContext = null;")
            create_file(base_path / f"{feat_dir}/index.js", "export * from './components/StatsCard';")
        elif feat == "profile":
            create_file(base_path / f"{feat_dir}/components/ProfileForm.jsx", "export function ProfileForm() { return <div>Profile</div>; }")
            create_file(base_path / f"{feat_dir}/components/AvatarUpload.jsx", "export function AvatarUpload() { return <div>Upload</div>; }")
            create_file(base_path / f"{feat_dir}/hooks/useProfile.js", "export function useProfile() { return {}; }")
            create_file(base_path / f"{feat_dir}/api/profileApi.js", "export const profileApi = {};")
            create_file(base_path / f"{feat_dir}/types/profile.types.ts", "export interface ProfileModel {}")
            create_file(base_path / f"{feat_dir}/store/profileSlice.js", "export const profileSlice = {};")
            create_file(base_path / f"{feat_dir}/utils/profileValidators.js", "export const validateProfile = () => true;")
            create_file(base_path / f"{feat_dir}/index.js", "export * from './components/ProfileForm';")
        elif feat == "settings":
            create_file(base_path / f"{feat_dir}/components/NotificationSettings.jsx", "export function NotificationSettings() { return <div>Notifications</div>; }")
            create_file(base_path / f"{feat_dir}/components/SecuritySettings.jsx", "export function SecuritySettings() { return <div>Security</div>; }")
            create_file(base_path / f"{feat_dir}/hooks/useSettings.js", "export function useSettings() { return {}; }")
            create_file(base_path / f"{feat_dir}/api/settingsApi.js", "export const settingsApi = {};")
            create_file(base_path / f"{feat_dir}/types/settings.types.ts", "export interface SettingsModel {}")
            create_file(base_path / f"{feat_dir}/store/settingsSlice.js", "export const settingsSlice = {};")
            create_file(base_path / f"{feat_dir}/utils/settingsHelpers.js", "export const settingsHelpers = {};")
            create_file(base_path / f"{feat_dir}/index.js", "export * from './components/NotificationSettings';")

    # 5. Core folders
    for h in ["useDebounce.js", "useFetch.js", "useLocalStorage.js", "useWindowSize.js"]:
        create_file(base_path / f"src/hooks/{h}", f"export function {h.replace('.js', '')}() {{ return null; }}")

    create_file(base_path / "src/context/ThemeContext.jsx", "export const ThemeContext = null;")
    create_file(base_path / "src/context/NotificationContext.jsx", "export const NotificationContext = null;")

    create_file(base_path / "src/services/api/axiosClient.js", "export const axiosClient = {};")
    create_file(base_path / "src/services/api/endpoints.js", "export const API_ENDPOINTS = {};")
    create_file(base_path / "src/services/firebase.js", "export const firebase = {};")
    create_file(base_path / "src/services/socket.js", "export const socket = {};")

    create_file(base_path / "src/store/index.js", "export const store = {};")
    create_file(base_path / "src/store/rootReducer.js", "export const rootReducer = {};")
    create_file(base_path / "src/store/slices/globalSlice.js", "export const globalSlice = {};")

    create_file(base_path / "src/types/api.types.ts", "export interface ApiData {}")
    create_file(base_path / "src/types/user.types.ts", "export interface UserData {}")
    create_file(base_path / "src/types/global.d.ts", "declare global {}")

    create_file(base_path / "src/utils/formatDate.js", "export const formatDate = () => '';")
    create_file(base_path / "src/utils/formatCurrency.js", "export const formatCurrency = () => '';")
    create_file(base_path / "src/utils/validators.js", "export const validators = {};")

    create_file(base_path / "src/constants/routes.js", "export const ROUTES = {};")
    create_file(base_path / "src/constants/roles.js", "export const ROLES = {};")
    create_file(base_path / "src/constants/apiConstants.js", "export const API_CONSTANTS = {};")

    create_file(base_path / "src/config/env.js", "export const env = {};")
    create_file(base_path / "src/config/appConfig.js", "export const appConfig = {};")

    create_file(base_path / "src/routes/AppRoutes.jsx", "export function AppRoutes() { return <div>Routes</div>; }")
    create_file(base_path / "src/routes/PrivateRoute.jsx", "export function PrivateRoute({ children }) { return children; }")
    create_file(base_path / "src/routes/routesConfig.js", "export const routesConfig = [];")

    create_file(base_path / "src/styles/globals.css", "/* Global styles */")
    create_file(base_path / "src/styles/variables.css", ":root { --color-primary: #6366F1; }")
    create_file(base_path / "src/styles/theme.js", "export const theme = {};")

    create_file(base_path / "src/lib/queryClient.js", "export const queryClient = {};")
    create_file(base_path / "src/tests/setupTests.js", "// Test setup")
    create_file(base_path / "src/tests/mocks/handlers.js", "export const handlers = [];")

    # Entrypoint
    create_file(base_path / "src/App.jsx", "export default function App() { return <div>React App</div>; }")
    create_file(base_path / "src/main.jsx", "import React from 'react';\nimport ReactDOM from 'react-dom/client';\nimport App from './App';\nimport './index.css';\n\nReactDOM.createRoot(document.getElementById('root')).render(<App />);")
    create_file(base_path / "src/index.css", "body { margin: 0; font-family: Inter, sans-serif; }")

    # Root config
    create_file(base_path / ".env", "VITE_API_URL=http://localhost:8000/api/v1\n")
    create_file(base_path / ".env.example", "VITE_API_URL=\n")
    create_file(base_path / ".gitignore", "node_modules\ndist\n.env\n")
    create_file(base_path / ".eslintrc.cjs", "module.exports = { env: { browser: true, es2020: true } };")
    create_file(base_path / ".prettierrc", '{\n  "semi": true,\n  "singleQuote": true\n}')
    create_file(base_path / "package.json", f'{{\n  "name": "{project_name}",\n  "private": true,\n  "version": "0.0.0",\n  "type": "module",\n  "scripts": {{\n    "dev": "vite",\n    "build": "vite build",\n    "preview": "vite preview"\n  }}\n}}')
    create_file(base_path / "README.md", f"# {project_name}\n\nReact + Vite feature-based application.\n")
    create_file(base_path / "tsconfig.json", '{\n  "compilerOptions": { "jsx": "react-jsx" }\n}')
    create_file(base_path / "vite.config.js", "import { defineConfig } from 'vite';\nimport react from '@vitejs/plugin-react';\n\nexport default defineConfig({\n  plugins: [react()],\n});")
    print(f"Finished React scaffolding in {base_path}")


def main():
    parser = argparse.ArgumentParser(description="Enterprise Project Scaffolder & Vibe Coding Initializer")
    parser.add_argument("--stack", choices=["nextjs", "fastapi", "react", "fullstack"], required=True, help="Technology stack to scaffold")
    parser.add_argument("--name", default="my-project", help="Project name")
    parser.add_argument("--output-dir", default=".", help="Target output directory")
    parser.add_argument("--with-docs", action="store_true", help="Scaffold full Vibe Coding docs suite")

    args = parser.parse_args()
    target_dir = Path(args.output_dir).resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    print(f"Initializing project '{args.name}' with stack '{args.stack}' in {target_dir}")

    if args.with_docs:
        scaffold_docs(target_dir, args.name, args.stack)

    if args.stack == "nextjs":
        frontend_dir = target_dir / "frontend" if (target_dir / "frontend").exists() or target_dir.name != "frontend" else target_dir
        scaffold_nextjs(frontend_dir, args.name)
    elif args.stack == "fastapi":
        backend_dir = target_dir / "backend" if (target_dir / "backend").exists() or target_dir.name != "backend" else target_dir
        scaffold_fastapi(backend_dir, args.name)
    elif args.stack == "react":
        react_dir = target_dir / "my-react-app" if (target_dir / "my-react-app").exists() or target_dir.name != "my-react-app" else target_dir
        scaffold_react(react_dir, args.name)
    elif args.stack == "fullstack":
        scaffold_nextjs(target_dir / "frontend", f"{args.name}-frontend")
        scaffold_fastapi(target_dir / "backend", f"{args.name}-backend")

    print("\nProject scaffolding completed successfully!")


if __name__ == "__main__":
    main()

