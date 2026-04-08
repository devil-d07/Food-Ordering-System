import tkinter as tk
from modules.cart import cart
from modules.order import Order

class CartUI:
    def __init__(self, root):
        self.root = root
        self.order = Order()

        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Cart", font=("Arial", 20)).pack(pady=10)

        self.display()

    def display(self):
        for widget in self.frame.winfo_children()[1:]:
            widget.destroy()

        for item in cart.items:
            f = tk.Frame(self.frame)
            f.pack()
            tk.Label(f, text=f"{item['name']} x {item['qty']}").pack(side="left")
            tk.Button(f, text="Remove", command=lambda n=item['name']: self.remove(n)).pack(side="right")

        tk.Label(self.frame, text=f"Total: ₹{cart.total()}").pack(pady=10)
        tk.Button(self.frame, text="Checkout", command=self.checkout).pack()

    def remove(self, name):
        cart.remove(name)
        self.display()

    def checkout(self):
        self.order.place(cart.items, cart.total())
        cart.clear()
        self.display()
        