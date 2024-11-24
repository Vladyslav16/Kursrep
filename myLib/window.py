# Конфігурації для різних елементів GUI
ButtonConfig = {
    'font': ("Times New Roman", 14, "bold"),
    'bg': "lightblue",
    'fg': "black",
    'activebackground': "blue",
    'activeforeground': "white",
}

EntryConfig = {
    'font': ("Arial", 12),
    'bg': "white",
    'fg': "black",
    'highlightbackground': "gray",
    'highlightthickness': 1,
}

LabelConfig = {
    'font': ("Verdana", 12),
    'bg': "lightgray",
    'fg': "black",
}


def win_to_center(parent, window_width, window_height):
    """
    Центрує вікно на екрані.
    """
    parent.update_idletasks()
    x = (parent.winfo_screenwidth() - window_width) // 2
    y = (parent.winfo_screenheight() - window_height) // 2 - 20
    parent.geometry(f"{window_width}x{window_height}+{x}+{y}")
    parent.resizable(False, False)


def return_to_previous(current_window, previous_window_func):
    """
    Закриває поточне вікно та відкриває попереднє.
    """
    current_window.destroy()
    previous_window_func()