import re

file = open("input.txt","r")
lines = file.read().split("\n")
del lines[-1]

pattern = re.compile("(\d )?(\w+ \w+) bags")
rules = [re.findall(pattern, rule) for rule in lines]

valid_bags = []
for rule in rules:
    if any("shiny gold" in color[1] for color in rule):
        valid_bags.append(rule[0][1])

