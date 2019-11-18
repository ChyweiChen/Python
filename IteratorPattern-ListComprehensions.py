##################################################
# Create an Array of Strings
##################################################

string_array = ["234", "75", "331", "73", "5"]
print(string_array)

##################################################
# Convert to an Array of Integers
##################################################

output1 = []

for num in string_array:
    # DO
    output1.append(int(num))
# ENDFOR

print(output1)

##################################################
# Convert to an Array of Integers <Comprehensions>
##################################################

output2 = [int(num) for num in string_array]
print(output2)

##################################################
# Convert to an Array of Integers <Comprehensions (IF)>
##################################################

output3 = [int(n) for n in string_array if len(n) < 3]
print(output3)

##################################################
# Reading a file
##################################################

with open("MyData.txt") as file:
    Lineswithc = [line.strip() for line in file if line.startswith("c")]
print(Lineswithc)
