import tkinter as tk
from tkinter import messagebox

from ui_login import UIlogin
from ui_budget import UIbudget


def user_from_text_file():
    with open("user.txt", 'r') as file:
        user = file.readline()

    return user

root = tk.Tk()
ui = UIlogin(root)
ui.open_start_window()
root.mainloop()




user = user_from_text_file()


ui_budget = UIbudget(user)
