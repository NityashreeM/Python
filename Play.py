def function_play(a,b):
    if a>b:
        if(a%3!=0):
            return a+b
        else:
            return a*b
    elif a<b:
        if(a%3!=0):
            return a*b
        else:
            return a+b
    elif a==b:
        return a*a - b*b
a=int(input("enter a number"))
b=int(input("enter b number"))
c=function_play(a,b)
if(b%7==0):
   print(c*2)
else:
    print(c)