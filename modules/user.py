from modules.database import Database

class User:
    def __init__(self):
        self.db = Database('data/users.json')

    def register(self, username, password):
        users = self.db.read()
        if any(u['username']==username for u in users):
            return False
        users.append({'username': username, 'password': password})
        self.db.write(users)
        return True

    def login(self, username, password):
        return any(u['username']==username and u['password']==password for u in self.db.read())
    
