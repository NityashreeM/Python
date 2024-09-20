n=int(input("Enter a 3-digit number:"))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("sum is",sum)