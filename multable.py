def multable():
    print("enter a number")
    num=int(input())
    for i in range(1,11):
        print(f"{i}*{num}={i*num}")
multable()