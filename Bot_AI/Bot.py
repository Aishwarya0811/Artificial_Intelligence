def displayPathtoPrincess(n,grid):
    pos_m = [[i,j] for i in range(n) for j in range(len(list(grid[i]))) if grid[i][j] == 'm']
    pos_p = [[i,j] for i in range(n) for j in range(len(list(grid[i]))) if grid[i][j] == 'p']
    pos_diff = [(pos_m[0][0] - pos_p[0][0]), (pos_m[0][1] - pos_p[0][1])]
    for i in range(0, abs(pos_diff[0])):
        print('DOWN') if pos_diff[0] < 0 else print('UP')
    for i in range(0,abs(pos_diff[1])):
        print('RIGHT') if pos_diff[1] < 0 else print('LEFT') 

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)