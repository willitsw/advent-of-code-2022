lines = open("./1-1-data.txt").read().splitlines()

current_elf = 1
current_calories = 0

top_calories = [0, 0, 0]

for idx, line in enumerate(lines):
    if line == "":
        for idx, entry in enumerate(top_calories):
            if current_calories > entry:
                top_calories[idx] = current_calories
                break
        top_calories.sort()
        current_elf += 1
        current_calories = 0
        continue
    current_calories += int(line)

print(top_calories)
print(sum(top_calories))
