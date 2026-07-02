# Web Application Security Notes

## Common risk areas

- Broken access control
- Injection flaws
- Cross-site scripting
- Insecure authentication and sessions
- Security misconfiguration
- Vulnerable dependencies
- Sensitive data exposure

## Defensive checklist

- Validate and encode user-controlled input.
- Use parameterized queries.
- Enforce authorization on the server side.
- Set secure cookie flags: `HttpOnly`, `Secure`, and `SameSite`.
- Add rate limits to sensitive actions.
- Keep dependencies patched.
- Use HTTPS everywhere.

## Security headers

Helpful headers include:

```text
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options: nosniff
Referrer-Policy
Permissions-Policy
```
