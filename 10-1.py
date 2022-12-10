instructions = open("./10-data.txt").read().splitlines()

cycle_number = 1
x = 1
recorded_signals = []


def record_signal():
    if cycle_number in [20, 60, 100, 140, 180, 220]:
        recorded_signals.append(cycle_number * x)


for instruction in instructions:
    if instruction == "noop":
        record_signal()
        cycle_number += 1
    else:
        new_number = int(instruction.split(" ")[1])
        record_signal()
        cycle_number += 1
        record_signal()
        cycle_number += 1
        x = x + new_number

print(sum(recorded_signals))