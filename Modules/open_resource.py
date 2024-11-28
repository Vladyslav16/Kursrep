import tkinter as tk
from myLib.window import *
from Modules.authorize import current_user
from Modules.elgamal import generate_keys, encrypt_text, decrypt_text
from tkinter import messagebox
import os
from Modules.action_log import log_action


# Параметри для алгоритма Ель-Гамаля
p = 7919  # Просте число
g = 2     # Примітивний корінь
private_key, public_key = generate_keys(p, g)


def save_file(file_path, text_widget):
    """Зберігає зміни у файлі."""
    content = text_widget.get("1.0", tk.END).strip()
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    log_action(current_user["username"], f"Збережено зміни у файлі: {file_path}")
    messagebox.showinfo("Успіх", "Зміни збережено!")


def read_file(file_path):
    """Читання змісту файлу."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Файл не знайдено!"


class ResourceWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Ресурс")
        win_to_center(self, 760, 460)

        access_level = current_user["access_level"]
        username = current_user["username"]

        # Відображення контенту в залежності від рівня доступу
        if access_level == "A":  # Адміністратор
            file_path = "data/input.txt"
            content = read_file(file_path)
            log_action(username, f"Відкрито ресурс для редагування: {file_path}")
            self.create_text_widget(content, editable=True, save_path=file_path)
        elif access_level == "B":  # Доступ тільки для читання
            file_path = "data/out.txt"
            content = read_file(file_path)
            log_action(username, f"Відкрито розшифрований ресурс для читання: {file_path}")
            self.create_text_widget(content, editable=False)
        elif access_level == "C":  # Доступ до зашифрованного файлу
            file_path = "data/close.txt"
            content = read_file(file_path)
            log_action(username, f"Відкрито зашифрованний ресурс в силу низького доступу: {file_path}")
            self.create_text_widget(content, editable=False)
        else:
            content = "У вас немає доступу до ресурсу."
            log_action(username, "Невдалий доступ до ресурсу")
            self.create_text_widget(content, editable=False)

    def create_text_widget(self, content, editable=False, save_path=None):
        """Створює текстовий віджет з вказаним змістом."""
        text_widget = tk.Text(self, wrap=tk.WORD)
        text_widget.insert(tk.END, content)
        if not editable:
            text_widget.configure(state="disabled")
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        if editable:
            save_button = tk.Button(self, text="Зберегти", command=lambda: save_file(save_path, text_widget))
            save_button.pack(pady=10)

        close_button = tk.Button(self, text="Закрити", command=self.destroy)
        close_button.pack(pady=10)


