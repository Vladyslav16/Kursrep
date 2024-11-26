import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os


class User(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Вікно користувача", **LabelConfig)
        label.pack(pady=20)

        button_back = tk.Button(self, text="Назад", **ButtonConfig,
                                command=self.open_previous_window)
        button_back.pack()


    def open_previous_window(self):
        return switch_window(Admin)