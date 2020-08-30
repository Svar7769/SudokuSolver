#program uses recursive function to backtrack the solution 

from check import check

def solve():
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j] == 0:
                for n in range(1,10):
                    if check(i,j,n) :
                        grid[i][j]=n
                        solve()
                    if n==9:
                        grid[i][j]=0
                        return 
    print(grid)
solve()
