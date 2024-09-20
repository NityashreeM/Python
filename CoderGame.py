import random
a=str(random.randint(1000,9999))
c=0

for i in range(20):
    cow=0
    bull=0
    n=input("Enter password(a 4 digit number)")
    res1 = [int(x) for x in str(a)]
    res2 = [int(x) for x in str(n)]
    c=c+1
    if a==n:
        print("Hacked in ",c,"attempts")
        break
    else:
        for j in range(4):
            for k in range(4):
                if res1[j]==res2[k] and j==k:
                    bull=bull+1 
                elif res1[j]==res2[k] and j!=k:
                    cow=cow+1
    print("Bull=",bull,"cow=",cow)
    if bull==4:
        print("Hacked with ",c,"attempts")
        exit()