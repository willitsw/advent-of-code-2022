lines = open("./1-1-data.txt").read().splitlines()

current_elf = 1
current_calories = 0

top_elf = 0
top_calories = 0

for idx, line in enumerate(lines):
    if current_elf == 178:
        a = 1
    if current_calories > top_calories:
        print(
            f"WOOO TOP CALORIES FOR ELF {current_elf} with calories {current_calories} index {idx}"
        )
        top_calories = current_calories
        top_elf = current_elf
    if line == "":
        print(f"Elf {current_elf} had {current_calories}")
        current_elf += 1
        current_calories = 0
        continue
    current_calories += int(line)

print(top_elf)
