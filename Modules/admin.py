import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os


class Admin(tk.Frame):
    def __init__(self, master):
        label = tk.Label(self, text="Это главное окно")
        label.pack(pady=20)