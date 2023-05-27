class Player():
    def __init__(self, name, hitpoints, damage, armor) -> None:
        self.name=name
        self.hitpoints=hitpoints
        self.baseHitpoints=hitpoints
        self.damage=damage
        self.baseDamage=damage
        self.armor=armor
        self.baseArmor=armor
        self.costs=0
        self.items=[]
        
    def __str__(self) -> str:
        self.updateStats()
        return f'{self.name}, hitpoints={self.hitpoints}, damage={self.damage}, armor={self.armor} , costs={self.costs}'
    
    def __repr__(self) -> str:
        self.updateStats()
        return repr((self.name, self.hitpoints,  self.damage, self.armor, self.costs))
    
    def resetStats(self):
        self.hitpoints=self.baseHitpoints
        self.damage=self.baseDamage
        self.armor=self.baseArmor
        self.costs=0
        self.items=[]
    
    def updateStats(self):
        self.damage=self.baseDamage
        self.armor=self.baseArmor
        self.costs=0
        for item in self.items:
            self.costs+=item.cost
            match item.type:
                case 'Weapon':
                    self.damage+=item.damage
                case 'Armor':
                    self.armor+=item.armor
                case 'Ring':
                    self.armor+=item.armor
                    self.damage+=item.damage
            
    def addItem(self, item):
        self.items.append(item)
    
    def battle(self, opponent):
        self.updateStats()
        opponent.updateStats()
        finished=False
        turn=1
        while not finished:
          if turn % 2 != 0:
              opponent.hitpoints-=self.damage-opponent.armor
              #print(f'The {self.name} deals {self.damage}-{opponent.armor} = {self.damage-opponent.armor} damage; the {opponent.name} goes down to {opponent.hitpoints} hit points.')
              if opponent.hitpoints<=0: 
                finished=True
                return 'Win'
          else:
              self.hitpoints-=opponent.damage-self.armor
              #print(f'The {opponent.name} deals {opponent.damage}-{self.armor} = {opponent.damage-self.armor} damage; the {self.name} goes down to {self.hitpoints} hit points.')
              if self.hitpoints<=0: 
                finished=True
                return 'Lose' 
          turn+=1