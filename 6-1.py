packet = open("./6-data.txt").read()
# packet = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

for idx, _ in enumerate(packet):
    substring = packet[idx : idx + 14]

    if len(set(substring)) == len(substring):
        print(idx + 14)
        break
