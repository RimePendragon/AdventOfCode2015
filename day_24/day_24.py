import os
import sys
import itertools
data = open(os.path.join(sys.path[0], "example.txt" ), "r").readlines()

packages=[]
for line in data:
    line = line.strip()
    packages.append(int(line))
  


weight=sum(packages)/3
   
def getGroup(packages, weight):
    packages.sort(reverse=True)
    group=[]
    for package in packages:
        if sum(group)<weight:
            group.append(package)
        if sum(group)>weight:
            group=group[-1:]
    return group        



# for permutation in itertools.permutations(packages, len(packages)):
#     group1=[]
#     group2=[]
#     group3=[]
#     for package in permutation:
#         sum1=sum(group1)
#         sum2=sum(group2)
#         sum3=sum(group3)
#         if sum1 <= sum2 and sum1 <= sum3:
#             group1.append(package)
#         elif sum2 <= sum1 and sum2 <= sum3:
#             group2.append(package)
#         elif sum3 <= sum1 and sum3 <= sum2:
#             group3.append(package)
#     print(group1)
#     print(group2)
#     print(group3)
#     print('---------------------------------------------------------------')


# https://old.reddit.com/r/adventofcode/comments/3y1s7f/day_24_solutions/cy9srkh/
import functools
import operator
nums = list(map(int, [line.strip("\n") for line in open(os.path.join(sys.path[0], "input.txt" ), "r")]))
parts = 4
tot = sum(nums)/parts

def hasSum(lst, sub):
    for y in range(1,len(lst)): 
        for x in (z for z in itertools.combinations(lst, y) if sum(z) == tot):
            if sub == 2:
                return True
            elif sub < parts:
                return hasSum(list(set(lst) - set(x)), sub - 1)
            elif hasSum(list(set(lst) - set(x)), sub - 1):
                return functools.reduce(operator.mul, x, 1)
            
print(hasSum(nums, parts))