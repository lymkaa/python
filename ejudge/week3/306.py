class Shape:
    def area(self):
        return 0

class Rec(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

if __name__ == "__main__":
    length, width = map(int, input().split())
    rect = Rec(length, width)
    print(rect.area())
