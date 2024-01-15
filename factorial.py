def fact():
        print("Enter the number")
        num=int(input())
        fact=1
        if num==0:
            print("factorial is 0")
        else:
            for i in range(1,num+1):
                fact=fact*i
            print("factorial is",fact)
fact()

