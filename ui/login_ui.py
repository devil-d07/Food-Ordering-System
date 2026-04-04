import tkinter as tk
from modules.user import User
from ui.dashboard_ui import DashboardUI

class LoginUI:
    def __init__(self, root):
        self.root = root
        self.user = User()

        self.frame = tk.Frame(root, bg="#1e1e2f")
        self.frame.pack(expand=True)

        tk.Label(self.frame, text="Login", fg="white", bg="#1e1e2f", font=("Arial", 22)).pack(pady=20)

        self.u = tk.Entry(self.frame)
        self.u.pack(pady=5)
        self.p = tk.Entry(self.frame, show="*")
        self.p.pack(pady=5)

        tk.Button(self.frame, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.frame, text="Register", command=self.register).pack()

        self.msg = tk.Label(self.frame, bg="#1e1e2f")
        self.msg.pack()

    def login(self):
        if self.user.login(self.u.get(), self.p.get()):
            self.frame.destroy()
            DashboardUI(self.root)
        else:
            self.msg.config(text="Invalid credentials", fg="red")

    def register(self):
        if self.user.register(self.u.get(), self.p.get()):
            self.msg.config(text="Registered", fg="green")
        else:
            self.msg.config(text="User exists", fg="red")