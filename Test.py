import random
from sympy import isprime

# Генерація простого числа для алгоритму шифрування
def generate_prime(limit=1000):
    while True:
        p = random.randint(2, limit)
        if isprime(p):
            return p

# Алгоритм шифрування/розшифрування Аль-Гамаля
class ElGamal:
    def __init__(self, p=None, g=None, x=None):
        self.p = p if p else generate_prime()
        self.g = g if g else random.randint(2, self.p - 1)
        self.x = x if x else random.randint(1, self.p - 2)
        self.y = pow(self.g, self.x, self.p)

    def encrypt(self, m):
        k = random.randint(1, self.p - 2)
        a = pow(self.g, k, self.p)
        b = (m * pow(self.y, k, self.p)) % self.p
        return a, b

    def decrypt(self, a, b):
        s = pow(a, self.x, self.p)
        m = (b * pow(s, -1, self.p)) % self.p
        return m

# Клас користувача
class User:
    def __init__(self, username, password, access_level):
        self.username = username
        self.password = password
        self.access_level = access_level

# Клас адміністратор
class Admin:
    def __init__(self):
        self.users = []

    def register_user(self, username, password, access_level):
        # Генерація ключів для користувача
        elgamal = ElGamal()
        encrypted_password = elgamal.encrypt(int(password))
        user = {
            "username": username,
            "password": encrypted_password,
            "access_level": access_level,
            "keys": {
                "p": elgamal.p,
                "g": elgamal.g,
                "y": elgamal.y,
            },
        }
        self.users.append(user)
        self.save_users()

    def save_users(self):
        with open("respy.txt", "w") as file:
            for user in self.users:
                file.write(f"{user}\n")

    def load_users(self):
        try:
            with open("respy.txt", "r") as file:
                for line in file:
                    self.users.append(eval(line.strip()))
        except FileNotFoundError:
            pass

    def authenticate_user(self, username, password):
        for user in self.users:
            if user["username"] == username:
                elgamal = ElGamal(
                    p=user["keys"]["p"],
                    g=user["keys"]["g"],
                    x=None,  # Закритий ключ не зберігається
                )
                decrypted_password = elgamal.decrypt(
                    *user["password"]
                )
                if int(password) == decrypted_password:
                    return user["access_level"]
        return None

# Основна логіка
if __name__ == "__main__":
    admin = Admin()
    admin.load_users()

    while True:
        print("1. Зареєструвати користувача")
        print("2. Авторизуватись")
        print("3. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            username = input("Ім'я користувача: ")
            password = input("Пароль (число): ")
            access_level = input("Рівень доступу: ")
            admin.register_user(username, password, access_level)
            print("Користувача зареєстровано!")
        elif choice == "2":
            username = input("Ім'я користувача: ")
            password = input("Пароль (число): ")
            access_level = admin.authenticate_user(username, password)
            if access_level:
                print(f"Авторизація успішна! Рівень доступу: {access_level}")
            else:
                print("Невірний логін або пароль")
        elif choice == "3":
            break
        else:
            print("Невірний вибір!")
