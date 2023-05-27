from item import Item
from player import Player
from result import Result
import os
import sys

filename = "items.txt"
data = open(os.path.join(sys.path[0], filename ), "r")
items=[]

for itemString in data:
    itemString=itemString.strip()
    itemString=itemString.split(';')
    item = Item(itemString[0],itemString[1],itemString[2],itemString[3],itemString[4])
    items.append(item)

boss = Player("Boss", 100, 8, 2)
player = Player("Player", 100, 0, 0)

#example
# boss = Player("Boss", 12, 7, 2)
# player = Player("Player", 8, 5, 5)
# print(player.battle(boss))

resultList=[]
weaponList = filter(lambda item: item.type == 'Weapon', sorted(items, key=lambda item: item.cost))
for weapon in weaponList:
    armorList = filter(lambda item: item.type == 'Armor', sorted(items, key=lambda item: item.cost))
    for armor in armorList:
        ringList1 = filter(lambda item: item.type == 'Ring', sorted(items, key=lambda item: item.cost))
        for ring1 in ringList1:
            ringList2 = filter(lambda item: item.type == 'Ring', sorted(items, key=lambda item: item.cost))
            for ring2 in ringList2:
                player.resetStats()
                boss.resetStats()
                player.addItem(weapon)
                player.addItem(armor)
                player.addItem(ring1)
                player.addItem(ring2)
                result = Result(player.battle(boss), int(player.costs), player.items)
                resultList.append(result)


wonList = list(filter(lambda result: result.outcome == 'Win', sorted(resultList, key=lambda result: result.cost)))
print(wonList[0])
lostList = list(filter(lambda result: result.outcome == 'Lose', sorted(resultList, key=lambda result: result.cost, reverse=True)))
print(lostList[0])
