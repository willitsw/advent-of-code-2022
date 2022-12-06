pairs = open("./4-data.txt").read().splitlines()

overlap_count = 0

for pair in pairs:
    [pair1, pair2] = pair.split(",")

    [pair1_start, pair1_end] = pair1.split("-")
    [pair2_start, pair2_end] = pair2.split("-")

    if (
        (int(pair1_start) >= int(pair2_start))
        and (int(pair1_start) <= int(pair2_end))
        or (int(pair2_start) >= int(pair1_start))
        and (int(pair2_start) <= int(pair1_end))
    ):
        overlap_count += 1


print(overlap_count)
