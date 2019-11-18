############################################
#  Iterable
############################################

class MyCountIterable:
    
    def __init__(self, Value):
        self.Value = Value
    # END Init

    def __iter__(self):
        return MyCountIteration(self.Value)
    # END Iter

# END MyCountIterable.


############################################
#  Iteration
############################################

class MyCountIteration:

    def __init__(self, Value):
        self.Index = 0
        self.Value = Value
    # END Init

    def __iter__(self):
        # Iterators are iterables too.
        # Adding this functions to make them so.
        return self
    # END Iter

    def __next__(self):
        if self.Index < self.Value:
            # THEN
            Index = self.Index
            self.Index = self.Index + 1
            return Index
        else:
            raise StopIteration()
        # ENDIF;
    # END Next

# END MyCountIteration.



############################################
#  Program Execution
############################################

FirstCount = MyCountIterable(5)
list(FirstCount)
FirstCountIter = iter(FirstCount)

while True:
# DO
    try:
        print(next(FirstCountIter))
    except StopIteration:
	    break
# ENDWHILE
