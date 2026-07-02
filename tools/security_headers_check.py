#!/usr/bin/env python3
"""Check defensive HTTP security headers for a URL.

Only run this against sites you own or have permission to assess.
"""

from __future__ import annotations

import argparse
import sys
import urllib.request

RECOMMENDED_HEADERS = {
    "content-security-policy": "Helps reduce cross-site scripting impact.",
    "strict-transport-security": "Forces HTTPS after first trusted visit.",
    "x-content-type-options": "Prevents MIME sniffing.",
    "referrer-policy": "Limits referrer data leakage.",
    "permissions-policy": "Restricts powerful browser features.",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Check common HTTP security headers.")
    parser.add_argument("url", help="URL to check, for example https://example.com")
    args = parser.parse_args()

    request = urllib.request.Request(args.url, headers={"User-Agent": "cyberduck-header-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            headers = {key.lower(): value for key, value in response.headers.items()}
            print(f"Status: {response.status}")
    except Exception as exc:  # noqa: BLE001 - CLI should show concise error
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    for header, reason in RECOMMENDED_HEADERS.items():
        if header in headers:
            print(f"PASS {header}: {headers[header]}")
        else:
            print(f"MISS {header}: {reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
