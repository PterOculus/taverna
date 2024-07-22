import random
import uuid

class Product:
    def __init__(self, id, name, count, price):
        self.id = id
        self.name = name
        self.count = count
        self.price = price

class Repository:
    def __init__(self, path):
        pass

    def read(self):
        # check file existance and create if needed
        # todo read file and parse it
        return []
    
    def save(self, products):
        # todo save to file in csv
        pass

class Service:
    products = []

    def __init__(self, repo):
        self.repository = repo
        self.products = self.repository.read()

    def get_all(self):
        return self.products

    def get_by_id(self, id):
        # find product by id
        for p in self.products:
            if p.id == id:
                return p
        return None
    
    def add(self, name, count, price):
        # todo check strings length
        self.products.append(Product(self._generateId(), name, count, price))
        self.repository.save(products)

    def update(self, product: Product):
        p = self.get_by_id(product.id)
        if (p == None):
            raise Exception("Product not found")
        # todo update staff
        self.repository.save(self.products)

    def delete(self, id):
        # todo like update but delete from array
        pass

    def _generateId(self):
        return uuid.uuid4()

if __name__ == '__main__':
    service = Service(Repository('./path'))

    print("l - show all items")
    print("d - delete item")
    print("q - quit")

    while True:
        cmd = input("Command: ")
        try:
            if (cmd == "1"):
                print([i.name for i in self.service.get_all()])
            elif (cmd == "2"):
                name = input("name: ")
                count = input("count: ")
                price = input("price: ")
                self.service.add(name, count, price)
            elif (cmd == "q"):
                break
            else:
                print("retard")
        except Exception as e:
            print(f"Failed to perform command: {e}")
    
    print("bye bye")
