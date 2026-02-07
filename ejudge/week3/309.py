import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == "__main__":
    r = int(input())
    circle = Circle(r)
    area = circle.area()
    print(f"{area:.2f}")
