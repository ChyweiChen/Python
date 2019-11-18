# PROGRAM Stacks as Linked Lists:

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

def CreateEmptyList():
    global HeadNode
    HeadNode = None
# END CreateEmptyList.

##################################

def DeleteAList():
    global HeadNode
    HeadNode = None
# END DeleteAList.

##################################

def ListIsEmpty():
    global HeadNode
    return HeadNode == None
# END ListIsEmpty.

##################################

########## PRINT WITH LOOP ##########

def PrintNodesWithLoop():
    global HeadNode
    Current = HeadNode
    if (Current != None):
    # THEN
        while (Current.pointer != None):
        # DO
            print(Current.value)
            Current = Current.pointer
        # ENDWHILE;
        print(Current.value)
    else:
        print("Empty list")
    # ENDIF;
# END PrintNodesWithLoop.

PrintNodesWithLoop()

########## PRINT AND COUNT ##########

def PrintNodesWithLoopAndCount():
    global HeadNode
    Current = HeadNode
    CountNodes = 0
    if (Current != None):
    # THEN
        while (Current.pointer != None):
            # DO
            print(Current.value)
            Current = Current.pointer
            CountNodes = CountNodes + 1
        # ENDWHILE;

        # Print out and count for last node
        CountNodes = CountNodes + 1
        print(Current.value)
    
        print("Count:", CountNodes)
    else:
        print("Empty list")
    # ENDIF;
# END PrintNodesWithLoopAndCount.

PrintNodesWithLoopAndCount()

##################################

def FindANode(N):
    global HeadNode
    Current = HeadNode
    while ((Current.pointer != None) and (Current.value != N)):
    # DO
        Current = Current.pointer
    # ENDWHILE;

    # Print out and count for last node
    if (Current.pointer == None):
    # THEN
        print(N, "is not in the list")
    else:
        print("Found value:", Current.value)
    # ENDIF; 
# END FindANode.
FindANode(33337)

##################################

def InsertANode(Pos, N):
    global HeadNode
    Current = HeadNode

    nodeX = ListNode(N, None)

    PositionCounter = 1
    CountNodes = 0
    if Pos == 0:
    # THEN
        HeadNode = nodeX
        nodeX.pointer = Current
    else:
        while (Pos > PositionCounter):
            # DO
            Current = Current.pointer
            PositionCounter = PositionCounter + 1
        # ENDWHILE;

        nodeX.pointer = Current.pointer
        Current.pointer = nodeX
    # ENDIF;
# END InsertANode.
InsertANode(2, 12345)       
PrintNodesWithLoopAndCount()

##################################

def DeleteANode(N):
    global HeadNode
    Previous = None
    Current = HeadNode
    if Current.value == N:
    # THEN
        HeadNode = Current.pointer
    else:
        while ((Current.pointer != None) and (Current.value != N)):
        # DO
            Previous = Current
            Current = Current.pointer
        # ENDWHILE;
        Previous.pointer = Current.pointer
    # ENDIF;
# END DeleteANode.

DeleteANode(12345)
PrintNodesWithLoopAndCount()
    
#################################
########## S T A C K S ##########
#################################

PrintNodesWithLoopAndCount()
StackTop = HeadNode;
PrintNodesWithLoopAndCount()

##################################

def CreateEmptyStack():
    global StackTop
    StackTop = None
# END CreateEmptyStack.

CreateEmptyStack()

##################################

def StackIsEmpty():
    global StackTop
    return StackTop == None
# END StackIsEmpty.

##################################

def PrintStack():
    global StackTop
    SPrint = StackTop
    print("Printing Stack...")
    while(SPrint != None):
    # DO
        print(SPrint.value)
        SPrint = SPrint.pointer
    # ENDWHILE;
    print("* End of Stack *")
# END QueueIsEmpty.

##################################

def StackPush(N):
    global StackTop
    nodeX = ListNode(N, None)
    if StackIsEmpty():
    # THEN
        StackTop = nodeX
    else:
        nodeX.pointer = StackTop
        StackTop = nodeX
    # ENDIF;
# END StackPush.

StackPush(35)
StackPush(34)
StackPush(33)
StackPush(32)
PrintStack()

##################################

def StackPop():
    global StackTop
    if StackIsEmpty():
    # THEN
        print("Stack is empty")
        N = 0
    else:
        N = StackTop.value
        StackTop = StackTop.pointer
    # ENDIF;
    return N
# END StackPop.

PopValue = StackPop()
print("Pop value:", PopValue)
PrintStack()
##################################

def ShowStackTop():
    global StackTop
    if StackIsEmpty():
    # THEN
        print("Stack is empty")
        N = 0
    else:
        N = StackTop.value
        print("Top value:", StackTop.value)
    # ENDIF;
    return N
# END ShowStackTop.

TopValue = ShowStackTop()
PrintStack()
##################################
