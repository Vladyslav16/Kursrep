import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os


# Функція авторизації
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Успіх", "Успішний вхід!")
    else:
        messagebox.showerror("Помилка", "Неправильне ім'я користувача або пароль.")


def register():
    messagebox.showinfo("Реєстрація", "Тут має бути реєстрація")


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

tk.Label(root, text="Авторизація:", **Config).grid(row=0, column=0, columnspan=2, padx=10, pady=5)
tk.Label(root, text="Або", **Config).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Поля вводу
# Ім'я
tk.Label(root, text="Введіть ім'я:", **Config).grid(row=1, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root, **Config)
username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
# Пароль
tk.Label(root, text="Введіть пароль:", **Config).grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*", **Config)
password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Кнопки
# Увійти
login_button = tk.Button(root, text="Увійти", **Config, command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)
# Зареєстуватися
register_button = tk.Button(root, text="Зареєструватися", **Config, command=register)
register_button.grid(row=5, column=0, columnspan=2, pady=10)

# Запуск програми
root.mainloop()
