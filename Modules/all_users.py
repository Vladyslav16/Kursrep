import tkinter as tk
from tkinter import messagebox, ttk
import os
from myLib.window import *


def load_users():
    """Завантажуємо користувачів з файлів"""
    users = []
    files = ["data/admin.txt", "data/nameuser.txt"]

    for file in files:
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    username, password, access_level = line.strip().split(":", 2)
                    users.append(
                        {"username": username, "password": password, "access_level": access_level, "file": file})
        else:
            messagebox.showerror("Помилка", f"Файл {file} не знайдено!")

    return users


# Клас створення списку
def remove_user_from_file(user):
    """Видаляє користувача з відповідного файлу"""
    with open(user["file"], "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(user["file"], "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip().split(":", 1)[0] != user["username"]:
                f.write(line)


class UserListWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.tree = None
        self.title("Список користувачів")
        win_to_center(self, 760, 460)

        # Завантажуємо користувачів з файлів
        self.users = load_users()

        # Створюємо таблицю користувачів
        self.create_user_table()

        # Видалити користувача
        delete_button = tk.Button(self, text="Видалити", **ButtonConfig, command=self.delete_user)
        delete_button.pack(pady=10)

        # Закрити вікно
        close_button = tk.Button(self, text="Закрити", **ButtonConfig, command=self.destroy)
        close_button.pack(pady=10)

    def create_user_table(self):
        """Створюємо таблицю для відображення користувачів"""
        columns = ("username", "password", "access_level")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Налаштовуємо заголовки колонок
        self.tree.heading("username", text="Name")
        self.tree.heading("password", text="Password")
        self.tree.heading("access_level", text="Access")

        # Встановлюємо розмір колонок
        self.tree.column("username", width=200, anchor=tk.CENTER)
        self.tree.column("password", width=200, anchor=tk.CENTER)
        self.tree.column("access_level", width=100, anchor=tk.CENTER)

        # Додаємо дані до таблиці
        for user in self.users:
            self.tree.insert("", tk.END, values=(user["username"], user["password"], user["access_level"]))

    def delete_user(self):
        """Видаляє вибраного користувача"""
        selected_item = self.tree.selection()
        if not selected_item:
            pass

        # Отримуємо дані вибраного користувача
        values = self.tree.item(selected_item, "values")
        username_to_delete = values[0]

        # Підтвердження видалення
        confirm = messagebox.askyesno(
            "Підтвердження",
            f"Ви дійсно хочете видалити користувача '{username_to_delete}'?"
        )
        if confirm:
            # Видаляємо користувача зі списку
            selected_user = next((user for user in self.users if user["username"] == username_to_delete), None)
            if selected_user:
                self.users.remove(selected_user)

                # Видаляємо користувача з відповідного файлу
                remove_user_from_file(selected_user)

            # Оновлюємо таблицю
            self.tree.delete(selected_item)

            # Повідомлення про успішне видалення
            messagebox.showinfo("Успіх", f"Користувача '{username_to_delete}' успішно видалено!")

    def update_files(self):
        """Перезаписуємо файли"""
        for user in self.users:
            with open(user["file"], "r") as f:
                lines = f.readlines()

            with open(user["file"], "w") as f:
                for line in lines:
                    username, password, access_level = line.strip().split(":", 2)
                    if username == user["username"]:
                        f.write(f"{user['username']}:{user['password']}:{user['access_level']}\n")
                    else:
                        f.write(line)
        messagebox.showinfo("Успіх", "Зміни збережено!")

