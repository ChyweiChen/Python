import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
# END distance

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    # ENDFOR
    print(perimeter)
# END perimeter


square = [(1,1),(1,2),(2,2),(2,1)]
perimeter(square)
square2 = [(1,1),(1,4),(4,4),(4,1)]
perimeter(square2)
