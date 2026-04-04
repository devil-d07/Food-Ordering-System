from modules.database import Database

class Menu:
    def __init__(self):
        self.db = Database('data/menu.json')

    def get_items(self):
        return self.db.read()