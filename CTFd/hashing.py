from hashlib import md5, sha256

def hash(inp):
    try:
        inp = inp.encode()
    except:
        pass
    finally:
        return md5(sha256(inp).hexdigest().encode()).hexdigest()