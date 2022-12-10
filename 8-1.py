rows = open("./8-data.txt").read().splitlines()

width = len(rows[0])
length = len(rows)

visible = width * 2 + length * 2 - 4

for length_index in range(1, length - 1):
    for width_index in range(1, width - 1):
        tree = int(rows[length_index][width_index])

        above_is_visible = True
        for above_index in range(0, length_index):
            if int(rows[above_index][width_index]) >= tree:
                above_is_visible = False

        below_is_visible = True
        for below_index in range(length_index + 1, length):
            if int(rows[below_index][width_index]) >= tree:
                below_is_visible = False

        left_is_visible = True
        for left_index in range(0, width_index):
            if int(rows[length_index][left_index]) >= tree:
                left_is_visible = False

        right_is_visible = True
        for right_index in range(width_index + 1, width):
            if int(rows[length_index][right_index]) >= tree:
                right_is_visible = False

        if above_is_visible or below_is_visible or left_is_visible or right_is_visible:
            visible += 1

print(visible)