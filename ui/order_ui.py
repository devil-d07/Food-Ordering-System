# =========================
# ui/order_ui.py
# =========================
import tkinter as tk
from tkinter import ttk
from modules.order import Order

class OrderUI:
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
            text="Order History",
            fg="white",
            bg="#1e293b",
            font=("Arial", 18, "bold")
        ).pack(side="left", padx=20)

        # ===== Scrollable Area =====
        container = tk.Frame(self.frame, bg="#0f172a")
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg="#0f172a", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)

        self.scroll_frame = tk.Frame(canvas, bg="#0f172a")

        # Configure scrolling
        self.scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # ===== Load Orders =====
        self.display_orders()

    def display_orders(self):
        orders = self.order.history()

        if not orders:
            tk.Label(
                self.scroll_frame,
                text="No orders yet 📦",
                fg="white",
                bg="#0f172a",
                font=("Arial", 14)
            ).pack(pady=50)
            return

        for o in orders:
            card = tk.Frame(self.scroll_frame, bg="#1e293b")
            card.pack(pady=10, padx=20, fill="x")

            tk.Label(
                card,
                text=f"Date: {o['date']}",
                fg="#cbd5f5",
                bg="#1e293b"
            ).pack(anchor="w", padx=10, pady=2)

            tk.Label(
                card,
                text=f"Total: ₹{o['total']}",
                fg="#22c55e",
                bg="#1e293b",
                font=("Arial", 12, "bold")
            ).pack(anchor="w", padx=10, pady=2)

    def go_back(self):
        # ✅ Avoid circular import
        from ui.dashboard_ui import DashboardUI

        self.frame.destroy()
        DashboardUI(self.root)