rounds = open("./2-data.txt").read().splitlines()

# A = rock (opponent)
# B = Paper (opponent)
# C = scissors (opponent)

# X = rock (you) + 1
# Y = paper (you) + 2
# Z = scissors (you) + 3

# 0 for loss
# 3 for draw
# 6 for win

score = 0

for round in rounds:
    [opponent, you] = round.split(" ")

    if you == "X":
        score += 1
    elif you == "Y":
        score += 2
    elif you == "Z":
        score += 3

    if (
        (you == "X" and opponent == "C")
        or (you == "Y" and opponent == "A")
        or (you == "Z" and opponent == "B")
    ):
        score += 6

    if (
        (you == "X" and opponent == "A")
        or (you == "Y" and opponent == "B")
        or (you == "Z" and opponent == "C")
    ):
        score += 3

print(score)