# Project Face Standalone

Project Face is an AI-powered skin analysis platform with onboarding, dashboard analytics, auth, and payment flows.

## What this repository does
- Runs a FastAPI backend for skin analysis and billing endpoints.
- Serves a React + Vite frontend for landing, auth, dashboard, and settings.
- Supports Stripe-backed payment setup and operational deployment via Docker.

## Website in Test (Vercel)
- Test URL: https://project-face-standalone.vercel.app
- Deployment automation reference: `/DEPLOYMENT_GUIDE.md` (CI/CD + environment setup)

## Current value and goal alignment
- Value: enables direct-to-consumer skin diagnostics with conversion-ready funnel components.
- Goal priority: high, because it supports revenue generation through subscription/payment workflows.
- Strategic fit: contributes to the 3-year scale objective with an immediately deployable web product.

## Quick start
1. Backend: install `/backend/requirements.txt`, then run `uvicorn backend.main:app --host 0.0.0.0 --port 8001`.
2. Frontend: `cd frontend && npm install && npm run dev`.
3. Baseline checks (revvel-standards): run `npm test` and `npm run build` at repository root.
