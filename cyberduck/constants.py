"""Shared constants for defensive security helpers."""

RECOMMENDED_SECURITY_HEADERS = {
    "content-security-policy": "Reduce XSS impact with an allowlist policy.",
    "strict-transport-security": "Ask browsers to keep using HTTPS.",
    "x-content-type-options": "Prevent MIME type sniffing.",
    "referrer-policy": "Limit referrer data leakage.",
    "permissions-policy": "Restrict powerful browser features.",
}

COMMON_PORTS = {
    20: "FTP data",
    21: "FTP control",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "Alternate HTTP",
}

RISKY_PUBLIC_PORTS = {21, 23, 445, 1433, 3306, 3389, 5432, 6379, 9200, 27017}
WEAK_PASSWORD_WORDS = {"password", "admin", "welcome", "qwerty", "letmein", "dragon"}
WEAK_HASHES = {"md5", "sha1"}
