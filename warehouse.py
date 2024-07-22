import random
import json


class Warehouse:

    '''общий класс с работой с продукатми на складе'''

    TOTAL = 0

    def __init__(self, ware_house, basket):
        self.ware_house = ware_house
        self.basket = basket

    def load(self):
        file = self.ware_house + '.json'
        with open(file, 'r') as read:
            array = json.load(read)
        return array

    def add_product(self, product, count, price):

        '''добавляет продукт на склад'''

        file = self.ware_house + '.json'
        new_product = {product: {'количество': count, 'цена': price}}
        array = self.load()
        array.update(new_product)
        with open(file, 'w') as add:
            json.dump(array, add)

    def warehouse_info(self):

        '''показывает обстановку на складе'''

        array = self.load()
        print([a for a in array.items()])

    def delete_product(self, product):

        '''удаление товара со склада'''

        file = self.ware_house + '.json'
        array = self.load()
        if product in array:
            del array[product]
            with open(file, 'w') as delete:
                json.dump(array, delete)
        else:
            raise ValueError('такого продукта нет на складе')

    def counter(self, product, count):

        '''меняет количество товаров на складе'''
        if product not in self.load():
            raise ValueError('такого продукта нет')
        array = self.load()
        new_count = array[product]['количество']
        file = self.ware_house + '.json'

        if count == 0:
            raise ValueError('число должно быть больше нуля')

        elif new_count + count < 0:
            array[product]['количество'] = 0

        else:
            new_count = array[product]['количество']
            array[product]['количество'] = new_count+count

        with open(file, 'w') as ct:
            json.dump(array, ct)

    def pricer(self, product, price):

        '''меняет цену товаров на складе'''
        if product not in self.load():
            raise ValueError('такого продукта нет')
        array = self.load()
        new_price = array[product]['цена']
        file = self.ware_house + '.json'

        if price == 0 or new_price + price < 0:
            array[product]['цена'] = 'бесплатно'

        else:
            new_price = array[product]['цена']
            array[product]['цена'] = new_price + price

        with open(file, 'w') as pt:
            json.dump(array, pt)

    @staticmethod
    def add_id():

        '''создает номер заказа и файл'''

        a = 1
        b = 100
        num = random.randint(a, b)
        ii = 'order ' + str(num) + '.txt'
        with open(ii, 'w'):
            print(f'ORDER ID: {num}')

    @classmethod
    def total_price(cls, file, product, count):

        '''считает общую цену'''

        with open(file, 'r') as read:
            array = json.load(read)

        price = array[product]['цена'] * count
        cls.TOTAL += price
        return cls.TOTAL

    @classmethod
    def total(cls, order_id):
        o_id = 'order ' + str(order_id) + '.txt'

        with open(o_id, 'r') as read:
            add_total = read.read()

        add_total += f'TOTAL: {str(cls.TOTAL)}'

        with open(o_id, 'w') as write:
            write.write(add_total)

    def order_product(self, order_id, product, count):

        '''составляет заказ и кладет продукты в корзину (убирая купленное со склада)'''

        array = self.load()
        new_count =- count
        self.counter(product, new_count)
        file_name = self.ware_house + '.json'

        if count <= 0:
            raise ValueError('количество продуктов должно быть больше нуля')
        elif product not in array:
            raise ValueError('такого продукта нет на складе')
        elif array[product]['количество'] == 0 or array[product]['количество'] - new_count < 0:
            raise ValueError('товар кончился, или попробуйте взять меньше товара. Товара осталось: ', array[product]['количество'])

        o_id = 'order ' + str(order_id) + '.txt'
        price = array[product]['цена'] * count
        basket = (f'Product: {product} \nCount: {count} \nPrice: {price}\n \n')

        with open(o_id, 'r') as read:
            all = read.read()

        all += basket

        with open(o_id, 'w') as write:
            write.write(all)
            self.total_price(file_name, product, count)