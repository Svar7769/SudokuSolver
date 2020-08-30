#Function to check if number is valid 
#it checks for row ,column and block
#if all checks out it returns true

def check(x,y,n):
    #check for row and cols
    for i in range(0,9):
        if grid[x][i]==n:
            return False
        if grid[i][y]==n:
            return False
    #in block
    if x >= 0 and x <=2:
        if y >= 0 and y <= 2:
            for i in range(0,3):
                for j in range(0,3):
                    if grid[i][j]==n:
                        return False
        elif y >= 3 and y <= 5:
            for i in range(0,3):
                for j in range(3,6):
                    if grid[i][j]==n:
                        return False
        elif y >= 6 and y <= 8:
            for i in range(0,3):
                for j in range(6,9):
                    if grid[i][j]==n:
                        return False
    elif x >= 3 and x <= 5:
        if y >= 0 and y <= 2:
            for i in range(3,6):
                for j in range(0,3):
                    if grid[i][j]==n:
                        return False
        elif y >= 3 and y <= 5:
            for i in range(3,6):
                for j in range(3,6):
                    if grid[i][j]==n:
                        return False
        elif y >= 6 and y <= 8:
            for i in range(3,6):
                for j in range(6,9):
                    if grid[i][j]==n:
                        return False
    elif x >= 6 and x <= 8:   
        if y >= 0 and y <= 2:
            for i in range(6,9):
                for j in range(0,3):
                    if grid[i][j]==n:
                        return False
        elif y >= 3 and y <= 5:
            for i in range(6,9):
                for j in range(3,6):
                    if grid[i][j]==n:
                        return False
        elif y >= 6 and y <= 8:
            for i in range(6,9):
                for j in range(6,9):
                    if grid[i][j]==n:
                        return False
    return True
