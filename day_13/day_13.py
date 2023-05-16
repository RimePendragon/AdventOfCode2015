import os
import sys
import itertools

filename = "input.txt"
data = open(os.path.join(sys.path[0], filename ), "r")

partTwo=True


attendees = {}

for line in data:
    line = line.replace('.', '')
    line = line.strip()
    data = line.split(" ")
    personA = data[0]
    operator = data[2]
    value = int(data[3])
    personB = data[len(data)-1]
    if personA not in attendees:
        if partTwo:
            attendees[personA]={"Me":0}
        else:
            attendees[personA]={}
    happiness = attendees[personA]
    if personB not in happiness:
        happiness[personB] = int(value) if 'gain' in operator else 0-(int(value))
    

print(attendees)

if partTwo:
    happiness={}
    for person in attendees.keys():
        happiness[person]=0
    attendees["Me"]=happiness
  
print(attendees) 
  
persons = attendees.keys()
list_combinations = list()


list_combinations += list(itertools.permutations(persons, len(persons)))

scores={}

highScore=0
for n in list_combinations:
    #print('====================================')
    score = 0
    for attendee in n:
        #print(attendee)
        index = n.index(attendee)
        indexP = index-1 if index-1 >-1 else len(n)-1 
        indexN = index+1 if index+1 < len(n) else 0
        #print('prev=' + n[indexP])
        #print('next=' + n[indexN])
        happiness = attendees[attendee]
        score = score + happiness[n[indexP]] + happiness[n[indexN]]
    scores[n] = score
    if score > highScore:
        highScore=score

print(highScore)
