# PROGRAM Point:

class Point:
    
    def reset(self):
        self.x = 0
        self.y = 0
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
