# Web App Security Review Checklist

## Authentication

- [ ] Password reset tokens expire quickly.
- [ ] MFA is available for sensitive accounts.
- [ ] Login and reset endpoints are rate limited.

## Authorization

- [ ] Users cannot access another user's data by changing IDs.
- [ ] Admin actions are protected server-side.
- [ ] API routes check permissions consistently.

## Data protection

- [ ] Secrets are not committed to source control.
- [ ] Sensitive data is encrypted in transit.
- [ ] Error messages do not leak internals.
