class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class Product:
    
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:

    def filter_by_color(self, products, color):
        return [p for p in products if p.color == color]

    def filter_by_size(self, products, size):
        return [p for p in products if p.size == size]

    def filter_by_size_and_color(self, products, size, color):
        return [p for p in products if p.color == color and p.size == size]
