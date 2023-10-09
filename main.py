class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'

    def __lt__(self, other):
        distance_self = self.x ** 2 + self.y ** 2
        distance_other = other.x ** 2 + other.y ** 2

        return distance_self > distance_other

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Point(new_x, new_y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

if __name__ == '__main__':
    point_1 = Point(1, 2)
    point_2 = Point(3, 4)

    # using magic methods
    # string representation
    print(point_1)
    print(point_2)

    # debugging
    print(repr(point_1))
    print(repr(point_2))

    # less than comparison
    print(point_1 > point_2)

    # adding two points
    print(point_1 + point_2)

    # checking equality
    print(point_1 == point_2)
