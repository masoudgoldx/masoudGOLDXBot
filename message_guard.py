
import hashlib
import os

HASH_FILE = "last_message.hash"

def is_new_message(message):
    current_hash = hashlib.sha256(message.encode("utf-8")).hexdigest()

    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            last_hash = f.read().strip()
            if last_hash == current_hash:
                return False  # پیام قبلاً ارسال شده

    with open(HASH_FILE, "w") as f:
        f.write(current_hash)

    return True  # پیام جدید است
