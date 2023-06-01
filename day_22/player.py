class Player():
    def __init__(self, name, hitpoints, damage, armor, mana) -> None:
        self.name=name
        self.hitpoints=hitpoints
        self.baseHitpoints=hitpoints
        self.damage=damage
        self.baseDamage=damage
        self.armor=armor
        self.baseArmor=armor
        self.mana=mana
        self.baseMana=mana
        self.costs=0
        self.items=[]
        self.spells=[]
        self.activeSpells=[]
        
    def __str__(self) -> str:
        self.updateStats()
        return f'{self.name}, hitpoints={self.hitpoints}, damage={self.damage}, armor={self.armor} , costs={self.costs}, mana={self.mana}'
    
    def __repr__(self) -> str:
        self.updateStats()
        return repr((self.name, self.hitpoints,  self.damage, self.armor, self.costs, self.mana))
    
    def resetStats(self):
        self.hitpoints=self.baseHitpoints
        self.damage=self.baseDamage
        self.armor=self.baseArmor
        self.mana=self.baseMana
        self.costs=0
        self.items=[]
        self.spells=[]
        self.activeSpells=[]
    
    def updateStats(self):
        self.damage=self.baseDamage
        self.armor=self.baseArmor
        self.mana=self.baseMana
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
    
    def addSpell(self, spell):
        self.spells.append(spell)
        self.spells = sorted(self.spells, key=lambda spell: spell.cost, reverse=True)
        
    def castSpell(self, spell):
        if not spell in self.activeSpells:
            self.activeSpells.append(spell)
            print(f'Player casts {spell.name}.')
                    
    
    def battle(self, opponent):
        self.updateStats()
        opponent.updateStats()
        finished=False
        turn=1
        while not finished:
            newActiveSpells=[]
            for spell in self.activeSpells:
                if spell.mana>0:
                    self.mana+=spell.mana
                if spell.damage>0:
                     opponent.hitpoints-=spell.damage
                     print(f'{spell.name} deals {spell.damage} damage; its timer is now {spell.duration}.')
                if spell.heal>0:
                    self.hitpoints+=spell.heal
                spell.duration-=1
                if spell.duration>0:
                    newActiveSpells.append(spell)
                elif spell.armor>0:
                    self.armor-=spell.armor
                if spell.duration<0:
                    print(f'{spell.name} wears off.')
            self.activeSpells=newActiveSpells
            if turn % 2 != 0:  
                print('-- Player turn --') 
                print(f'Player has {self.hitpoints} hit points, {self.armor} armor, {self.mana} mana') 
                print(f'Boss has {opponent.hitpoints} hit points')
                manaSpells = list(filter(lambda spell: spell.mana > 0 , sorted(self.spells, key=lambda spell: spell.mana, reverse=True)))
                spellList = list(filter(lambda spell: spell.mana == 0 , sorted(self.spells, key=lambda spell: spell.damage, reverse=True)))              
                if self.mana<manaSpells[0].cost and manaSpells[0] not in self.activeSpells:
                    self.castSpell(manaSpells[0])
                    self.mana+=manaSpells[0].mana
                else:
                    for spell in spellList:
                        if spell not in self.activeSpells:
                            if spell.duration==0:
                                if spell.damage>0:
                                    opponent.damage-=spell.damage
                                    print(f'Player casts {spell.name}, dealing {spell.damage} damage;')
                                if spell.heal>0:
                                    self.hitpoints+=spell.heal
                                    print(f'Player casts {spell.name}, healing {spell.heal} hitpoints;')
                            if spell.armor>0:
                                    self.armor+=spell.armor 
                                    print(f'Player casts {spell.name}, increasing armor by {spell.armor}.')                    
                            else:
                                self.castSpell(spell)
                            break                        
                opponent.hitpoints-=self.damage-opponent.armor
                #print(f'The {self.name} deals {self.damage}-{opponent.armor} = {self.damage-opponent.armor} damage; the {opponent.name} goes down to {opponent.hitpoints} hit points.')
                if opponent.hitpoints<=0: 
                    finished=True
                    return 'Win'
            else:
                print('-- Boss turn --') 
                print(f'Player has {self.hitpoints} hit points, {self.armor} armor, {self.mana} mana') 
                print(f'Boss has {opponent.hitpoints} hit points')
                self.hitpoints-=opponent.damage-self.armor
                #print(f'The {opponent.name} deals {opponent.damage}-{self.armor} = {opponent.damage-self.armor} damage; the {self.name} goes down to {self.hitpoints} hit points.')
                if self.hitpoints<=0: 
                    finished=True
                    return 'Lose' 
            turn+=1