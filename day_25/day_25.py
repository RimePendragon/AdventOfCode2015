#from https://medium.com/@ghaiklor/advent-of-code-2015-explanation-aa9932db6d6f#9b80

row=2947
col=3029
first_code=20151125
target_index=((pow(row + col - 1, 2) + row + col - 1) / 2) - ((row + col - 1) - col)

result=first_code
for i in range(1, int(target_index) ):
    result = (result * 252533) % 33554393

print(result)