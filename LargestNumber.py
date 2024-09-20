a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
max=a
if b>a and b>c:
    max=b
elif c>a and c>b:
    max=c
print("The largest number is:",max)    