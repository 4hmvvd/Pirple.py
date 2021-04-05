for i in range(1,31,1):
    if i%15 == 0:
        print("FizzBuzz")
        
    elif i%3 == 0:
        print("Fizz")
        
    elif i%5 == 0:
        print("Buzz")

    elif i > 1:
        for num in range(2,31,1):
            if num%i == 0:
                print("Prime")
                break
    
    else:
        print(i)
