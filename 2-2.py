rounds = open("./2-data.txt").read().splitlines()

# A = rock (opponent)
# B = Paper (opponent)
# C = scissors (opponent)

# X = need to lose
# Y = need to draw
# Z = need to win

# rock (you) + 1
# paper (you) + 2
# scissors (you) + 3

# 0 for loss
# 3 for draw
# 6 for win

score = 0

for round in rounds:
    [opponent, need] = round.split(" ")

    if need == "X":  # losing
        if opponent == "A":
            score += 3
        if opponent == "B":
            score += 1
        if opponent == "C":
            score += 2

    if need == "Z":  # win
        score += 6
        if opponent == "A":
            score += 2
        if opponent == "B":
            score += 3
        if opponent == "C":
            score += 1

    if need == "Y":  # draw
        score += 3
        if opponent == "A":
            score += 1
        if opponent == "B":
            score += 2
        if opponent == "C":
            score += 3


print(score)