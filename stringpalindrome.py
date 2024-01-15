print("enter a string that you have to check palindrome or not")
test=input()
rev_test=test[::-1]
if test==rev_test:
    print("It is palindrome")
else:
    print("It is Not palindrome")