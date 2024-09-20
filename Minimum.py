def minimum(a,b):
    if a%10 <b%10:
        return a
    else:
        return b
a=int(input("Enter teh first number:"))
b=int(input("Enter teh second number:"))
n=minimum(a,b)
print(n)    