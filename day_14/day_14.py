import os
import sys

filename = "input.txt"
data = open(os.path.join(sys.path[0], filename ), "r")

totalTime = int(2503)

class Reindeer():
    def __init__(self, name, speed, duration, restingTime):
        self.name = name
        self.speed = int(speed)
        self.duration = int(duration)
        self.restingTime = int(restingTime)     
        self.points = 0
        
    def distanceTraveled(self, totalDuration):
        distance=0
        resting = False
        counter = 0
        
        for x in range(0, totalDuration):
            if not resting:
                distance+=self.speed
                counter+=1
                if counter>=self.duration:
                    resting = True
                    counter=0
            elif resting:
                counter+=1
                if counter>=self.restingTime:
                    resting = False
                    counter=0
              

        return distance

winningDistance=0
reindeers={}

for line in data:
    line = line.replace('.', '').replace(',', '')
    line = line.strip()
    data = line.split(" ")
    name = data[0]
    speed = int(data[3])
    duration = int(data[6])
    restingTime = int(data[13])
    reindeer = Reindeer(name, speed, duration, restingTime)
    distance = reindeer.distanceTraveled(totalTime)
    if distance > winningDistance:
        winningDistance = distance      
    reindeers[reindeer.name]=reindeer
        

for n in range(1, totalTime+1):
    leadingReindeer=[]
    leadingDistance=0
    for reindeer in reindeers:
        distance = reindeers[reindeer].distanceTraveled(n)
        if distance>leadingDistance:
            leadingDistance=distance
            leadingReindeer=[]
            leadingReindeer.append(reindeer)
        elif distance==leadingDistance:
            leadingReindeer.append(reindeer)
    for reindeer in leadingReindeer:       
        reindeers[reindeer].points+=1


for reindeer in reindeers:
    print(reindeer + ': ' + str(reindeers[reindeer].points))