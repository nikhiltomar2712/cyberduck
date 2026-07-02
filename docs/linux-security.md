# Linux Security Basics

## Account hygiene

- Disable unused accounts.
- Use SSH keys instead of passwords where possible.
- Avoid logging in directly as root.
- Review sudo access regularly.

## Useful read-only commands

```bash
whoami
id
uname -a
ss -tulpen
systemctl --failed
last -a | head
```

## File permissions

- `chmod 600 file` for private files.
- `chmod 700 directory` for private directories.
- Avoid world-writable paths unless required.
- Review sensitive files such as `/etc/passwd`, `/etc/shadow`, and SSH configs.

## Logging

Important logs may be available through:

```bash
journalctl -p warning..alert
journalctl -u sshd
```
