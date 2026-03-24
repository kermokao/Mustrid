from enum import Enum

class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *specs):
        self.specs = specs
    
    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.specs)

class NameSpecification(Specification):
    def __init__(self, name):
        self.name = name
    
    def is_satisfied(self, item):
        return self.name == item.name

class BetterFilter:
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

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


products = [
   Product("Apple", Color.GREEN, Size.SMALL),
   Product("Tree", Color.GREEN, Size.LARGE),
   Product("House", Color.BLUE, Size.LARGE)
]

if __name__ == "__main__":

    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    bf = BetterFilter()

    print("Green products:")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large")

    print("Large blue items:")
    large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")
