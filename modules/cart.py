class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        for i in self.items:
            if i['name']==item['name']:
                i['qty'] += 1
                return
        item['qty'] = 1
        self.items.append(item)

    def remove(self, item_name):
        self.items = [i for i in self.items if i['name']!=item_name]

    def total(self):
        return sum(i['price']*i['qty'] for i in self.items)

    def clear(self):
        self.items = []

cart = Cart()