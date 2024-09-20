temp=int(input("Enter the tempreture:"))
print("Enter 'f' for faranite and 'c' for celcius:")
c=input()
if c=='f':
    t=5/9*(temp-52)
elif c=='c':
    t=((9/5)*temp)+32 
print("The tempreture after convertion is:",t)       