import os
import sys
import re

input1 = open(os.path.join(sys.path[0], "input.txt" ), "r").read()
input2 = open(os.path.join(sys.path[0], "request.txt" ), "r").read()




# from https://old.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4nsdd/

molecule = input2.split('\n')[-1][::-1]
reps = {m[1][::-1]: m[0][::-1] 
        for m in re.findall(r'(\w+) => (\w+)', input1)}
def rep(x):
    return reps[x.group()]

count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    count += 1

print(count)