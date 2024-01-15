print("Enter a number")
num=int(input())
if num==1:
    print("not a prime")
elif num==2:
    print("prime number")
else:
    is_prime=True
    for i in range(2,(num//2)+1):
        if num%i==0:
           is_prime=False
    if is_prime:
        print("It's a prime number")
    else:
        print("Not a prime")
