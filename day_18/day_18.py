import os
import sys

############### class Light() ###############

class Light():
    def __init__(self,x, y, state):
        self.x=x
        self.y=y
        self.state=state
        self.newState=state
    
    def setState(self, state):
        self.state=state
        self.newState=state
    
    def getState(self):
        return self.state
        
    def turnOff(self):
        self.state=0
        self.newState=0
    
    def turnOn(self):
        self.state=1
        self.newState=1
        
    def turnNewStateOff(self):
        self.newState=0
    
    def turnNewStateOn(self):
        self.newState=1
        
    def update(self):
            self.state=self.newState
  
 ############### class Grid() ###############
    
class Grid():
    def __init__(self, rows, cols):
        self.grid =[[0 for x in range(rows)] for y in range(cols)] 
        self.rows=rows
        self.cols=cols
        for x in range(rows):
            for y in range(cols):
                self.grid[x][y]=Light(x,y, 0)
     
    def turnCornersOn(self):
        self.grid[0][0].turnOn()
        self.grid[self.rows-1][self.cols-1].turnOn()
        self.grid[0][self.cols-1].turnOn()
        self.grid[self.rows-1][0].turnOn()
                
    def setStateOn(self, x, y):
        self.grid[x][y].setState(1)

    def setStateOff(self, x, y):
        self.grid[x][y].setState(0)
        
    def animateGrid(self):
        for x in range(self.rows):
            for y in range(self.cols):
                currentState=self.grid[x][y].getState()
                neighbors=0
                for a in range (x-1, x+2, 1):
                    for b in range(y-1, y+2, 1):
                        if a > -1 and a < self.rows:
                            if b > -1 and b < self.cols:
                                if a != x or b != y:
                                    neighbors+=self.grid[a][b].getState()
                if currentState==1 and (neighbors<2 or neighbors>3):
                     self.grid[x][y].turnNewStateOff()
                elif currentState==0 and neighbors==3:
                    self.grid[x][y].turnNewStateOn()
        self.update()
                            
                
    def update(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.grid[x][y].update()
                
    def getCountLightsOn(self):
        count=0
        for x in range(self.rows):
            for y in range(self.cols):
                count += self.grid[x][y].state
        return count
    
    def print(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.grid[x][y].getState()==1:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
        print('')
                
 #########################################################
 
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
