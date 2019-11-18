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


##################################################
# Set Comprehensions
##################################################

from collections import namedtuple
Book = namedtuple("Book", "author title genre")
books = [
        Book("Pratchett", "Nightwatch", "fantasy"),
        Book("Pratchett", "Thief Of Time", "fantasy"),
        Book("Le Guin", "The Dispossessed", "scifi"),
        Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
        Book("Turner", "The Thief", "fantasy"),
        Book("Phillips", "Preston Diamond", "western"),
        Book("Phillips", "Twice Upon A Time", "scifi"),
        ]

fantasy_authors = {b.author for b in books if b.genre == 'fantasy'}
print(fantasy_authors)

##################################################
# Dictionary Comprehensions
##################################################

from collections import namedtuple
Book = namedtuple("Book", "author title genre")
books = [
        Book("Pratchett", "Nightwatch", "fantasy"),
        Book("Pratchett", "Thief Of Time", "fantasy"),
        Book("Le Guin", "The Dispossessed", "scifi"),
        Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
        Book("Turner", "The Thief", "fantasy"),
        Book("Phillips", "Preston Diamond", "western"),
        Book("Phillips", "Twice Upon A Time", "scifi"),
        ]

fantasy_titles = {b.title: b for b in books if b.genre == 'fantasy'}
print(" ")
print(fantasy_titles)
