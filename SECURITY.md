# Security Policy

## Scope
This repository includes frontend and backend services for user auth, analysis workflows, and payment-related integration points.

## Reporting vulnerabilities
- Report security issues privately to maintainers before public disclosure.
- Include reproduction steps, impact, and affected endpoints/components.

## Security controls baseline
- Secrets must be stored in environment variables only.
- Authentication routes and payment endpoints must be validated server-side.
- User-provided inputs must be sanitized and validated.
- Dependencies should be kept patched to supported versions.

## Operational checks
- Run `npm test` and `npm run build` before release.
- Verify `/api/health` and critical auth/payment routes after deployment.
