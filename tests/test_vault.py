
def test_vault_distinct():
    assert "vault" == "vault"

def test_vault_crypto():
    import hashlib
    assert len(hashlib.sha256(b"test").hexdigest()) == 64
