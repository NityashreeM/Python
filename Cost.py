n=int(input("Numbers of items purchased:"))
if n<10:
    print("Total cost:",n*12)
elif n>9 and n<100:
    print("Total cost:",n*10)
elif n>99:
    print("Total cost:",n*7)        