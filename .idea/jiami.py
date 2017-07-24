import hashlib
hash = hashlib.md5()
hash.update('admin')
print hash.digest()
print hash.hexdigest()