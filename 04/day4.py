grid = open("input.txt").read().splitlines()

print(grid)

count=0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != "X": continue
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == dc == 0: continue
                if not (0 <= row + 3*dr < len(grid) and 0<= col + 3 * dc < len(grid[0])): continue
                if grid[row+dr][col+dc] == "M" and grid[row+2*dr][col+2*dc] == "A" and grid[row+3*dr][col+ 3* dc] == "S":
                    count += 1 

print(count)

counter = 0
for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[0]) -1 ):
        if grid[row][col] != "A": continue
        corners = grid[row - 1][col - 1] + grid[row - 1][col + 1] + grid[row + 1][col + 1] + grid[row + 1][col - 1]
        if corners in ("SSMM", "MMSS", "MSSM", "SMMS"):
            counter+=1

print(counter)