import tkinter as tk
from tkinter import messagebox
import time
import csv

import tkTools as T

class UIlogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw() #hide the root window (self) all windows will be managed with Toplevels
        manager = WindowManger()
        starting_menu = StartingMenu(self, manager)
        manager.push_window(starting_menu)
        self.mainloop()



class WindowManger:
    def __init__(self):
        self.window_stack = []

    def push_window(self, window):
        if self.window_stack:
            self.window_stack[-1].withdraw()    #-1 refers to the last element in the list
        self.window_stack.append(window)
        window.deiconfiy() #.deiconify make new window visible

    def pop_window(self):
        if self.window_stack:
            current_window = self.window_stack.pop()
            current_window.destroy()
        if self.window_stack:
            self.window_stack[-1].deiconify



class StartingMenu(tk.Toplevel):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager



