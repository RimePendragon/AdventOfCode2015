import os
import sys

# https://stackoverflow.com/a/1884277
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

data = open(os.path.join(sys.path[0], "input.txt" ), "r").readlines()
molecule = open(os.path.join(sys.path[0], "request.txt" ), "r").readlines()[0]

replacements=[]

for line in data:
    line = line.strip()
    line = line.replace(" ", "")
    replacement = line.split("=>")
    replacements.append([replacement[0], replacement[1]])

def calibrate():
    generated=[]
    for replacement in replacements:
        key=replacement[0]
        value=replacement[1]
        count=molecule.count(key)
        for n in range(1,count+1):
            split=find_nth(molecule,key,n)
            part1=molecule[:split]
            part2=molecule[split+len(key):]
            new=part1+value+part2
            if generated.count(new)==0:
                generated.append(new)               
    print(len(generated))
    
