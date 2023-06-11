def validation(grid, row, col , num): 
    for x in range(9):
        if grid[row][x]==num:
            return False
    for x in range(9):
        if grid[x][col]==num:
            return False
    corner_row = row - row%3
    corner_col = col - col%3
    for x in range(3):
        for y in range(3):
             if grid[corner_row + x][corner_col+y] == num:
                 return False
    return True

def answer (grid, row,col):
    if col == 9:
        if row ==8:
            return True
        row +=1
        col = 0
    if grid[row][col]>0:
        return answer(grid, row, col+1)
    for x in range (1,10):
        if(validation(grid,row,col,x)):
            grid[row][col]=x
            if (answer(grid,row,col+1)):
                return True
        grid[row][col]=0
    return False
print ("Welcome to Sudoku Solve")
print("Enter your grid:")
grid = []
for x in range(9):
    print("Enter row: " + str(x+1))
    row = []
    for y in range(9):
        value = int(input("    Enter column " + str(y+1) + ": "))
        row.append(value)
    grid.append(row)
print("Solved")
if answer(grid,0,0):
    for i in range (9):
        for j in range (9):
            print(grid[i][j], end = " ")
        print()
else:
    print("No Solution")
    

        
        
    
  
        
    
