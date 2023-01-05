import json
from functools import reduce

f = open("aqua.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]

def pick_animals_type(animal):
    return animal["type"], 1

def reducer(acd, var):
    print(var)
    if var[0] not in acd.keys():
        acd[var[0]] = var[1]
    else: 
        acd[var[0]] = acd[var[0]] + acd[var[1]]
        print(acd)
    return acd
        

type_animals = list(map(pick_animals_type, animals))
print(type_animals)
reduce(reducer, type_animals, {})
