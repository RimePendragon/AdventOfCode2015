import networkx as nx
import matplotlib.pyplot as plt

filename = "input.txt"
data = open(filename, "r")

G = nx.Graph()

for line in data:
    line = line.strip()
    data = line.split(" ")
    point1 = data[0]
    point2 = data[2]
    distance = data[4]
    # print("Distance from", point1, "to", point2, "is", distance)
    G.add_edge(point1, point2, weight=int(distance))

nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig("graph.png")

cities = G.nodes()

minWeight = 999999
minPath = []
maxWeight = 0
maxPath = []
for source in cities:
    for target in cities:
        if source != target:
            # print("Source=", source, "; Target=", target)
            paths = nx.all_simple_paths(G, source, target)
            for path in paths:
                if len(path) == len(G.nodes()) and nx.is_simple_path(G, path):
                    pathWeight = nx.path_weight(G, path, weight='weight')
                    if pathWeight < minWeight:
                        minWeight = pathWeight
                        minPath = path
                    if pathWeight > maxWeight:
                        maxWeight = pathWeight
                        maxPath = path

if len(minPath) > 0:
    for city in minPath:
        print(city, end=" -> ")

print("\b\b\b=", minWeight)

if len(maxPath) > 0:
    for city in maxPath:
        print(city, end=" -> ")

print("\b\b\b=", maxWeight)
