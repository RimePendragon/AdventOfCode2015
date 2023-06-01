class Item:
    def __init__(self, name, type, cost, damage, armor) -> None:
        self.name=name
        self.type=type
        self.cost=int(cost)
        self.damage=int(damage)
        self.armor=int(armor)
    
    def __str__(self) -> str:
        return f'{self.name}, type={self.type}, cost={self.cost}, damage={self.damage}, armor={self.armor}'
    
    def __repr__(self) -> str:
        return repr((self.name, self.type, self.cost, self.damage, self.armor))

