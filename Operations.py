def operation(list):
    print("Sum=",sum(list))
    av=sum(list)/len(list)
    print("Avg=",av)
    print("Max=",max(list))
    print("Min=",min(list))
    list.sort() 
    mid = len(list) // 2
    res = (list[mid] + list[~mid]) / 2
    print("Median = " + str(res)) 
list = []
n = int(input("Enter number of elements : "))
print("Enter the elements:")
for i in range(0, n):
    ele = int(input())
    list.append(ele)  
operation(list)   