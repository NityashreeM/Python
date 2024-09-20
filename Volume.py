def volume(l=1,b=1,h=1):
    v=l*b*h
    return v
l=float(input("Enter the length:"))
b=float(input("Enter the breath:"))
h=float(input("Enter the height:"))
v=volume(l,b,h)
print("The volume is: ",v)