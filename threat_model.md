# STRIDE Threat Model – Tawakkalna

## Spoofing
- Stolen credentials
- Fake Nafath requests  
**Mitigation:** MFA, device binding, short-lived tokens.

## Tampering
- Modifying QR codes or health status  
**Mitigation:** Digital signatures, input validation, audit logs.

## Repudiation
- Denying permit or API actions  
**Mitigation:** Immutable logs, timestamps, API tracing.

## Information Disclosure
- Leaking health or location data  
**Mitigation:** Encryption, RBAC, secure APIs.

## Denial of Service
- Overloading login or status endpoints  
**Mitigation:** Rate limiting, WAF, auto-scaling.

## Elevation of Privilege
- Normal user gains admin access  
**Mitigation:** Least privilege, IAM reviews, per-service API keys.
