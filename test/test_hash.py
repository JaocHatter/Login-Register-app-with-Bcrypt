from src.utils.hash_password import HashUtil

def test_hash_password():
    hashed = HashUtil.hash("12345678")
    assert HashUtil.verify("12345678", hashed)
    