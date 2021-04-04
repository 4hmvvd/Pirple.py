#While loop
"""
The syntax of a "while" loop is 
while (condition):
    Action1
    Action2
    Action3
    ...
"""

counter = 1

while (counter<= 10):
    print(counter)
    counter = counter + 1
    

#Summation of numbers through counter

counter = 1
Sum = 0

while (counter<= 100):
    #print(counter)
    Sum = Sum + counter
    counter = counter + 1

print(Sum)


#Using "while" loop and indexing a list

Letters = ["a", "b", "c", "d", "e"]

Index = 0

while (Index < len(Letters)):
    print(Letters[Index])
    print(Index)
    Index = Index + 1

#Using while loop to calculate the time it takes for an object to hit ground

height = 500
velocity = 50
time = 0

while (height > 0):
    height = height - velocity
    time = time + 1

print(height)
print(time)

""" For more accuracy, the values of the velocity and the addition
of step (1) are reduced into decimals below zero or closer to zero.
"""
