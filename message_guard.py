
import hashlib
import os

HASH_FILE = "last_message.hash"

def is_new_message(message):
    h = hashlib.sha256(message.encode()).hexdigest()
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE) as f:
            if f.read().strip() == h:
                return False
    with open(HASH_FILE, "w") as f:
        f.write(h)
    return True
