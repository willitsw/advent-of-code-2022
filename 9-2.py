moves = open("./9-test.txt").read().splitlines()

body = ["0/0", "0/0", "0/0", "0/0", "0/0", "0/0", "0/0", "0/0", "0/0", "0/0"]

spaces_landed = {"0/0"}

counter = 0


def advance_snake(leader_index, follower_index):
    [leader_y, leader_x] = body[leader_index].split("/")
    [follower_y, follower_x] = body[follower_index].split("/")

    leader_x = int(leader_x)
    leader_y = int(leader_y)
    follower_x = int(follower_x)
    follower_y = int(follower_y)

    # head is 2 above
    if leader_y + 2 == follower_y and leader_x == follower_x:
        follower_y -= 1

    # head is 2 above and left
    elif leader_y + 2 == follower_y and leader_x + 1 == follower_x:
        follower_y -= 1
        follower_x -= 1

    # head is 2 above and right
    elif leader_y + 2 == follower_y and leader_x - 1 == follower_x:
        follower_y -= 1
        follower_x += 1

    # head is 2 below
    elif leader_y - 2 == follower_y and leader_x == follower_x:
        follower_y += 1

    # head is 2 below and left
    elif leader_y - 2 == follower_y and leader_x + 1 == follower_x:
        follower_y += 1
        follower_x -= 1

    # head is 2 below and right
    elif leader_y - 2 == follower_y and leader_x - 1 == follower_x:
        follower_y += 1
        follower_x += 1

    # head is 2 right
    elif leader_x - 2 == follower_x and leader_y == follower_y:
        follower_x += 1

    # head is 2 right and above
    elif leader_x - 2 == follower_x and leader_y + 1 == follower_y:
        follower_x += 1
        follower_y -= 1

    # head is 2 right and below
    elif leader_x - 2 == follower_x and leader_y - 1 == follower_y:
        follower_x += 1
        follower_y += 1

    # head is 2 left
    elif leader_x + 2 == follower_x and leader_y == follower_y:
        follower_x -= 1

    # head is 2 left and above
    elif leader_x + 2 == follower_x and leader_y + 1 == follower_y:
        follower_x -= 1
        follower_y -= 1

    # head is 2 left and below
    elif leader_x + 2 == follower_x and leader_y - 1 == follower_y:
        follower_x -= 1
        follower_y += 1

    if follower_index == 9:
        spaces_landed.add(f"{follower_y}/{follower_x}")

    return f"{follower_y}/{follower_x}"


for move in moves:
    [direction, count] = move.split(" ")
    count = int(count)

    while count > 0:
        # move head
        [head_y, head_x] = body[0].split("/")
        head_y = int(head_y)
        head_x = int(head_x)
        if direction == "U":
            head_y -= 1
        elif direction == "D":
            head_y += 1
        elif direction == "L":
            head_x -= 1
        elif direction == "R":
            head_x += 1

        body[0] = f"{head_y}/{head_x}"

        # move tail
        for part in range(1, len(body)):
            leader_index = part - 1
            follower_index = part
            body[part] = advance_snake(leader_index, follower_index)

        count -= 1


# [print(line) for line in matrix]
print(len(spaces_landed))