# PROGRAM Linked Lists:

####### DECLARE LINKED LIST #######

class ListNode:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer
# END ListNode.

nodeD = ListNode(31, None)
nodeC = ListNode(37, nodeD)
nodeB = ListNode(62, nodeC)
nodeA = ListNode(23, nodeB)

HeadNode = nodeA

##################################

########## SIMPLE PRINT ##########
def PrintNodes():
    print("[", nodeA.value, "] -> [",nodeB.value, "] -> [",nodeC.value, "] -> [",nodeD.value, "] -> NULL")
# END PrintNodes.
PrintNodes()

##################################
Current = HeadNode
def RecursiveCount(Current):
    if Current == None:
    # THEN
        return 0
    else:
        return 1 + RecursiveCount(Current.pointer)
    # ENDIF;
# END RecursiveCount.

print("Recursive Count:", RecursiveCount(HeadNode))

##################################
Current = HeadNode
def RecursivePrint(Current):
    if Current == None:
    # THEN
        return
    else:
        print(Current.value)
        RecursivePrint(Current.pointer)
    # ENDIF;
# END RecursiveCount.

RecursivePrint(Current)

##################################

Current = HeadNode
def RecursivePrettyPrint(Current):
    if Current == None:
    # THEN
        print("  NULL")
        return
    else:
        print("[", Current.value, "]")
        print("   |")
        print("   V")
        RecursivePrettyPrint(Current.pointer)
    # ENDIF;
# END RecursivePrettyCount.
RecursivePrettyPrint(Current)

##################################

Current = HeadNode
def FindANode(Current, N):
    if (Current.pointer == None):
    # THEN
        return None
    elif (Current.value == N):
    # THEN
        print(N, "was found")
        return N
    else:
        return FindANode(Current.pointer, N)
    # ENDIF; 
# END FindANode.
FindANode(Current, 37)

##################################

print("------------")
Current = HeadNode
def InsertANode(Current, Pos, N):
    if (Current.pointer == None):
    # THEN
        return None
    elif (Current.value == Pos):
    # THEN
        nodeX = ListNode(N, None)
        nodeX.pointer = Current.pointer
        Current.pointer = nodeX
        return N
    else:
        return InsertANode(Current.pointer, Pos, N)
    # ENDIF; 
# END. InsertANode.
RetValue = InsertANode(Current, 37, 12345)       
RecursivePrint(Current)

##################################

Current = HeadNode
def DeleteANode(Current, N):
    if (Current != None):
        # THEN
        if (Current.value == N):
        # THEN
            Current = Current.pointer
        else:
            Current.pointer = DeleteANode(Current.pointer, N)
        # ENDIF;
    # ENDIF;
    return Current

# END DeleteANode.
RetValue = DeleteANode(Current, 12345)
RecursivePrint(Current)
    
##################################
