def fizzbuzz():
    print("enter a number")
    num=int(input())
    for i in range(1,num+1):
        if i%3==0 and i%5==0:
            print(f"{i} Fizz Buzz")
        elif i%5==0:
            print(f"{i} Buzz")
        elif i%3==0:
            print(f"{i} Fizz")
        else:
            print(f"{i} The number is not a multiple of 3 or 5")
fizzbuzz()            