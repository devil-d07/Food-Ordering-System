import tkinter as tk
from modules.menu import Menu
from modules.cart import cart

class MenuUI:
    def __init__(self, root):
        self.root = root
        self.menu = Menu()

        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        # ===== Top Bar =====
        top = tk.Frame(self.frame)
        top.pack(fill="x", pady=10)

        tk.Button(
            top,
            text="⬅ Back",
            command=self.go_back,
            bg="#444",
            fg="white",
            padx=10
        ).pack(side="left", padx=10)

        tk.Label(
            top,
            text="Menu",
            font=("Arial", 20)
        ).pack(side="left", padx=20)

        # ===== Menu Items =====
        for item in self.menu.get_items():
            item_frame = tk.Frame(self.frame, bd=1, relief="solid", padx=10, pady=5)
            item_frame.pack(pady=5, padx=20, fill="x")

            tk.Label(
                item_frame,
                text=f"{item['name']} - ₹{item['price']}",
                font=("Arial", 12)
            ).pack(side="left")

            tk.Button(
                item_frame,
                text="Add to Cart",
                command=lambda i=item: cart.add(i.copy()),
                bg="#28a745",
                fg="white"
            ).pack(side="right")

    def go_back(self):
        # 🔥 Import here to avoid circular import
        from ui.dashboard_ui import DashboardUI
        
        self.frame.destroy()
        DashboardUI(self.root)



    
        