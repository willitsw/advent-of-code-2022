moves = open("./9-data.txt").read().splitlines()

head_x = tail_x = head_y = tail_y = 0

spaces_landed = {f"{tail_y}-{tail_x}"}

for move in moves:
    [direction, count] = move.split(" ")

    count = int(count)

    while count > 0:
        # move head
        if direction == "U":
            head_y -= 1
        elif direction == "D":
            head_y += 1
        elif direction == "L":
            head_x -= 1
        elif direction == "R":
            head_x += 1

        # move tail
        # head is 2 above
        if head_y + 2 == tail_y and head_x == tail_x:
            tail_y -= 1

        # head is 2 above and left
        elif head_y + 2 == tail_y and head_x + 1 == tail_x:
            tail_y -= 1
            tail_x -= 1

        # head is 2 above and right
        elif head_y + 2 == tail_y and head_x - 1 == tail_x:
            tail_y -= 1
            tail_x += 1

        # head is 2 below
        elif head_y - 2 == tail_y and head_x == tail_x:
            tail_y += 1

        # head is 2 below and left
        elif head_y - 2 == tail_y and head_x + 1 == tail_x:
            tail_y += 1
            tail_x -= 1

        # head is 2 below and right
        elif head_y - 2 == tail_y and head_x - 1 == tail_x:
            tail_y += 1
            tail_x += 1

        # head is 2 right
        elif head_x - 2 == tail_x and head_y == tail_y:
            tail_x += 1

        # head is 2 right and above
        elif head_x - 2 == tail_x and head_y + 1 == tail_y:
            tail_x += 1
            tail_y -= 1

        # head is 2 right and below
        elif head_x - 2 == tail_x and head_y - 1 == tail_y:
            tail_x += 1
            tail_y += 1

        # head is 2 left
        elif head_x + 2 == tail_x and head_y == tail_y:
            tail_x -= 1

        # head is 2 left and above
        elif head_x + 2 == tail_x and head_y + 1 == tail_y:
            tail_x -= 1
            tail_y -= 1

        # head is 2 left and below
        elif head_x + 2 == tail_x and head_y - 1 == tail_y:
            tail_x -= 1
            tail_y += 1

        # add spaces
        spaces_landed.add(f"{tail_y}-{tail_x}")
        count -= 1

print(len(spaces_landed))