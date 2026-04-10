import tkinter as tk
from ui.login_ui import LoginUI

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Food Ordering System")
        self.geometry("1000x650")
        self.configure(bg="#1e1e2f")
        self.resizable(False, False)
        LoginUI(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
    