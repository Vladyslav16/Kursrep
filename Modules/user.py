import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os


# Клас вікна користувача
class User(tk.Frame):
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

        tk.Label(self, text="Вікно користувача:", **LabelConfig).grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        # Кнопки користувацького вікна
        button_open_resource = tk.Button(self, text="Відкрити ресурс", **ButtonConfig)
        button_open_resource.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Кнопка для повернення
        #button_exit = tk.Button(self, text="Вийти", **ButtonConfig,
                                #command=self.open_previous_window)
        #button_exit.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    #def open_previous_window(self):
        #from main import AuthorizeWindow
        #switch_window(self.master, AuthorizeWindow)