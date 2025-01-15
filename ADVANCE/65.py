class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
   
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

point1 = Point(2, 3)
point2 = Point(4, 5)

point3 = point1 + point2
print(point3)  
