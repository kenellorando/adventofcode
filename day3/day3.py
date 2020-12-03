grid = []
for line in open("input.txt", 'r').readlines():
    grid.append(line.strip())

## Part 1
x = 0
trees = 0
for row in grid[1:len(grid)]: # For every row, starting from row 1 (2nd)
    x += 3
    if x >= len(row):
        x -= len(row)
    if row[x] == "#":
        trees += 1
print("Part one count:", trees)

## Part 2

moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
treeSets = []    
for coords in moves: # For each slope set
    trees = 0
    x, y = 0,0 # Starting from 0,0

    while y < len(grid): # For the y rows being examined
        row = grid[y]
        if row[x] == "#": # Check first
            trees += 1
        x += coords[0] # Then move
        if x >= len(row):
            x -= len(row)
        y += coords[1]
    treeSets.append(trees)

totalTrees = 1
for tree in treeSets:
    totalTrees *= tree
print("Part two product:", totalTrees)