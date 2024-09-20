def subset(str, curr, index=-1):
    n=len(str)
    if index==n:
        return
    print(curr)
    for i in range(index +1,n):
        curr+=str[i]
        subset(str,curr,i)
        curr = curr.replace(curr[len(curr) - 1], "") 
    return

str=input("Enter the string:")

subset(str,"",-1,)