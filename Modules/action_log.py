import tkinter as tk
from tkinter import messagebox
import os
import datetime
from myLib.window import *

LOG_FILE_PATH = "data/log.txt"


def log_action(user, action):
    """
    Логування дій користувача з міткою часу.

    :param user: Ім'я користувача, який виконав дію.
    :param action: Опис дії.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] User: {user}, Action: {action}\n"

    # Перевірка існування файлу журналу
    if not os.path.exists("data"):
        os.makedirs("data")

    with open(LOG_FILE_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)


def view_log():
    """
    Читає та повертає вміст журналу дій.

    :return: Вміст файлу журналу у вигляді рядка.
    """
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
            return log_file.read()
    else:
        return "Лог-файл не знайдено."


def show_log_window(master):
    """Відображає журнал подій у новому вікні."""
    if not os.path.exists(LOG_FILE_PATH):
        messagebox.showerror("Помилка", "Лог-файл не знайдено!")
        return

    # Створюємо нове вікно
    log_window = tk.Toplevel(master)
    log_window.title("Журнал подій")
    win_to_center(master, 760, 460)

    # Читаємо вміст файлу
    with open(LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
        log_content = log_file.read()

    # Текстове поле для відображення логу
    text_widget = tk.Text(log_window, wrap=tk.WORD)
    text_widget.insert(tk.END, log_content)
    text_widget.configure(state="disabled")  # Робимо текстове поле лише для читання
    text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Кнопка закриття
    close_button = tk.Button(log_window, text="Закрити", command=log_window.destroy)
    close_button.pack(pady=10)
