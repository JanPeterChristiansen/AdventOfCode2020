import re

file = open("input.txt", "r")
lines = file.read().replace("no other bags", "").split("\n")
del lines[-1]

pattern = re.compile("(\w+ \w+) bags?")
rules = [re.findall(pattern, rule) for rule in lines]

start_points = [rule[0] for rule in rules]


def contains_shiny_gold(rule):
    if len(rule) == 1:
        # reached an endpoint
        return 0
    elif rule[0] == "shiny gold":
        # a shiny golden cannot contain another shiny golden
        return 0
    else:
        if "shiny gold" in rule:
            # bag contains a shiny golden bag
            return 1
        else:
            # bag does not contain a shiny golden bag
            for bag in rule[1:]:
                # check the contained bag if they contain a shiny golden instead
                indx = start_points.index(bag)
                if contains_shiny_gold(rules[indx]):
                    return 1

            return 0


cnt = 0
for i, rule in enumerate(rules):
    if contains_shiny_gold(rule):
        cnt += 1


pattern2 = re.compile("(\d)? ?(\w+ \w+) bags?")
rules2 = [re.findall(pattern2, rule) for rule in lines]


def nr_of_bags(rule):
    if len(rule) == 1:
        return 0
    else:
        summe = 0
        for bag in rule[1:]:
            indx = start_points.index(bag[1])
            summe += int(bag[0])+int(bag[0])*nr_of_bags(rules2[indx])
        return summe


cnt2 = 0
indx = start_points.index("shiny gold")
cnt2 = nr_of_bags(rules2[indx])
