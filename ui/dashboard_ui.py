import tkinter as tk
from PIL import Image, ImageTk

class DashboardUI:
    def __init__(self, root):
        self.root = root

        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        # ===== Load Background Image =====
        self.bg_image = Image.open("assets/images/foodbackground.jpg")
        self.bg_image = self.bg_image.resize((1100, 650))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self.frame, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # ===== Overlay Frame (for UI on top of image) =====
        overlay = tk.Frame(self.frame, bg="#000000", bd=0)
        overlay.place(relwidth=1, relheight=1)

        overlay.configure(bg="#000000")
        overlay.attributes = {"alpha": 0.6}  # visual effect (optional)

        # ===== Sidebar =====
        sidebar = tk.Frame(overlay, bg="#1e293b", width=200)
        sidebar.pack(side="left", fill="y")

        tk.Label(
            sidebar,
            text="🍔 Food App",
            fg="white",
            bg="#1e293b",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Button(sidebar, text="Menu", command=self.menu,
                  bg="#334155", fg="white", width=20).pack(pady=10)

        tk.Button(sidebar, text="Cart", command=self.cart,
                  bg="#334155", fg="white", width=20).pack(pady=10)

        tk.Button(sidebar, text="Orders", command=self.orders,
                  bg="#334155", fg="white", width=20).pack(pady=10)

        # ===== Main Area =====
        main = tk.Frame(overlay, bg="#000000")
        main.pack(fill="both", expand=True)

        tk.Label(
            main,
            text="Welcome 👋",
            fg="white",
            bg="#000000",
            font=("Arial", 28, "bold")
        ).pack(pady=50)

    def menu(self):
        from ui.menu_ui import MenuUI
        self.frame.destroy()
        MenuUI(self.root)

    def cart(self):
        from ui.cart_ui import CartUI
        self.frame.destroy()
        CartUI(self.root)

    def orders(self):
        from ui.order_ui import OrderUI
        self.frame.destroy()
        OrderUI(self.root)
        










        

        