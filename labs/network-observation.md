# Lab: Network Observation

Goal: understand normal network behavior on a machine you own.

## Safe commands

```bash
ip addr
ip route
ss -tulpen
resolvectl status 2>/dev/null || cat /etc/resolv.conf
```

## Questions

- What IP address does your machine use?
- What DNS servers are configured?
- Which local services are listening?
- Are any listening services surprising?

## Cleanup

This lab is read-only and should not change system state.
