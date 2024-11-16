import time
import bcrypt

# Дані користувачів
users = {
    "admin": bcrypt.hashpw("password".encode(), bcrypt.gensalt())
}

# Функція входу
def login():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")

    if username in users and bcrypt.checkpw(password.encode(), users[username]):
        print("Успішний вхід!")
        return True
    else:
        print("Неправильне ім'я користувача або пароль.")
        return False

# Головне меню
def main_menu():
    while True:
        print("\nГоловне меню")
        print("1. Вхід у систему")
        print("2. Вихід")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            if login():
                user_menu()
        elif choice == "2":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Меню для авторизованих користувачів
def user_menu():
    while True:
        print("\nМеню користувача")
        print("1. Перегляд журналу")
        print("2. Шифрування даних")
        print("3. Вихід")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            print("Показ журналу...")
        elif choice == "2":
            print("Шифрування даних...")
        elif choice == "3":
            print("Вихід до головного меню.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    main_menu()
