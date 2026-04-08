from modules.database import Database
from datetime import datetime

class Order:
    def __init__(self):
        self.db = Database('data/orders.json')

    def place(self, items, total):
        data = self.db.read()
        data.append({
            'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'items': items,
            'total': total
        })
        self.db.write(data)

    def history(self):
        return self.db.read()
        