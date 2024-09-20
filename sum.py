def combination_sum(candidates, target, current, result, index):
    if target == 0:
        result.append(list(current))
        return
    if target < 0:
        return

    for i in range(index, len(candidates)):
        current.append(candidates[i])
        combination_sum(candidates, target - candidates[i], current, result, i)
        current.pop()

n=int(input("enter the number of elements:"))
print("Enter the discrete variables (space-separated)")
candidates = [1, 2, 4, 1, 3]
target = int(input("enter the target:"))
current = []
result = []

combination_sum(candidates, target, current, result, 0)

print("All combinations that sum up to", target, "are:")
for res in result:
    print(res)
