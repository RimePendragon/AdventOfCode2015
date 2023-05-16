import os
import sys

filename = "input.txt"
data = open(os.path.join(sys.path[0], filename ), "r")

found = False

highscore=0
highscoreAunt=''

for line in data:
    line = line.strip()
    name = line[:line.find(':')].strip()
    properties=line[line.find(':')+1:].strip().split(',')
    aunt={}
    aunt[name]=name
    for item in properties:
        item=item.split(':')
        aunt[item[0].strip()]=int(item[1].strip())
    
    score=0;
    if ('children' in aunt and aunt['children']==3):  
        score+=1 
    if 'cats' in aunt and aunt['cats']>7:
        score+=1 
    if 'samoyeds' in aunt and aunt['samoyeds']==2:
        score+=1 
    if 'pomeranians' in aunt and aunt['pomeranians']<3:
        score+=1 
    if 'akitas' in aunt and aunt['akitas']==0:
        score+=1 
    if 'vizslas' in aunt and aunt['vizslas']==0:
        score+=1 
    if 'goldfish' in aunt and aunt['goldfish']<5:
        score+=1 
    if 'trees' in aunt and aunt['trees']>3:
        score+=1 
    if 'cars' in aunt and aunt['cars']==2:
        score+=1 
    if 'perfumes' in aunt and aunt['perfumes']==1:
        score+=1 
    
    if score>highscore:
        highscore=score
        highscoreAunt=name


print(highscoreAunt)
        
    
    
    
    
    
class Aunt():
    def __init__(self, children, cats,  samoyeds, pomeranians, akitas, vizslas, goldfish,  trees, cars, perfume):
        self.children=int(children)
        self.cats=int(cats)
        self.samoyeds=int(samoyeds)
        self.pomeranians=int(pomeranians)
        self.akitas=int(akitas)
        self.vizslas=int(vizslas)
        self.goldfish=int(goldfish)
        self.trees=int(trees)
        self.cars=int(cars)
        self.perfume=int(perfume)
        
        
    
    
    