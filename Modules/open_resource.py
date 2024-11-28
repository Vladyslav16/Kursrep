import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os
from Modules.action_log import log_action


class ResourceWindow(tk.Toplevel):
    def __init__(self, master, file_path="data/out.txt"):
        super().__init__(master)
        self.title("Ресурс")
        win_to_center(self, 760, 460)

        # Читаємо дані з файлу out.txt
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            log_action("User", f"Ресурс відкрито: {file_path}")  # Логування події
        else:
            content = "Файл не знайдено!"
            log_action("User", f"Спроба відкрити відсутній файл: {file_path}")  # Логування події

        # Текстове поле для відображення контенту
        text_widget = tk.Text(self, wrap=tk.WORD)
        text_widget.insert(tk.END, content)
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Кнопка закриття вікна
        close_button = tk.Button(self, text="Закрити", command=self.destroy)
        close_button.pack(pady=10)


