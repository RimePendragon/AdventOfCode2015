import os
import sys

filename = "input.txt"
data = open(os.path.join(sys.path[0], filename ), "r")


class Ingredient():
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name=name
        self.capacity=int(capacity)
        self.durability=int(durability)
        self.flavor=int(flavor)
        self.texture=int(texture)
        self.calories=int(calories)
        
    def show(self):
        print(self.name)
        print('Capacity: ' + str(self.capacity))
        print('Durability: ' + str(self.durability))
        print('Flavor: ' + str(self.flavor))
        print('Texture: ' + str(self.texture))
        print('Calories: ' + str(self.calories))
        
class Recipe():
    def __init__(self):
        self.ingredients={}
        self.capacity=0
        self.durability=0
        self.flavor=0
        self.texture=0
        self.calories=0
        
        
    def addIngredient(self, ingredient, quantity):
        self.ingredients[ingredient.name] = [ingredient,quantity]
        
    def calculateScore(self):
        for item in self.ingredients.values():
            self.capacity+=item[0].capacity * item[1]
            self.durability+=item[0].durability * item[1]
            self.flavor+=item[0].flavor * item[1]
            self.texture+=item[0].texture * item[1]
            self.calories+=item[0].calories * item[1]
            
        if self.capacity<0: self.capacity=0
        if self.durability<0: self.durability=0
        if self.flavor<0: self.flavor=0
        if self.texture<0: self.texture=0
        
        return self.capacity * self.durability * self.flavor * self.texture           

ingredients ={}        

for line in data:
    line = line.strip()
    data = line.split(':')
    properties = data[1].split(',')
    ingredient = Ingredient(data[0],
                            properties[0].strip().split(' ')[1],
                            properties[1].strip().split(' ')[1],
                            properties[2].strip().split(' ')[1],
                            properties[3].strip().split(' ')[1],
                            properties[4].strip().split(' ')[1]
                            )
    ingredients[ingredient.name]=ingredient
    

teaspoons = 100

#recipe = Recipe()
#recipe.addIngredient(ingredients['Butterscotch'], 44)
#recipe.addIngredient(ingredients['Cinnamon'], 56)
#print(recipe.calculateScore())

# code from https://blog.jverkamp.com/2015/12/15/advent-of-code-day-15/
def splits(amount, count):
    if count <= 1:
        yield [amount]
    else:
        for i in range(amount + 1):
            for subsplit in splits(amount - i, count - 1):
                yield [i] + subsplit


highscore=0

for split in splits(teaspoons, len(ingredients)):
    recipe = Recipe()
    for n in range(0, len(split)):
        recipe.addIngredient(ingredients[list(ingredients.keys())[n]],split[n])    
    score=recipe.calculateScore()
    if recipe.calories == 500 and score > highscore:
        highscore=score

print(highscore)
