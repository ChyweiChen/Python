# PROGRAM StdDevVal:

import math

#### Calculate Average ###

Age = [44, 23, 42, 33, 18, 54, 34, 16]
TotalAvg = 0
for index in range(0,len(Age)):
# DO
    TotalAvg = TotalAvg + Age[index]
# ENDFOR;

AverageVal = TotalAvg/len(Age)

#### Calculate Standard Deviation ###

TotalStdDevNum = 0
for index in range(0,len(Age)):
# DO
    StdDevNum = (Age[index] - AverageVal) * (Age[index] - AverageVal)
    TotalStdDevNum = TotalStdDevNum + StdDevNum
# ENDFOR;
print(math.sqrt(TotalStdDevNum/len(Age)-1))
# END.
      
