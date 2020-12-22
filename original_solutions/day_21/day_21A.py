import re
from collections import defaultdict
from pprint import pp

with open("input_21.txt") as input_file:
    possible = dict()
    all_allergens = set()
    all_ingredients = set()
    foods = []
    occurences = defaultdict(int)
    for line in [line.strip() for line in input_file]:
        ingredients = set(re.findall(r"\w+", line.split("(contains")[0]))
        for ing in ingredients:
            occurences[ing] += 1
        all_ingredients.update(ingredients)
        allergens = set([i[0] for i in re.findall(r"(\w+)(, |\))", line.split("(contains")[1])])
        all_allergens.update(allergens)
        foods.append((ingredients, allergens))
    for ingredients, allergens in foods:
        for al in allergens:
            if al in possible:
                possible[al].intersection_update(ingredients)
            else:
                possible[al] = set(ingredients)
    no_allergen = all_ingredients.difference(set().union(*possible.values()))
    print(" -> part A:", sum([occurences[i] for i in no_allergen]))
    contains = dict()
    while len(contains) < len(all_allergens):
        for alg, ings in possible.items():
            if len(ings) == 1:
                ingredient = list(ings)[0]
                contains[ingredient] = alg
                for i in possible.values():
                    if ingredient in i: i.remove(ingredient)
                break
    print(",".join([i[0] for i in sorted(contains.items(), key=lambda i: i[1])]))
