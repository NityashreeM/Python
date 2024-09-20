units=int (input("Enter the units consumed:"))

if units<101:
    print("No charge")
elif units<201:
    cost=(units-100)*5
    print("charge=",cost)
else:
    cost=(units-200)*10+(100*5)
    print("Charge=",cost)    