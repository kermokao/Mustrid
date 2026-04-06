class Square:
    def __init__(self, side=0):
        self.side = side

    def calculate_area(rc):
        return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square
        self.width = square.side
        self.height = square.side

def calculate_area(rc):
    return rc.width * rc.height

sq = Square(5)
adapter = SquareToRectangleAdapter(sq)

print(calculate_area(adapter))
