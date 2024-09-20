import math
a=int(input("Enter the first side of traingle:"))
b=int(input("Enter the second side of traingle:"))
c=int(input("Enter the third side of traingle:"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of the triangle is:",area)