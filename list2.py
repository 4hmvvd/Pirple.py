#List from online. Haven't ran the code 

myUniqueList = []

    
def UList(myUniqueList):
    print(f'Current Numbers List {myUniqueList}')
    num = int(input("Please enter a number to add to list:\n"))
    for n in range(num):
        numbers=int(input('Enter number:\n'))
        myUniqueList.append(numbers)
        myUniqueList=list(dict.fromkeys(myUniqueList))
print (UList(myUniqueList))
print (f'Current Numbers List {myUniqueList}')

