import tkinter as tk
from myLib.window import *
from Modules.elgamal import generate_keys, encrypt_text, decrypt_text, text_to_int, int_to_text
from tkinter import messagebox
import os
from Modules.action_log import log_action


# Параметри для алгоритма Ель-Гамаля
p = 7919  # Просте число
g = 2     # Примітивний корінь
private_key, public_key = generate_keys(p, g)


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
        win_to_center(self, 760, 560)
        from Modules.authorize import current_user
        self.access_level = current_user["access_level"]
        self.username = current_user["username"]

        # Відображення контенту в залежності від рівня доступу
        if self.access_level == "A":  # Адміністратор
            file_path = "data/input.txt"
            content = read_file(file_path)
            log_action(self.username, f"Відкрито ресурс для редагування: {file_path}")
            self.create_text_widget(content, editable=True, save_path=file_path)
        elif self.access_level == "B":  # Доступ тільки для читання
            self.decrypt_close_to_out()
            file_path = "data/out.txt"
            content = read_file(file_path)
            log_action(self.username, f"Відкрито розшифрований ресурс для читання: {file_path}")
            self.create_text_widget(content, editable=False)
        elif self.access_level == "C":  # Доступ до зашифрованного файлу
            file_path = "data/close.txt"
            content = read_file(file_path)
            log_action(self.username, f"Відкрито зашифрованний ресурс в силу низького доступу: {file_path}")
            self.create_text_widget(content, editable=False)
        else:
            content = "У вас немає доступу до ресурсу."
            log_action(self.username, "Невдалий доступ до ресурсу")
            self.create_text_widget(content, editable=False)

    def encrypt_input_to_close(self, text):
        """Шифрування тексту input.txt і запис в close.txt."""
        plaintext_int = text_to_int(text)  # Конвертуємо текст в число
        c1, c2 = encrypt_text(p, g, public_key, plaintext_int)  # Зашифровка тексту
        with open("data/close.txt", "w", encoding="utf-8") as f:
            f.write(f"{c1}\n{c2}")
        log_action(self.username, "Файл input.txt зашифрованний и збережений в close.txt")

    def decrypt_close_to_out(self):
        """Розшифрування тексту из close.txt і запис в out.txt."""
        if os.path.exists("data/close.txt"):
            with open("data/close.txt", "r", encoding="utf-8") as f:
                c1 = int(f.readline().strip())
                c2 = int(f.readline().strip())
            plaintext_int = decrypt_text(p, private_key, c1, c2)  # Розшифровка чисел
            plaintext = int_to_text(plaintext_int)  # Конвертація числа в текст
            with open("data/out.txt", "w", encoding="utf-8") as f:
                f.write(plaintext)
            log_action(self.username, "Файл close.txt розшифрований і збережений в out.txt")

    def save_file(self, file_path, text_widget):
        """Зберігає зміни у файлі."""
        content = text_widget.get("1.0", tk.END).strip()
        if file_path == "data/input.txt":
            # Шифруємо текст і записуємо в close.txt
            self.encrypt_input_to_close(content)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            log_action(self.username, f"Збережено зміни у файлі: {file_path}")
            messagebox.showinfo("Успіх", "Зміни збережено!")

    def create_text_widget(self, content, editable=False, save_path=None):
        """Створює текстовий віджет з вказаним змістом."""
        text_widget = tk.Text(self, wrap=tk.WORD)
        text_widget.insert(tk.END, content)
        if not editable:
            text_widget.configure(state="disabled")
        text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        if editable:
            text_widget.configure(state="normal")
            save_button = tk.Button(self, text="Зберегти", command=lambda: self.save_file(save_path, text_widget))
            save_button.pack(pady=10)

        close_button = tk.Button(self, text="Закрити", command=self.destroy)
        close_button.pack(pady=10)
