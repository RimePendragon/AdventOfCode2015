class Spell:
    def __init__(self, name, cost, duration, damage, heal, armor, mana) -> None:
        #name;cost;duration;damage;heal;armor;mana
        self.name=name
        self.cost=int(cost)
        self.duration=int(duration)
        self.damage=int(damage)
        self.heal=int(heal)
        self.armor=int(armor)
        self.mana=int(mana)
    
    def __str__(self) -> str:
        return f'{self.name}, cost={self.cost}, duration={self.duration}, damage={self.damage}, heal={self.heal}, armor={self.armor}, mana={self.mana}'
    
    def __repr__(self) -> str:
        return repr((self.name, self.cost, self.duration, self.damage, self.heal, self.armor, self.mana))

