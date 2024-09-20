credit=int(input("Enter the amount of credits you have taken:"))
if credit<24:
    print("The student is a freshman.")
elif credit>23 and credit<54:
    print("You are a sophomore.")
elif credit>53 and credit<84:
    print("Juniors")
elif credit>83:
    print("Seniors")            