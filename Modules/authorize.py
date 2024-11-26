import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os
from Modules.admin import Admin
from Modules.user import User


# Функція для зчитування даних(ім'я,пароль) з файлу
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


# Клас вікна авторизації
class AuthorizeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Розміщення вмісту за допомогою grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self, text="Авторизація:", **LabelConfig).grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Поля вводу
        tk.Label(self, text="Введіть ім'я:", **LabelConfig).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(self, **EntryConfig)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self, text="Введіть пароль:", **LabelConfig).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(self, show="*", **EntryConfig)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Кнопка входу
        login_button = tk.Button(self, text="Увійти", **ButtonConfig, command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Шлях до файлів
        admin_file = "data/admin.txt"
        user_file = "data/nameuser.txt"

        # Зчитуємо дані з файлів
        admin_credentials = read_credentials(admin_file)
        user_credentials = read_credentials(user_file)

        if username in admin_credentials and admin_credentials[username] == password:
            messagebox.showinfo("Успіх", "Авторизований, як Адміністратор")
            switch_window(self.master, Admin)  # Відкриваємо вікно адміністратора
        elif username in user_credentials and user_credentials[username] == password:
            messagebox.showinfo("Успіх", "Авторизований, як Користувач")
            switch_window(self.master, User)  # Відкриваємо вікно користувача
        else:
            messagebox.showerror("Помилка", "Неправильне ім'я користувача або пароль.")
