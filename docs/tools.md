# Cyberduck Tools

Small defensive utilities live in `tools/`.

## Available tools

- `password_strength_checker.py` — offline password strength feedback.
- `file_hash.py` — generate file hashes for integrity verification.
- `security_headers_check.py` — review common HTTP security headers for authorized sites.
- `local_port_inventory.py` — list local listening ports without remote scanning.
- `log_failed_login_summary.py` — summarize failed-login-like log lines.

## Run checks

```bash
scripts/run_checks.sh
```

## Safety

Use these tools only for your own systems or systems where you have explicit permission.
