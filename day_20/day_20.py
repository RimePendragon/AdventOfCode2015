goal = 34000000
found = False


#for x in range(1,10):
#	print(f'x={x}')
#	for y in range(0,x):
#		y+=1
#		print(f'y={y}')
#		print(f'{x} % {y} = {x % y}')

house=1
houses={}	
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
#print('---------------------------')		
#for housenumber, presents in houses.items():
	#print(f'House {housenumber} got {presents} presents.')
