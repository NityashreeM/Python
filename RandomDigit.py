import random
def rando(n):
    a=10**(n-1)
    b=(10**(n))-1
    r=int(random.randint(a,b))
    return r
n=int(input("Eneter the number:"))
ra=rando(n)
print("The random number is :",ra)