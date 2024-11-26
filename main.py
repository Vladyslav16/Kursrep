import tkinter as tk
from myLib.window import *
from tkinter import messagebox
import os
from Modules.authorize import AuthorizeWindow


# Запуск програми
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Program")
    win_to_center(root, 660, 330)
    # Налаштування головного контейнера
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    # Запуск головного екрану
    main_screen = AuthorizeWindow(root)
    main_screen.grid(row=0, column=0, sticky="nsew")

    root.mainloop()

