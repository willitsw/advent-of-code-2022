rows = open("./8-data.txt").read().splitlines()

width = len(rows[0])
length = len(rows)

top_score = 0
top_left = 0
top_right = 0

for length_index in range(1, length - 1):
    for width_index in range(1, width - 1):
        tree = int(rows[length_index][width_index])

        above_length = 1
        for above_index in range(0, length_index)[::-1]:
            if int(rows[above_index][width_index]) < tree and above_index != 0:
                above_length += 1
            else:
                break

        below_length = 1
        for below_index in range(length_index + 1, length):
            if int(rows[below_index][width_index]) < tree and below_index != length - 1:
                below_length += 1
            else:
                break

        left_length = 1
        for left_index in range(0, width_index)[::-1]:
            if int(rows[length_index][left_index]) < tree and left_index != 0:
                left_length += 1
            else:
                break

        right_length = 1
        for right_index in range(width_index + 1, width):
            if int(rows[length_index][right_index]) < tree and left_index != width - 1:
                right_length += 1
            else:
                break

        score = above_length * below_length * right_length * left_length

        if score > top_score:
            top_score = score
            top_left = left_index
            top_right = right_index

print(top_score)