# PROGRAM Point-Init-Default:

class Point:
    
    def __init__(self,x=0,y=0):
        self.move(x,y)
    # END Init

    
    def move(self,a,b):
        self.x = a
        self.y = b
    # END Reset

    def reset(self):
        self.move(0,0)
    # END Reset

# END Class

p1 = Point()
p2 = Point(4,6)

print("P1-x, P1-y is: ", p1.x, p1.y);
print("P2-x, P2-y is: ", p2.x, p2.y);

p1.reset()
p2.reset()

print(" ### RESETTING ### ")
print("P1-x, P1-y is: ", p1.x, p1.y);
print("P2-x, P2-y is: ", p2.x, p2.y);

# END.
