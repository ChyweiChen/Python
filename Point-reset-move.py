# PROGRAM Point-Reset-Move:

class Point:
    
    def move(self,a,b):
        self.x = a
        self.y = b
    # END Reset

    def reset(self):
        self.move(0,0)
    # END Reset

# END Class

p = Point()
p.x = 5
p.y = 4
print("P-x, P-y is: ", p.x, p.y);

p.reset()
print(" ### RESETTING ### ")
print("P-x, P-y is: ", p.x, p.y);

# END.
