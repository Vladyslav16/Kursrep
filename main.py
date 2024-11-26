import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os


# Функція для зчитування даних з файлу
def read_credentials(file_path):
    credentials = {}
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                username, password = line.strip().split(":")
                credentials[username] = password
    else:
        messagebox.showerror("Помилка", f"Файл {file_path} не знайдено!")
    return credentials


# Функція авторизації
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Шлях до файлів
    admin_file = "data/admin.txt"
    user_file = "data/nameuser.txt"

    # Зчитуємо дані з файлів
    admin_credentials = read_credentials(admin_file)
    user_credentials = read_credentials(user_file)

    if username in admin_credentials and admin_credentials[username] == password:
        messagebox.showinfo("Успіх", "Адміністратор")
        # open_admin_window()  # Відкриваємо вікно адміністратора
    elif username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo("Успіх", "Користувач")
        #open_user_window()  # Відкриваємо вікно користувача
    else:
        messagebox.showerror("Помилка", "Неправильне ім'я користувача або пароль.")


# Головне вікно
root = tk.Tk()
root.title("Система ідентифікації користувачів")
win_to_center(root, 660, 330)

# Центрування вмісту за допомогою grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

tk.Label(root, text="Авторизація:", **LabelConfig).grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# Поля вводу
# Ім'я
tk.Label(root, text="Введіть ім'я:", **LabelConfig).grid(row=1, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root, **EntryConfig)
username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
# Пароль
tk.Label(root, text="Введіть пароль:", **LabelConfig).grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*", **EntryConfig)
password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Кнопки
# Увійти
login_button = tk.Button(root, text="Увійти", **ButtonConfig, command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

# Запуск програми
if __name__ == "__main__":
    root.mainloop()
