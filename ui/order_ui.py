import tkinter as tk
from modules.order import Order

class OrderUI:
    def __init__(self, root):
        self.root = root
        self.order = Order()

        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Order History", font=("Arial", 20)).pack()

        for o in self.order.history():
            tk.Label(self.frame, text=f"{o['date']} - ₹{o['total']}").pack()
            