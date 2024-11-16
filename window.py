import sys

Config = {
  'active background': "light gray",
  'font': ("Times New Roman", 16),
  'bg': "white",
  'fg': "black"
}


def win_to_center(parent, window_width, window_height):
    parent.update_idletasks()
    x = (parent.winfo_screenwidth() - window_width) // 2
    y = (parent.winfo_screenheight() - window_height) // 2 - 40
    parent.geometry(f"{window_width}x{window_height}+{x}+{y}")
    parent.resizable(False,False)