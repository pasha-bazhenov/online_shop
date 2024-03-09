class Category:
    """Класс категории"""
    name: str
    description: str
    goods: list
    total_numbers_of_category = 0
    unique_products = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods
        Category.total_numbers_of_category += 1
        Category.unique_products += 1

    @property
    def goods(self):
        """Получение приватного атрибута __products"""
        return self.__goods

    def add_goods(self, product):
        """Добавление данных с приватного атрибута __products"""
        self.__goods.append(product)

    @property
    def get_goods(self):
        """Получение имени, цены и остатка"""
        current_list = []
        for product in self.__goods:
            current_list.append(f'{str(product.name)}, {product.price} руб. Остаток: {product.quantity} шт.')
        return current_list

    def __repr__(self):
        return f'Category({self.name}, {self.description}, {self.__goods})'




class Product:
    """Класс продукт"""
    name: str
    description: str
    price: float
    quantity_in_lock: int

    def __init__(self, name, description, price, quantity_in_lock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_lock = quantity_in_lock

    @property
    def price(self):
        """Получение приватных данных через гетер"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Условия изменения цены"""
        if new_price <= 0:
            print('Цена введена некоректно')
        elif new_price < self.__price:
            user_answer = input('Цена понизилась. Установить эту цену? (y - да, n - нет)')
            if user_answer == 'y':
                self.__price = new_price
            else:
                print('Цена осталась прежней')
        else:
            self.__price = new_price

    def get_product_price(self):
        """Получение приватного атрибута price"""
        return self.price

    def __repr__(self):
        return f'Product({self.name}, {self.description}, {self.price}, {self.quantity_in_lock})'

    @classmethod
    def add_new_product(cls, product_data, list_of_products=None):
        # забираем данные в переменные для удобства работы
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        # если передан и словарь и список продуктов - попытаться найти в списке продуктов продукт схожий по имени
        if list_of_products:
            for product in list_of_products:
                if product.name == name:  # если перебираемый продукт по имени равен тому имени продукта, который
                    # предлагается создать
                    # здесь мы нашли продукт, вернем его, сначала установив количество и цену
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    # установив атрибуты у продукта - возвращаем его
                    return product

        # здесь мы окажемся в двух случаях: если не передан список продуктов, либо он был передан но в цикле не нашлось
        # совпадения по имени - значит мы должны создать продукт и вернуть его
        new_product = cls(name, description, price, quantity)
        return new_product
