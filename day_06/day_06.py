filename = "input.txt"
data = open(filename, "r")

lights = [[{"status": 0, "brightness": 0} for columns in range(1000)] for rows in range(1000)]


def get_lights_on_count(list_of_lights):
    count = 0
    for x in range(len(list_of_lights)):
        for y in range(len(list_of_lights[x])):
            count += list_of_lights[x][y]["status"]
    return count


def get_brightness_count(list_of_lights):
    count = 0
    for x in range(len(list_of_lights)):
        for y in range(len(list_of_lights[x])):
            count += list_of_lights[x][y]["brightness"]
    return count


def switch_lights(list_of_lights, op, corner1, corner2):
    x1 = int(corner1.split(",")[0])
    y1 = int(corner1.split(",")[1])
    x2 = int(corner2.split(",")[0])
    y2 = int(corner2.split(",")[1])
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            status = list_of_lights[x][y]["status"]
            brightness = list_of_lights[x][y]["brightness"]
            if op == "on":
                status = 1
                brightness += 1
            elif op == "off":
                status = 0
                brightness -= 1
            else:
                status = 0 if status == 1 else 1
                brightness += 2

            brightness = 0 if brightness < 0 else brightness
            list_of_lights[x][y]["status"] = status
            list_of_lights[x][y]["brightness"] = brightness


counter = 0
for line in data:
    counter += 1
    print("\rProcessing line", counter, end="")
    # print(line)
    instruction = line.replace("\n", "").split()
    # print(instruction)
    operation = instruction[1] if instruction[0] != "toggle" else "toggle"
    start = instruction[2] if instruction[0] != "toggle" else instruction[1]
    end = instruction[4] if instruction[0] != "toggle" else instruction[3]
    # print(operation)
    # print(start)
    # print(end)
    switch_lights(lights, operation, start, end)

print("\rTotal lights on:", get_lights_on_count(lights))
print("\rTotal brightness:", get_brightness_count(lights))