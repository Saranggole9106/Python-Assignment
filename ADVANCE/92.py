class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  

rect = Rectangle(4, 5)
print(f"Rectangle Area: {rect.area()}")

sq = Square(4)
print(f"Square Area: {sq.area()}")
