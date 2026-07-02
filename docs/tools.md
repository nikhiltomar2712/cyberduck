# Cyberduck Tools

Small defensive utilities live in `tools/`.

## Available tools

- `password_strength_checker.py` — offline password strength feedback.
- `file_hash.py` — generate file hashes for integrity verification.
- `security_headers_check.py` — review common HTTP security headers for authorized sites.
- `local_port_inventory.py` — list local listening ports without remote scanning.
- `log_failed_login_summary.py` — summarize failed-login-like log lines.


## Python package

The `cyberduck/` package contains reusable defensive helpers for:

- password policy review
- file hashing and integrity checks
- HTTP security header grading
- local port explanations
- failed-login log parsing
- risk scoring and threat modeling
- CIDR, DNS, URL, email-header, and security.txt parsing
- incident timelines, report building, and audit rules

The repository now includes unit tests in `tests/`.

## Run checks

```bash
scripts/run_checks.sh
```

## Safety

Use these tools only for your own systems or systems where you have explicit permission.
