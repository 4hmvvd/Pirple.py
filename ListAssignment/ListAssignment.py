myUniqueList = []
myLeftOvers = []

def add(x):
    global myUniqueList
    if x in myUniqueList:
        addToLeftOvers(x)
        return False

    else:
          myUniqueList.append(x)
          return True


def addToLeftOvers(x):
    global myLeftOvers
    myLeftOvers.append(x)


print(add(5))
print (myUniqueList)

print(add(10))
print(myUniqueList)

print(add(15))
print(myUniqueList)
print(myLeftOvers)

print(add(10))
print(myUniqueList)
print(myLeftOvers)
