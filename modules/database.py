import json, os

class Database:
    def __init__(self, path):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump([], f)

    def read(self):
        with open(self.path, 'r') as f:
            return json.load(f)

    def write(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)
