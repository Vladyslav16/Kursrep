### !Конфігурації для різних елементів GUI! ###
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
### ^Конфігурації для різних елементів GUI^ ###


def tkinter_to_turtle(x_tkinter, y_tkinter, width, height):
    """
    Переводить координати tkinter ---> turtle
    """
    xt0 = width // 2
    yt0 = height // 2
    return x_tkinter - xt0, -(y_tkinter - yt0)


def turtle_to_tkinter(x_turtle, y_turtle, width, height):
    """
    Переводить координати turtle ---> tkinter
    """
    xt0 = width // 2
    yt0 = height // 2
    return x_turtle + xt0, yt0 + y_turtle


def win_to_center(parent, window_width, window_height):
    """
    Центрує вікно на екрані.
    """
    parent.update_idletasks()
    x = (parent.winfo_screenwidth() - window_width) // 2
    y = (parent.winfo_screenheight() - window_height) // 2 - 20
    parent.geometry(f"{window_width}x{window_height}+{x}+{y}")
    parent.resizable(False, False)


def switch_window(current_window, next_window):
    """
    Метод для перемикання вікон.
    """
    for widget in current_window():
        widget.destroy()

    return next_window



