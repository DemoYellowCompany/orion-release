# PR #388 - Enforce invoice idempotency
Status: MERGED
Merged: 16 September 2026 14:20
Author: Karim Haddad

## Changes
- Persist idempotency key before payment-provider call.
- Return existing invoice on repeated request.
- Add integration tests for basic timeout and retry.

## Review note
Maya Trabelsi: code coverage is acceptable, but the operational 48-hour campaign remains mandatory.
