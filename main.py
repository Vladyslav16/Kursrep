import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os


# Функція для входу
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":  # Проста перевірка
        messagebox.showinfo("Успіх", "Успішний вхід!")
    else:
        messagebox.showerror("Помилка", "Неправильне ім'я користувача або пароль.")


# Головне вікно
root = tk.Tk()
root.title("Система ідентифікації")
win_to_center(root, 600, 300)

# Центрування вмісту за допомогою grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Поля вводу
tk.Label(root, text="Ім'я користувача:").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Пароль:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Кнопка входу
login_button = tk.Button(root, text="Увійти", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)
register_button = tk.Button(root, text="Реєстрація", command=register)
register_button.grid(row=2, column=1, columnspan=2, pady=10)

# Запуск програми
root.mainloop()
