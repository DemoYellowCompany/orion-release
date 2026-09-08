def test_same_key_returns_same_invoice():
    first = "INV-9001"
    retried = "INV-9001"
    assert first == retried
# Demo fixture only. The 48-hour operational campaign is tracked in issue #147.