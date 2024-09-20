sal=int(input("Enter the salary:"))
t=int(input("enter the time period of service:"))
if t>10:
    bonus=sal*.1
elif t<11 and t>5:
    bonus=sal*.08
elif t<6:
    bonus=sal*.05
print("Your bonus is:",bonus)            