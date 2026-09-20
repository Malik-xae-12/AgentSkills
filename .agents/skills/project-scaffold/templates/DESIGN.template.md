# Design System & UI Guidelines

## 1. Aesthetic Principles
- **Theme**: Modern, Minimal, Clean, Accessible.
- **Tone**: Professional, crisp, high-contrast.

## 2. Typography
- **Primary Font**: Inter / Geist Sans (`sans-serif`)
- **Monospace Font**: JetBrains Mono / Geist Mono (`monospace`)
- **Scale**:
  - H1: `2.25rem (36px)`, Bold, Line-height: 1.2
  - H2: `1.875rem (30px)`, Semi-bold, Line-height: 1.25
  - H3: `1.5rem (24px)`, Semi-bold, Line-height: 1.3
  - Body: `1rem (16px)`, Regular, Line-height: 1.5
  - Small / Caption: `0.875rem (14px)`, Regular, Line-height: 1.4

## 3. Color Tokens
- **Background**: Light `#F8FAFC` / Dark `#090D16`
- **Surface / Card**: Light `#FFFFFF` / Dark `#111827`
- **Primary Accent**: `#4F46E5` (Indigo) / Hover `#4338CA`
- **Secondary Accent**: `#06B6D4` (Cyan)
- **Text Primary**: Light `#0F172A` / Dark `#F9FAFB`
- **Text Muted**: Light `#64748B` / Dark `#9CA3AF`
- **Border / Divider**: Light `#E2E8F0` / Dark `#1F2937`
- **Destructive / Error**: `#EF4444` (Red)
- **Success**: `#10B981` (Green)
- **Warning**: `#F59E0B` (Amber)

## 4. Component Standards
- **Buttons**: Primary, Secondary, Outline, Ghost, Destructive. All buttons must display a loading spinner when in a submitting state.
- **Cards**: Border radius `12px` (`rounded-xl`), subtle border, soft drop-shadow.
- **Inputs**: Consistent focus rings, explicit labels, inline error messages.

## 5. Required UX States
Every view, feature, and asynchronous interaction MUST support:
1. **Loading State**: Skeleton loaders or Spinner indicators.
2. **Empty State**: Friendly illustration/icon, clear explanation, and primary call-to-action button.
3. **Error State**: Non-blocking banner or card with actionable retry button.
4. **Responsive Layout**: Fluid at 375px (mobile), 768px (tablet), and 1440px (desktop).

