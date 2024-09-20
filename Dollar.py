def convert(dolar):
    rupee=dolar*83.95
    return rupee
dolar=float(input("Enter the money in dollar:"))
rupee=convert(dolar)
print("In rupees = ",rupee)