from item import Item
from spell import Spell
from player import Player
from result import Result
import os
import sys

filename = "items.txt"
data = open(os.path.join(sys.path[0], filename ), "r")
items=[]

for line in data:
    line=line.strip()
    if line[0] != '#':
        line=line.split(';')   
        item = Item(line[0],line[1],line[2],line[3],line[4])
        items.append(item)
    
filename = "spells.txt"
data = open(os.path.join(sys.path[0], filename ), "r")
spells=[]
for line in data:
    line=line.strip()
    if line[0] != '#':
        line=line.split(';')
        spell = Spell(line[0],line[1],line[2],line[3],line[4],line[5],line[6])
        spells.append(spell)

#example
boss = Player("Boss", 13, 8, 0, 0)
player = Player("Player", 10, 0, 0, 250)

for spell in spells:
    player.addSpell(spell)
  
result = Result(player.battle(boss), int(player.mana))

        
#boss = Player("Boss", 51, 9, 0, 0)
#player = Player("Player", 100, 0, 0, 500)