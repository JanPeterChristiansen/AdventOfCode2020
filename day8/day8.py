import re
from copy import deepcopy  # okay python :/

file = open("input.txt", "r")
reg = re.compile("(\w+) ([+-]\d+)")
instructions = re.findall(reg, file.read())
instructions = [list(instr) for instr in instructions]
# %% part I


class run():
    def __init__(self, instructions):
        self.acc = 0
        self.pc = 0
        self.pc_list = []

        while self.pc not in self.pc_list and self.pc < len(instructions):
            self.pc_list.append(self.pc)
            if instructions[self.pc][0] == "acc":
                self.acc += int(instructions[self.pc][1])
                self.pc += 1
            elif instructions[self.pc][0] == "jmp":
                self.pc += int(instructions[self.pc][1])
            elif instructions[self.pc][0] == "nop":
                self.pc += 1


run1 = run(instructions)
print("Answer for part I: acc="+str(run1.acc))
# %% part II


instruction_sets = []
for i, instr in enumerate(instructions):
    if instr[0] == "nop":
        instruction_sets.append(deepcopy(instructions))
        instruction_sets[-1][i][0] = "jmp"
    elif instr[0] == "jmp":
        instruction_sets.append(deepcopy(instructions))
        instruction_sets[-1][i][0] = "nop"

runs = [run(instruction_set) for instruction_set in instruction_sets]

for _run in runs:
    if _run.pc == len(instructions):
        print("Answer for part II: acc="+str(_run.acc))
