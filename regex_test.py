import re

regex = re.compile("[0-9a-f")

string = ""

if regex.match(string):
    print("yay")