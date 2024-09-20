def par(n, i=0, j=0, current="", result=None):
    if result is None:
        result = []
    if len(current) == 2 * n:
        result.append(current)
        return result

    if i < n:
        par(n, i + 1, j, current + "(", result)
    if j < i:
        par(n, i, j + 1, current + ")", result)

    return result
n=int(input("Enter the nunber of paranthesis:"))
print(par(n))
