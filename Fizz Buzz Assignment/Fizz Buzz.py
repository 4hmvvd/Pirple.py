for i in range(1,101,1):
    if i%15 == 0:
        print("FizzBuzz")
        
    elif i%3 == 0:
        print("Fizz")
        
    elif i%5 == 0:
        print("Buzz")

    elif i>1 and i%i == 0 and i%2 == 1:
            print("Prime")

    else:
        print(i)
