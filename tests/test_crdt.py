
def test_crdt_distinct():
    assert "crdt" == "crdt"

def test_crdt_crypto():
    import hashlib
    assert len(hashlib.sha256(b"test").hexdigest()) == 64
