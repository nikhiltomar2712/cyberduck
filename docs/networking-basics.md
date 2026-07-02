# Networking Basics for Security

## Layers to know

- **Link layer:** local network communication, MAC addresses, switches.
- **Network layer:** IP addressing and routing.
- **Transport layer:** TCP and UDP ports.
- **Application layer:** HTTP, DNS, SSH, SMTP, and other protocols.

## Ports worth recognizing

| Port | Protocol | Typical use |
| --- | --- | --- |
| 22 | SSH | remote administration |
| 53 | DNS | name resolution |
| 80 | HTTP | web traffic |
| 443 | HTTPS | encrypted web traffic |
| 3389 | RDP | Windows remote desktop |

## Defensive checks

- Know which services should be exposed.
- Block unnecessary inbound traffic.
- Monitor DNS and outbound connections for unusual patterns.
- Prefer encrypted protocols over plaintext protocols.
