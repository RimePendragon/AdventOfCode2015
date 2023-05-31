import os
import sys


data = open(os.path.join(sys.path[0], "input.txt" ), "r").readlines()

program=[]
for line in data:
    line = line.strip()
    program.append(line)

registers={'a' : 1, 'b' : 0}
running=True
index=0
while running:
    print('----------------------------------------')
    step=program[index]
    step=step.replace(',', '').split(' ')
    instruction=step[0]
    if instruction=='jmp':
        register=None
        offset=int(step[1])
    else:
        register=step[1]
        offset = 0 if len(step)<3 else int(step[2])   
    print(f'instruction={instruction} register={register} offset={offset}')   
    if instruction=='hlf':
        registers[register]= registers[register]/2
    elif instruction=='tpl':
        registers[register]=registers[register]*3
    elif instruction=='inc':
        registers[register]+=1
    elif instruction=='jmp':
        index+=offset-1
    elif instruction=='jie':
        if registers[register] % 2 == 0: index+=offset-1
    elif instruction=='jio':
        if registers[register] == 1: index+=offset-1     
    index+=1
    print(registers)
    if index>=len(program): running = False
    

    

        
    

