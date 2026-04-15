class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def set_width(self, width: float):
        self.width = width

    def set_height(self, height: float):
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    def set_width(self, width: float):
        self.width = width
        self.height = width 

    def set_height(self, height: float):
        self.width = height
        self.height = height

def print_area(rect: Rectangle):
    rect.set_width(5)
    rect.set_height(10)
    print(f"Площадь: {rect.area()}")  

print_area(Rectangle(2, 3)) 

print_area(Square(2))   