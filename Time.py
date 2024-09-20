time=int(input("Enter the time in seconds:"))
sec=time%60
time=time//60
min=time%60
hour=time//60
print("hours:",hour,"Mins:",min,"Sec:",sec)