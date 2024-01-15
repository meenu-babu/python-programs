print("enter the string")
test=input()
vowel="aeiou"
v_count=0
c_count=0
for i in test:
    #print(i)
        if i in vowel:
            v_count+=1
        else:
            c_count+=1
print(f"number of vowels is {v_count}")
print(f"number of consonents is {c_count}")

