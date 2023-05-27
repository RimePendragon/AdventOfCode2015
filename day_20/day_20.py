# https://rosettacode.org/wiki/Factors_of_an_integer#Python
from itertools import chain, cycle, accumulate # last of which is Python 3 only

def factors(n):
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
            if c*c > n: break
            if n%c: continue
            d,p = (), c
            while not n%c:
                n,p,d = n//c, p*c, d + (p,)
            yield(d)
        if n > 1: yield((n,))

    r = [1]
    for e in prime_powers(n):
        r += [a*b for a in r for b in e]
    return r


def brute_force(goal):
	house=1
	houses={}	
	found = False
	while not found:
		#print(f'House {house}')
		houses[str(house)]=0
		for elf in range(0,house):
			elf+=1
			if (house % elf) == 0:
					houses[str(house)]+=elf*10
					#print(f'Elf {elf} visits house {house} and gives {elf*10} presents for a total of {houses[str(house)]} presents.')
		if houses.get(str(house))>=goal:
			found=True
		print(f'House {house} has {houses.get(str(house))} presents.')
		house+=1
		#if house>20:
		#	found=True
		print(house)	
  
def part1(goal):
	house=1
	found = False
	while not found:
		elves=factors(house)
		presents=0
		for elf in elves:
			presents+=elf*10
		if presents>=goal:
			found=True
		else:
			house+=1
	print(house)
 
def part2(goal):
	house=1
	found = False
	while not found:
		elves=factors(house)
		presents=0
		for elf in elves:
			if (house / elf) <= 50:
				presents+=elf*11
		if presents>=goal:
			found=True
		else:
			house+=1
	print(house)
    


goal = 34000000

part2(goal)

