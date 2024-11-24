'''import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os



    register_window = tk.Tk()
    register_window.title("Реєстрація")
    win_to_center(register_window, 600, 300)

    # Центрування вмісту за допомогою grid
    register_window.grid_rowconfigure(0, weight=1)
    register_window.grid_rowconfigure(1, weight=1)
    register_window.grid_rowconfigure(2, weight=1)
    register_window.grid_rowconfigure(3, weight=1)
    register_window.grid_columnconfigure(0, weight=1)
    register_window.grid_columnconfigure(1, weight=1)

    tk.Label(register_window, text="Реєстрація нового користувача:").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
    # Поля вводу
    tk.Label(register_window, text="Ім'я:").grid(row=1, column=0, padx=10, pady=5)
    tk.Entry(register_window).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(register_window, text="Пароль:").grid(row=2, column=0, padx=10, pady=5)
    tk.Entry(register_window, show="*").grid(row=2, column=1, padx=10, pady=5)

    # Кнопки
    register_button = tk.Button(register_window, text="Зареєструватися", command=lambda: messagebox.showinfo("Реєстрація", "Успішно!"))
    register_button.grid(row=3, column=0, pady=10)

    return_button = tk.Button(register_window, text="Назад", command=return_to_login)
    return_button.grid(row=3, column=1, pady=10)
'''