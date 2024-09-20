def find_path(grid):
    if not grid or not grid[0]:
        return []
    
    n, m = len(grid), len(grid[0])
    path = []
    
    def dfs(x, y):
       
        if x == n - 1 and y == m - 1:
            path.append((x, y))
            return True
        
      
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return False
        
       
        grid[x][y] = 0  
        path.append((x, y))

     
        if (dfs(x + 1, y) or 
            dfs(x - 1, y) or  
            dfs(x, y + 1) or   
            dfs(x + 1, y + 1) or  
            dfs(x, y - 1)):   
            return True
        
       
        path.pop()
        grid[x][y] = 1 
        return False

    if dfs(0, 0):
        return path
    else:
        return []
def input_2d_array():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    array = []
    print("Enter the array row by row (space-separated values):")
    
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Please enter exactly {cols} values for row {i + 1}.")
            return None
        array.append(row)
    
    return array

grid = input_2d_array()
result = find_path(grid)
if result:
    print("Path found:", result)
else:
    print("No path found.")
