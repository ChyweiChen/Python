# PROGRAM Point-Reset-Move:

import math

class Point:
    
    def move(self,a,b):
        self.x = a
        self.y = b
    # END Reset

    def reset(self):
        self.move(0,0)
    # END Reset

    def calc_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2)
    # END calc_distance

# END Class

p1 = Point()
p2 = Point()

p1.move(2,2)
p2.move(6,5)

print("P1-x, P1-y is: ", p1.x, p1.y)
print("P2-x, P2-y is: ", p2.x, p2.y)
print("Distance from P1 to P2 is:", p1.calc_distance(p2))

# END.
