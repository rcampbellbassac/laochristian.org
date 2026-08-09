# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability affecting this repository or
[laochristian.org](https://www.laochristian.org/), please report it privately
rather than opening a public issue:

- **Email:** [laohollandsda@gmail.com](mailto:laohollandsda@gmail.com)
- Or use GitHub's [private vulnerability reporting](https://github.com/rcampbellbassac/laochristian.org/security/advisories/new) for this repository.

Please include as much detail as you can (steps to reproduce, potential
impact, affected files or URLs) so we can investigate quickly. We'll
acknowledge reports as soon as possible and keep you updated as we work
on a fix.

## Scope

This repository builds and deploys a static site (MkDocs, no backend
service, database, or user authentication). Relevant reports are most
likely to concern the build/deploy pipeline (`.github/workflows/`),
third-party dependencies (`requirements.txt`, `scripts/requirements.txt`),
or content actually served by the site. Dependency updates are tracked
automatically via [Dependabot](https://github.com/rcampbellbassac/laochristian.org/security/dependabot).
