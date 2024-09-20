def cube(a=2):
    c=a*a*a
    print("The cube of ",a,"is",c)
def equal(m,n):
    if m==n:
        print("Ture")
    else:    
        print("False")
a=int(input("Enter a number to find cube:"))
cube(a)
m=input("Enter a charecter:")
n=input("Enter another charecter:")
equal(m,n)        