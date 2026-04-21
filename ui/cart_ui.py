# =========================
# ui/cart_ui.py
# =========================
import tkinter as tk
from modules.cart import cart
from modules.order import Order

class CartUI:
    def __init__(self, root):
        self.root = root
        self.order = Order()

        self.frame = tk.Frame(root, bg="#0f172a")
        self.frame.pack(fill="both", expand=True)

        # ===== Top Bar =====
        top = tk.Frame(self.frame, bg="#1e293b")
        top.pack(fill="x")

        tk.Button(
            top,
            text="⬅ Back",
            command=self.go_back,
            bg="#334155",
            fg="white",
            padx=10
        ).pack(side="left", padx=10, pady=10)

        tk.Label(
            top,
            text="Your Cart",
            fg="white",
            bg="#1e293b",
            font=("Arial", 18, "bold")
        ).pack(side="left", padx=20)

        # ===== Cart Content =====
        self.content = tk.Frame(self.frame, bg="#0f172a")
        self.content.pack(fill="both", expand=True)

        self.display()

    def display(self):
        # Clear old content
        for widget in self.content.winfo_children():
            widget.destroy()

        if not cart.items:
            tk.Label(
                self.content,
                text="Cart is empty 🛒",
                fg="white",
                bg="#0f172a",
                font=("Arial", 14)
            ).pack(pady=50)
            return

        for item in cart.items:
            f = tk.Frame(self.content, bg="#1e293b")
            f.pack(pady=5, padx=20, fill="x")

            tk.Label(
                f,
                text=f"{item['name']} x {item['qty']}",
                fg="white",
                bg="#1e293b"
            ).pack(side="left", padx=10)

            tk.Button(
                f,
                text="Remove",
                command=lambda n=item['name']: self.remove(n),
                bg="#ef4444",
                fg="white"
            ).pack(side="right", padx=10)

        tk.Label(
            self.content,
            text=f"Total: ₹{cart.total()}",
            fg="#22c55e",
            bg="#0f172a",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        tk.Button(
            self.content,
            text="Checkout",
            command=self.checkout,
            bg="#22c55e",
            fg="white",
            padx=20
        ).pack()

    def remove(self, name):
        cart.remove(name)
        self.display()

    def checkout(self):
        self.order.place(cart.items, cart.total())
        cart.clear()
        self.display()

    def go_back(self):
        # ✅ Import inside function (avoid circular import)
        from ui.dashboard_ui import DashboardUI

        self.frame.destroy()
        DashboardUI(self.root)