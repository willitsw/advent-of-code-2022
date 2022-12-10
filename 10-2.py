instructions = open("./10-data.txt").read().splitlines()

cycle_number = 1
sprite_mid = 1

crt_row = ["." for _ in range(40)]
crt_screen = [crt_row.copy() for _ in range(6)]
active_row = 0


def print_to_screen():
    if cycle_number <= 40:
        active_row = 0
        pixel = cycle_number - 1
    elif cycle_number <= 80:
        active_row = 1
        pixel = cycle_number - 41
    elif cycle_number <= 120:
        active_row = 2
        pixel = cycle_number - 81
    elif cycle_number <= 160:
        active_row = 3
        pixel = cycle_number - 121
    elif cycle_number <= 200:
        active_row = 4
        pixel = cycle_number - 161
    elif cycle_number <= 240:
        active_row = 5
        pixel = cycle_number - 201

    sprite = [sprite_mid - 1, sprite_mid, sprite_mid + 1]
    if pixel in sprite:
        crt_screen[active_row][pixel] = "X"


for instruction in instructions:
    if instruction == "noop":
        print_to_screen()
        cycle_number += 1
    else:
        new_number = int(instruction.split(" ")[1])
        print_to_screen()
        cycle_number += 1
        print_to_screen()
        cycle_number += 1
        sprite_mid = sprite_mid + new_number

for row in crt_screen:
    rendered = ""
    for char in row:
        rendered += char
    print(rendered)