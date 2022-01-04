import os
import sys
filename = "input.txt"
data = open(os.path.join(sys.path[0], filename ), "r")

totalPaper = 0
totalRibbon = 0

for line in data:
    lwh = line.replace("\n", "").split("x")
    length = int(lwh[0])
    width = int(lwh[1])
    height = int(lwh[2])

    dimensions = [length, width, height]
    dimensions.sort()

    ribbon = 2 * dimensions[0] + 2 * dimensions[1]

    side1 = length * width
    side2 = width * height
    side3 = height * length

    surface = 2 * (side1 + side2 + side3)

    smallestSide = min(side1, side2, side3)

    cubicFeet = length * width * height

    if filename == "example.txt":
        print("line =", line.replace("\n", ""),
              "side1 =", side1,
              "side2 =", side2,
              "side3 =", side3,
              "surface =", surface,
              "smallestSide =", smallestSide,
              "cubic feet =", cubicFeet,
              "ribbon =", ribbon)

    totalPaper += surface + smallestSide
    totalRibbon += cubicFeet + ribbon

print("\ntotal paper =", totalPaper, "; total ribbon =", totalRibbon)
