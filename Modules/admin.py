import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os


# Клас вікна адміна
class Admin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

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
        button_resource = tk.Button(self, text="Відкрити Ресурс", **ButtonConfig)
        button_resource.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        button_register = tk.Button(self, text="Зареєструвати Нового Користувача", **ButtonConfig)
        button_register.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        button_log = tk.Button(self, text="Переглянути Журнал Подій", **ButtonConfig)
        button_log.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        button_users = tk.Button(self, text="Усі Користувачі", **ButtonConfig)
        button_users.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Кнопка для повернення
        #button_back = tk.Button(self, text="Назад", **ButtonConfig,
                                #command=self.open_previous_window)
        #button_back.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    #def open_previous_window(self):
    #from main import AuthorizeWindow
        #switch_window(self.master, AuthorizeWindow)
