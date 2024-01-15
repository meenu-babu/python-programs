print("enter the number")
num=int(input())
r_num=0
while num!=0:
    digit=num%10
    r_num=r_num*10+digit
    num=num//10
print("reversed number is",r_num)
