def addOne(Number):
    output = Number + 1
    return output

Var = 0
print(Var)
Var2 = addOne(Var)
print(Var2)

def addOneAddTwo(NumberOne,NumberTwo):
    output = NumberOne + 1
    output = output + NumberTwo + 2
#   output += NumberTwo + 2
    return output

Sum = addOneAddTwo(1,2)
print(Sum)


def printmessage(message, ntimes = 1):
    print(message * ntimes)

printmessage("Hello")
printmessage("Hello", 5)


num = 1
def func():
    num = 4
    print(num)

func()
print(num)
