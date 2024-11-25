from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path, initialvalue=None):
        self.password_file = path

        if initialvalue is not None:
            for site, password in initialvalue.items():
                self.add_password(site, password)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.strip().split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode()).decode()
                f.write(f"{site}:{encrypted}\n")

    def get_password(self, site):
        return self.password_dict.get(site, "Password not found.")

def main():
    passwords = {
        "email": "Quartz453",
        "instagram": "5864788",
        "YouTube": "Hello1234",
        "Something": "hafuhfhhfbd"
    }

    pm = PasswordManager()

    print("""
        What do you want to do?
        (1) Create a new key
        (2) Load an existing key
        (3) Create a new password file
        (4) Load existing password file
        (5) Add a new password
        (6) Get a password
        (7) QUIT
        """)
    
    done = False
    while not done:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                path = input("Enter path to save the key: ")
                pm.create_key(path)
            elif choice == 2:
                path = input("Enter path to load the key: ")
                pm.load_key(path)
            elif choice == 3:
                path = input("Enter path to create password file: ")
                pm.create_password_file(path, passwords)
            elif choice == 4:
                path = input("Enter path to load password file: ")
                pm.load_password_file(path)
            elif choice == 5:
                site = input("Enter site: ")
                password = input("Enter the password: ")
                pm.add_password(site, password)
            elif choice == 6:
                site = input("What site do you want the password for? ")
                print(f"Password for {site}: {pm.get_password(site)}")
            elif choice == 7:
                done = True
                print("Goodbye!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
