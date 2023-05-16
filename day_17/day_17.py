import os
import sys
import itertools

filename = "input.txt"
data = open(os.path.join(sys.path[0], filename ), "r")


containers=[]

for line in data:
    line = line.strip()
    containers.append(int(line))
 
containers.sort(reverse=True)    

total=150
result=[]
minimumSize=len(containers)
minimumCount=0
for x in range(1, len(containers)):
    for combination in itertools.combinations(containers, x):
        if sum(combination) == total:
            #print(combination)
            if len(combination)<minimumSize:
                minimumSize=len(combination)
                minimumCount=1
            elif len(combination)==minimumSize:
                minimumCount+=1
            result.append(combination)
            
print(len(result))
print(minimumCount)
