#Loop through a string and list

Word = "Hello"

Letter = []

for w in Word:
    print(w)
    if w == "o":
        print("Getting used to this")

    Letter.append(w)

print(Letter)

for l in Letter:
    print(l)
    
#Loop through numbers

for n in [1,2,3,4,5,6]:
    if n%2 == 0:    #n%2 means the remainder of n / 2. even numbers invariably
        print(n)

    
for m in [1,2,3,4,5,6]:
    if m%2 == 1:    #m%2 means the remainder of m / 2. odd numbers invariably
        print(m)

#Loop through Range
#range(start,stopping,steps)
"""
You must always include the "stopping" value. You might not include the
"starting" and "steps" value, the compiler automatically assumes you starting
from zero(0) and your steps value is one(1).  
"""
        
for num in range(10):
    print(num)

"""
Using "range" to add/ append numbers to an empty list
"""

Numbers = []

for num in range(10):
    Numbers.append(num)

print(Numbers)

OddNumbers = []

for num in range(1,10,2):
    OddNumbers.append(num)

print(OddNumbers)   
