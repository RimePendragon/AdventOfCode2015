from light import Light

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