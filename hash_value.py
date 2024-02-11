import hashlib


def get_hash(data, algorithm="sha256"):
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(data.encode("utf-8"))
    return hash_obj.hexdigest()


data = "Привет, как дела?"

hash_sha256 = get_hash(data)
print(f"SHA-256: {hash_sha256}")

hash_md5 = get_hash(data, algorithm="md5")
print(f"MD5: {hash_md5}")
