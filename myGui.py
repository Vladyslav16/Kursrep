import tkinter as tk
from tkinter import messagebox


# Функція для входу
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":  # Проста перевірка
        messagebox.showinfo("Успіх", "Успішний вхід!")
    else:
        messagebox.showerror("Помилка", "Неправильне ім'я користувача або пароль.")


# Головне вікно
root = tk.Tk()
root.title("Система ідентифікації")

# Поля вводу
tk.Label(root, text="Ім'я користувача:").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Пароль:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Кнопка входу
login_button = tk.Button(root, text="Увійти", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Запуск програми
root.mainloop()
