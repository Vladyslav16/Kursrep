import tkinter as tk
from myLib.window import *
from tkinter import messagebox
from Modules.admin import Admin


def show_about():
    """Виводить інформацію про програму."""
    messagebox.showinfo("Про програму", "Ця програма створена для авторизації користувачів та надання їм прав доступу "
                                        "для перегляду ресурсу.")


def show_access():
    pass


# Клас вікна адміна
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

        # Кнопка входу
        login_button = tk.Button(self, text="Підтвердити", **ButtonConfig, command=self.new_user_reg)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Кнопка для повернення
        button_back = tk.Button(self, text="Назад", **ButtonConfig,
                                command=self.open_previous_window)
        button_back.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def new_user_reg(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Шлях до файлів
        admin_file = "data/admin.txt"
        user_file = "data/nameuser.txt"

    def create_menu(self):
        """Створює меню для вікна."""
        menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(menu_bar, **MenuConfig)
        file_menu_1 = tk.Menu(menu_bar, **MenuConfig)

        menu_bar.add_cascade(label="Settings", menu=file_menu)
        file_menu.add_command(label="Про програму")
        file_menu.add_separator()
        file_menu.add_command(label="Вийти", command=self.master.quit)

        menu_bar.add_cascade(label="Access", menu=file_menu_1)
        file_menu_1.add_command(label="Перевірити рівень доступу")

        self.master.config(menu=menu_bar)

    def open_previous_window(self):
        from main import AuthorizeWindow
        switch_window(self.master, Admin)