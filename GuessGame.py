import random
a=int(random.randint(1,20))
c=0
for i in range(6):
    n=int(input(print("Guess a number in between the range 1 to 20:")))
    c=c+1
    if n==a and c==1:
        print("GENIOUS- Take a BOW")
        break
    elif n==c and c!=0:
        print("YOU WIN with ",c,"attempts")  
        break  
    elif a!=n and c<5:
        if n>a:
            print("TOO BIG")
        else:
            print("TOO SMALL")
    else:
        print("YOU ARE A LOOSER") 
        break
        