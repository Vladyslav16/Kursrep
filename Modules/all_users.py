import tkinter as tk
from tkinter import messagebox
import os
from myLib.window import win_to_center


def remove_user_from_file(user):
    """Видаляє користувача з відповідного файлу"""
    # Читаємо рядки з файлу
    with open(user["file"], "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Перезаписуємо файл, без рядка з видаленим користувачем
    with open(user["file"], "w", encoding="utf-8") as f:
        for line in lines:
            if line.strip().split(":", 1)[0] != user["username"]:
                f.write(line)


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
class UserListWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.tree = None
        self.title("Список користувачів")
        win_to_center(self, 600, 400)

        # Завантажуємо користувачів з файлів
        self.users = load_users()

        # Створюємо таблицю користувачів
        self.create_user_list()

        # Видалити користувача
        delete_button = tk.Button(self, text="Видалити", **ButtonConfig, command=self.delete_user)
        delete_button.pack(pady=10)

        # Закрити вікно
        close_button = tk.Button(self, text="Закрити",**ButtonConfig, command=self.destroy)
        close_button.pack(pady=10)

    def create_user_list(self):
        """Створюємо таблицю для завантаження користувачів"""
        self.tree = tk.Listbox(self, width=80, height=15)
        self.tree.pack(pady=10)

        for user in self.users:
            display_text = f"{user['username']} | {user['password']} | {user['access_level']}"
            self.tree.insert(tk.END, display_text)

    def delete_user(self):
        """Видаляє вибраного користувача"""
        selected_index = self.tree.curselection()
        if not selected_index:
            pass

        selected_user = self.users[selected_index[0]]

        # Підтвердження видалення
        confirm = messagebox.askyesno("Підтвердження",
                                      f"Ви дійсно хочете видалити користувача '{selected_user['username']}'?")
        if confirm:
            # Видаляємо користувача зі списку
            self.users.remove(selected_user)

            # Оновлюємо Listbox
            self.tree.delete(selected_index[0])

            # Видаляємо користувача з файлу
            remove_user_from_file(selected_user)

            messagebox.showinfo("Успіх", f"Користувача '{selected_user['username']}' успішно видалено!")

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

