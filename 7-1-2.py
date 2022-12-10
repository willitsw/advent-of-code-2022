instructions = open("./7-test.txt").read().splitlines()

instruction_length = len(instructions)


def build_tree(folder, index):
    if index >= instruction_length:
        return folder["size"]

    instruction = instructions[index]

    if instruction.startswith("$ cd .."):
        return folder["size"]
    elif instruction == "$ ls":
        build_tree(folder, index + 1)
    elif instruction.startswith("$ cd"):
        directory = instruction.split(" ")[2]
        folder["size"] += build_tree(folder["children"][directory], index + 1)
    elif instruction.startswith("dir"):
        directory = instruction.split(" ")[1]
        folder["children"][directory] = {
            "size": 0,
            "children": {},
            "parent": None,
            "files": [],
        }
        build_tree(folder, index + 1)
    else:
        folder["size"] += int(instruction.split(" ")[0])
        build_tree(folder, index + 1)


folder = {"size": 0, "children": {}, "parent": None, "files": []}

build_tree(folder, 0)

a = 1

# for instruction in instructions:
#     print(line)
#     line += 1
#     if instruction.startswith("$"):
#         if instruction.find("cd ..") != -1:
#             # go out one level
#             new_folder = folders.get(current_path)["parent"]
#             current_path = current_path.removesuffix(f"-{current_folder}")
#             current_folder = new_folder
#         elif instruction.find("cd") != -1:
#             # go in a level
#             new_folder = instruction.split(" ")[2]
#             current_path = f"{current_path}-{new_folder}"
#             if not folders.get(current_path):
#                 folders[current_path] = {
#                     "size": 0,
#                     "children": [],
#                     "parent": current_folder,
#                     "files": [],
#                 }
#             current_folder = new_folder
#     elif instruction.startswith("dir"):
#         # its a directory
#         directory = instruction.split(" ")[1]
#         if directory not in folders.get(current_path)["children"]:
#             folders.get(current_path)["children"].append(directory)
#     else:
#         # its a file
#         if instruction not in folders.get(current_path)["files"]:
#             folders.get(current_path)["size"] += int(instruction.split(" ")[0])
#             folders.get(current_path)["files"].append(instruction)

# acceptable_sums = []


# def get_total_size(current_folder):
#     folder_size = folders.get(current_folder)["size"]

#     for child in folders.get(current_folder)["children"]:
#         folder_size += get_total_size(f"{current_folder}-{child}")

#     if folder_size <= 100000:
#         acceptable_sums.append(folder_size)

#     return folder_size


# get_total_size("root")

# print(sum(acceptable_sums))
