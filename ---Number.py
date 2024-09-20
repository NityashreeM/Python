n=int(input("Enter the number:"))
for i in range(1, 6):
    print(n * i, end="--" if i < 5 else "")