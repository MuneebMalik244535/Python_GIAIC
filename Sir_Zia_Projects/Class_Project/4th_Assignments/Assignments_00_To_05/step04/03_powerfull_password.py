from hashlib import sha256  # ✅ Import SHA-256 for hashing

def hash_password(password):
    """🔐 Convert password to a SHA-256 hash."""
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """✅ Verify if the given password matches the stored hash for the email."""
    return stored_logins.get(email) == hash_password(password_to_check)

def main():
    # ✅ Dictionary storing emails & their hashed passwords
    stored_logins = {
        "example@gmail.com": hash_password("password"),  # 🔑 Pre-hashed passwords
        "code_in_placer@cip.org": hash_password("Karel"),
        "student@stanford.edu": hash_password("123!456?789")
    }
    
    # ✅ Test cases to verify login functionality
    print(login("example@gmail.com", stored_logins, "word"))  # ❌ False
    print(login("example@gmail.com", stored_logins, "password"))  # ✅ True
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # ✅ True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # ❌ False
    print(login("student@stanford.edu", stored_logins, "password"))  # ❌ False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # ✅ True

if __name__ == '__main__':
    main()
