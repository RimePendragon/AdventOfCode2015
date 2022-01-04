import os
import sys
filename = "input.txt"
data = open(os.path.join(sys.path[0], filename ), "r")
useRobot = True

locationSanta = [0, 0]  # n-z e-w coordinates
locationRobot = [0, 0]  # n-z e-w coordinates
turn = 1
visits = {str(locationSanta[0]) + "x" + str(locationSanta[1])}
for direction in data:
    if turn % 2 == 0 and useRobot is True:
        if direction == "^":
            locationRobot[0] += 1
        if direction == "v":
            locationRobot[0] -= 1
        if direction == "<":
            locationRobot[1] -= 1
        if direction == ">":
            locationRobot[1] += 1
        locationString = str(locationRobot[0]) + "x" + str(locationRobot[1])
    else:
        if direction == "^":
            locationSanta[0] += 1
        if direction == "v":
            locationSanta[0] -= 1
        if direction == "<":
            locationSanta[1] -= 1
        if direction == ">":
            locationSanta[1] += 1
        locationString = str(locationSanta[0]) + "x" + str(locationSanta[1])

    if locationString not in visits:
        visits.add(locationString)
    turn += 1

print(len(visits))
