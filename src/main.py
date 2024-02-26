class Category:
    """Класс категории"""
    name: str
    description: str
    product: list
    total_numbers_of_category = 0
    unique_products = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        Category.total_numbers_of_category += 1
        Category.unique_products += 1


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

