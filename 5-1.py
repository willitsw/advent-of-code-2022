instructions = open("./5-data.txt").read().splitlines()

stacks = {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}

# stacks = {
#     1: ["J", "H", "G", "M", "Z", "N", "T", "F"],
#     2: ["V", "W", "J"],
#     3: ["G", "V", "L", "J", "B", "T", "H"],
#     4: ["B", "P", "J", "N", "C", "D", "V", "L"],
#     5: ["F", "W", "S", "M", "P", "R", "G"],
#     6: ["G", "H", "C", "F", "B", "N", "V", "M"],
#     7: ["D", "H", "G", "M", "R"],
#     8: ["H", "N", "M", "V", "Z", "D"],
#     9: ["G", "N", "F", "H"],
# }

for instruction in instructions:
    instruction = instruction.replace("move ", "")
    instruction = instruction.replace(" from ", " ")
    instruction = instruction.replace(" to ", " ")
    [count, start, end] = instruction.split(" ")

    for move in range(int(count)):
        crate_to_move = stacks.get(int(start)).pop()
        stacks.get(int(end)).append(crate_to_move)

result = stacks.get(1).pop()

result += stacks.get(2).pop()

result += stacks.get(3).pop()


print(result)
