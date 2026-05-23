# Deployment Guide

## Target topology
- Frontend: Vercel deployment for the React app surface.
- Backend: containerized FastAPI service.
- Data/services: environment-driven integrations (Stripe, API keys, database/cache where configured).

## Environment setup
1. Copy `.env.example` and set production secrets.
2. Set Stripe keys and backend API secrets.
3. Confirm CORS and API base URL settings for the frontend.

## Build and validation
1. Run repository baseline checks:
   - `npm test`
   - `npm run build`
2. Build frontend:
   - `cd frontend && npm install && npm run build`
3. Build backend container:
   - `docker compose build backend`

## Release flow
1. Merge to protected main branch.
2. Trigger deployment automation for Vercel frontend and backend runtime.
3. Run smoke checks:
   - `/api/health`
   - auth login/register route access
   - dashboard + pricing + checkout flow

## Rollback
- Re-deploy last known good release artifact.
- Revert environment changes if issue is config-driven.
