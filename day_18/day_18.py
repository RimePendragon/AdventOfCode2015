import os
import sys
from grid import Grid
 
filename = "input.txt"
data = open(os.path.join(sys.path[0], filename ), "r")
   
data = data.readlines()
rows = len(data)
cols = len(data[0].strip())
grid = Grid(rows, cols)

currentRow=0
for line in data:
    currentCol=0
    line = line.strip()
    for char in line:
        match char:
            case '#':
                grid.setStateOn(currentRow, currentCol)
            case '.':    
                grid.setStateOff(currentRow, currentCol)
        currentCol+=1
    currentRow+=1

grid.turnCornersOn()

print('##############  START ####################')
grid.print()

steps = 100

for n in range(1, steps+1, 1):
    grid.animateGrid()
    grid.turnCornersOn()
    # print('############## ' + str(n) + ' ####################')
    # grid.print()
    
 

print(grid.getCountLightsOn())
