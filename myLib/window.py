import sys

Config = {
  'active background': "light gray",
  'font': ("Times New Roman", 16),
  'bg': "white",
  'fg': "black"
}


def win_to_center(parent, window_width, window_height):
    """
    Центрує вікно на екрані.
    """
    parent.update_idletasks()
    x = (parent.winfo_screenwidth() - window_width) // 2
    y = (parent.winfo_screenheight() - window_height) // 2 - 40
    parent.geometry(f"{window_width}x{window_height}+{x}+{y}")
    parent.resizable(False, False)


def return_to_previous(current_window, previous_window_func):
    """
    Закриває поточне вікно та відкриває попереднє.
    """
    current_window.destroy()  # Закриває поточне вікно
    previous_window_func()  # Викликає функцію для відкриття попереднього вікна