import tkinter as tk

class WindowManager:
    def __init__(self):
        # self.master = root
        self.window_stack = []

    def push_window(self, window):
        if self.window_stack:
            self.window_stack[-1].withdraw()
        self.window_stack.append(window)
        window.deiconify()

    def pop_window(self):
        if self.window_stack:
            current_window = self.window_stack.pop()
            current_window.destroy()
        if self.window_stack:
            self.window_stack[-1].deiconify()

class StartingMenu(tk.Toplevel):
    def __init__(self, master, manager):
        super().__init__(master)
        self.manager = manager
        self.title("Starting Menu")

        login_button = tk.Button(self, text="Login", command=self.open_login)
        login_button.pack()

    def open_login(self):
        self.manager.push_window(Login(self, self.manager))

class Login(tk.Toplevel):
    def __init__(self, master, manager):
        super().__init__(master)
        self.manager = manager
        self.title("Login")

        back_button = tk.Button(self, text="Back", command=self.go_back)
        back_button.pack()

    def go_back(self):
        self.manager.pop_window()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window as we'll manage everything via Toplevels
    manager = WindowManager()
    starting_menu = StartingMenu(root, manager)
    manager.push_window(starting_menu)
    root.mainloop()

if __name__ == "__main__":
    main()
