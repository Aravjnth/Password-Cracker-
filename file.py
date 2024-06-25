import hashlib

def password_crack(hash, wordlist):
    for word in wordlist:
        hashed_word = hashlib.sha256(word.encode()).hexdigest()
        if hashed_word == hash:
            return word
    return None

hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
wordlist = ["password", "iloveyou", "dragonball"]
cracked_password = password_crack(hash, wordlist)
print(f"Cracked password: {cracked_password}")