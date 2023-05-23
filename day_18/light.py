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