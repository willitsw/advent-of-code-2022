instructions = open("./7-data.txt").read().splitlines()

folders = {"root": {"size": 0, "children": [], "parent": None, "files": []}}

current_path = "root"
current_folder = "root"
parent_folder = ""

line = 1
for instruction in instructions:
    print(line)
    line += 1
    if instruction.startswith("$"):
        if instruction.find("cd ..") != -1:
            # go out one level
            new_folder = folders.get(current_path)["parent"]
            current_path = current_path.removesuffix(f"-{current_folder}")
            current_folder = new_folder
        elif instruction.find("cd") != -1:
            # go in a level
            new_folder = instruction.split(" ")[2]
            current_path = f"{current_path}-{new_folder}"
            if not folders.get(current_path):
                folders[current_path] = {
                    "size": 0,
                    "children": [],
                    "parent": current_folder,
                    "files": [],
                }
            current_folder = new_folder
    elif instruction.startswith("dir"):
        # its a directory
        directory = instruction.split(" ")[1]
        if directory not in folders.get(current_path)["children"]:
            folders.get(current_path)["children"].append(directory)
    else:
        # its a file
        if instruction not in folders.get(current_path)["files"]:
            folders.get(current_path)["size"] += int(instruction.split(" ")[0])
            folders.get(current_path)["files"].append(instruction)

all_sums = []


def get_total_size(current_folder):
    folder_size = folders.get(current_folder)["size"]

    for child in folders.get(current_folder)["children"]:
        folder_size += get_total_size(f"{current_folder}-{child}")

    all_sums.append(folder_size)

    return folder_size


root_size = get_total_size("root")

all_sums.sort()


free_space = 70000000 - root_size

needed_room = 30000000 - free_space

for sum in all_sums:
    if sum >= needed_room:
        print(sum)
        break
