print("Enter range of numbers:")
n=int(input("Enter the smallest number"))
m=int(input("Enter the largest number:"))
print("The prime numbers are:")
for j in range(n,m):
    c=0
    for i in range(1,j+1):
        if j%i==0:
            c=c+1
    if c==2:
        print(j)       