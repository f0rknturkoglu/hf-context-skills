# Code Quality Pipeline

For feature work, prefer a research -> implement -> verify flow.

- Start by spawning `researcher` to map the affected code paths and document current patterns.
- Then spawn `implementer` to own the change.
- Before merge, spawn `security_reviewer` and `performance_reviewer` in parallel and wait for both.
- Keep review agents read-only and report findings before committing.
