import math
def nthRoot(x,n):
    r=x**(1/n)
    return r
x=int(input("Enter the number:"))
n=int(input("Enter the root:"))
roo=nthRoot(x,n)
print("nth Root is:",roo)