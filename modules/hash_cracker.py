import hashlib

def crack(hash_value, wordlist_path):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                word = line.strip()
                if hashlib.md5(word.encode()).hexdigest() == hash_value:
                    return f"MD5: {word}"
                if hashlib.sha1(word.encode()).hexdigest() == hash_value:
                    return f"SHA1: {word}"
        return "Not found in wordlist."
    except Exception as e:
        return f"Error: {e}"
