# PROGRAM Point-Init:

class Point:
    
    def __init__(self,x,y):
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

p = Point(5,4)

print("P-x, P-y is: ", p.x, p.y);

p.reset()
print(" ### RESETTING ### ")
print("P-x, P-y is: ", p.x, p.y);

# END.
