temp=int(input("Enter the temp in celcius:"))
if temp<-273.15:
    print ("the temperature is invalid because it is below absolute zero")
elif temp==273.15:
    print ("the temperature is absolute 0.")
elif temp>0 and temp<-273.15:
    print ("the temperature is below freezing.")  
elif temp==0:
    print("the temperature is at the freezing point.")
elif temp>0 and temp<100:
    print("the temperature is in the normal range.")   
elif temp==100:
    print("the temperature is at the boiling point.")     
elif temp>100:
    print("the temperature is above the boiling point.")    