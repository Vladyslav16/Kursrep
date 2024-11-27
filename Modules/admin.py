import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os
from Modules.open_resource import ResourceWindow
from Modules.all_users import UserListWindow


def show_about():
    """Виводить інформацію про програму."""
    messagebox.showinfo("Про програму", "Ця програма створена для авторизації користувачів та надання їм прав доступу "
                                        "для перегляду ресурсу.")


def show_access(file_path):
    """Відображає рівень доступу поточного користувача."""
    messagebox.showinfo("Ваш доступ",  f"Рівень: '{check_access_level(file_path)}'")


def check_access_level(file_path):
    """Зчитує дані з файлу та повертає рівні доступу користувачів."""
    your_level = {}
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding="utf_8") as f:
            for line in f:
                username, _, access_level = line.strip().split(":", 2)
                your_level[username] = _, access_level
    else:
        messagebox.showerror("Помилка", f"Файл {file_path} не знайдено!")
    return your_level


# Клас вікна адміна
class Admin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master  # Зберігаємо посилання на кореневе вікно
        self.credentials_file = "data/admin.txt"  # Шлях до файлу з даними адмінів

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

        tk.Label(self, text="Вікно адміна:", **LabelConfig).grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Кнопки адмінського вікна
        button_resource = tk.Button(self, text="Відкрити ресурс", **ButtonConfig, command=self.open_resource)
        button_resource.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        button_register = tk.Button(self, text="Зареєструвати нового користувача", **ButtonConfig, command=self.registr)
        button_register.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        button_users = tk.Button(self, text="Список користувачів", **ButtonConfig, command=self.open_user_list)
        button_users.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        button_log = tk.Button(self, text="Переглянути журнал подій", **ButtonConfig)
        button_log.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Кнопка для повернення
        button_back = tk.Button(self, text="Назад", **ButtonConfig,
                                command=self.open_previous_window)
        button_back.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def create_menu(self):
        """Створює меню для вікна."""
        menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(menu_bar, **MenuConfig)
        file_menu_1 = tk.Menu(menu_bar, **MenuConfig)

        menu_bar.add_cascade(label="Settings", menu=file_menu)
        file_menu.add_command(label="Про програму", command=show_about)
        file_menu.add_separator()
        file_menu.add_command(label="Вийти", command=self.master.quit)

        menu_bar.add_cascade(label="Access", menu=file_menu_1)
        file_menu_1.add_command(label="Перевірити рівень доступу", command=lambda: show_access(self.credentials_file))

        self.master.config(menu=menu_bar)

    def open_previous_window(self):
        from main import AuthorizeWindow
        switch_window(self.master, AuthorizeWindow)

    def registr(self):
        from main import Register
        switch_window(self.master, Register)

    def open_resource(self):
        """Відкриває нове вікно з ресурсом."""
        ResourceWindow(self.master)

    def open_user_list(self):
        """Відкриває список користувачів """
        UserListWindow(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Program")
    win_to_center(root, 660, 330)
    # Налаштування головного контейнера
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Запуск головного екрану
    main_screen = Admin(root)
    main_screen.grid(row=0, column=0, sticky="nsew")

    root.mainloop()
