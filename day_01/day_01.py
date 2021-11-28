filename = "input.txt"
data = open(filename, "r").read()

floor = 0
index = 0
found = False
for x in data:
    index += 1
    if x == "(":
        floor += 1
    if x == ")":
        floor -= 1
    if floor < 0 and found is False:
        found = True
        print("Basement index:", index)

print("Floor:", floor)
