import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # END init
    
    def distance(self, p2):
        return math.sqrt(
            (self.x - p2.x)**2 + (self.y - p2.y)**2)
    # END distance

# END class point


class Polygon:
    def __init__(self):
        self.vertices = []
    # END init

    def add_point(self, point):
        self.vertices.append((point))
    # END add_point

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        # ENDFOR
        return perimeter
    # END perimeter

# END class perimeter

square = Polygon()

square.add_point(Point(1,1))
square.add_point(Point(1,2))
square.add_point(Point(2,2))
square.add_point(Point(2,1))

print("The polygon perimeter is", square.perimeter())

