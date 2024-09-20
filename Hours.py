h=int(input("Enter teh hour:"))
print("Is it am or pm:")
t=input("")
f=int(input("how many hours into the future you want to go:"))
newt=h+f
if newt>12:
 if t=='am':
    if (newt%12)%2==0:
        print("New hour:",newt%12,"am")
    else:
        print("New hour:",newt%12,"pm")
 else:
        if (newt%12)%2==0:
            print("New hour:",newt%12,"pm")
        else:
            print("New hour:",newt%12,"am")
 