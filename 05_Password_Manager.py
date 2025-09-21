# PASSWORD MANAGER

from cryptography.fernet import Fernet, InvalidToken

def load_key():
    with open("key.key", "rb") as f:
        return f.read()

try:
    key = load_key()
    fer = Fernet(key)
except FileNotFoundError:
    print("ERROR: key.key not found. Create or place the correct key.key file next to this script.")
    raise SystemExit(1)
except Exception as e:
    print("ERROR loading key:", e)
    raise SystemExit(1)

def view():
    try:
        with open('passwords.txt', 'r', encoding='utf-8') as f:
            for lineno, line in enumerate(f, start=1):
                data = line.rstrip('\n')
                if not data:
                    continue
                parts = data.split("|", 1)
                if len(parts) != 2:
                    print(f"Skipping malformed line {lineno}: {data}")
                    continue
                user, token = parts
                try:
                    pwd = fer.decrypt(token.encode()).decode()
                    print("User:", user, ", Password:", pwd)
                except InvalidToken:
                    print(f"Line {lineno} — User: {user}  —  Password: <unable to decrypt: InvalidToken>")
                except Exception as e:
                    print(f"Line {lineno} — User: {user}  —  Password: <decrypt error: {e}>")
    except FileNotFoundError:
        print("No passwords file found. Add one first with 'add'.")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    token = fer.encrypt(pwd.encode()).decode()   # store token as text
    with open('passwords.txt', 'a', encoding='utf-8') as f:
        f.write(name + "|" + token + "\n")
    print("Saved.")

if __name__ == "__main__":
    while True:
        try:
            mode = input("Would you like to add a new password or view existing ones (view/add), press q to quit? ").lower()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if mode == "q":
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid Mode.")
            continue
