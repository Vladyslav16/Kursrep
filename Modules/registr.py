import tkinter as tk
from myLib.window import *
from tkinter import messagebox
from Modules.admin import Admin
import os
from Modules.action_log import log_action


def show_about():
    """Виводить інформацію про програму."""
    messagebox.showinfo("Про програму", "Ця програма створена для авторизації користувачів та надання їм прав доступу "
                                        "для перегляду ресурсу.")


def show_access():
    pass


# Клас вікна реєстрації
class Register(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master  # Зберігаємо посилання на кореневе вікно

        # Меню
        self.create_menu()

        # Розміщення вмісту за допомогою grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self, text="Вікно реєстрації:", **LabelConfig).grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Поля вводу
        tk.Label(self, text="Введіть ім'я:", **LabelConfig).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(self, **EntryConfig)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        tk.Label(self, text="Введіть пароль:", **LabelConfig).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(self, show="*", **EntryConfig)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Поле для вибору типу користувача
        tk.Label(self, text="Тип користувача:", **LabelConfig).grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.user_type_var = tk.StringVar(value="user")  # Значення за замовчуванням — "user"
        user_type_menu = tk.OptionMenu(self, self.user_type_var, "user", "admin")
        user_type_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Поле для вибору рівня доступу
        tk.Label(self, text="Рівень доступу:", **LabelConfig).grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.access_level_var = tk.StringVar(value="C")  # Значення за замовчуванням — "C"
        access_level_menu = tk.OptionMenu(self, self.access_level_var, "A", "B", "C")
        access_level_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Кнопка підтвердження
        login_button = tk.Button(self, text="Підтвердити", **ButtonConfig, command=self.new_user_reg)
        login_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Кнопка для повернення
        button_back = tk.Button(self, text="Назад", **ButtonConfig,
                                command=self.open_previous_window)
        button_back.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    def new_user_reg(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type_var.get()
        access_level = self.access_level_var.get()

        # Шлях до файлів
        admin_file = "data/admin.txt"
        user_file = "data/nameuser.txt"

        if not username or not password:
            messagebox.showerror("Помилка", "Будь ласка, заповніть усі поля!")
            return

        if user_type == "admin":
            file_path = admin_file
            access_level = "A"  # Адміністратор завжди має рівень доступу "A"
        else:
            file_path = user_file

        # Перевіряємо, чи існує файл, і створюємо його, якщо він відсутній
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                pass

        # Перевірка, чи вже існує користувач
        with open(file_path, "r") as f:
            for line in f:
                existing_username, _, _ = line.strip().split(":", 2)
                if username == existing_username:
                    messagebox.showerror("Помилка", f"Користувач '{username}' вже існує!")
                    log_action("System", f"Помилка при реєстрації: Користувач '{username}' вже існує")  # Логування
                    return

        # Додавання нового користувача
        with open(file_path, "a") as f:
            f.write(f"{username}:{password}:{access_level}\n")
        messagebox.showinfo("Успіх", f"Користувача '{username}' успішно зареєстровано!")
        log_action("System", f"Новий користувач '{username}' успішно зареєстрований")  # Логування
        self.clear_entries()

    def clear_entries(self):
        """Очищує поля вводу."""
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def create_menu(self):
        """Створює меню для вікна."""
        menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(menu_bar, **MenuConfig)
        file_menu_1 = tk.Menu(menu_bar, **MenuConfig)

        menu_bar.add_cascade(label="Settings", menu=file_menu)
        file_menu.add_command(label="Про програму", command=show_about)
        file_menu.add_separator()
        file_menu.add_command(label="Вийти", command=self.master.quit)

        #menu_bar.add_cascade(label="Access", menu=file_menu_1)
        #file_menu_1.add_command(label="Перевірити рівень доступу")

        self.master.config(menu=menu_bar)

    def open_previous_window(self):
        switch_window(self.master, Admin)
