import time


def load_file(filename):
    basin = []
    with open(filename) as file:
        for row, line in enumerate(file):
            basin_row = []
            for col, char in enumerate(line.strip()):
                if char == '.':
                    basin_row.append([])
                else:
                    basin_row.append([char])
            basin.append(basin_row)

    return basin, [0, 1], [len(basin)-1, len(basin[0])-2]


def text(basin, elf_location):
    text = ""
    for row, line in enumerate(basin):
        for col, point in enumerate(line):
            if [row, col] == elf_location:
                text += "E"
            elif len(point) == 0:
                text += "."
            elif len(point) == 1:
                text += point[0]
            else:
                text += str(len(point))
        text += "\n"
    return text


def move_blizzards(basin):
    new_basin = [[[] for _ in range(len(basin[0]))] for _ in range(len(basin))]

    for row, line in enumerate(basin):
        for col, point in enumerate(line):
            for item in point:
                if item == '<':
                    if col == 1:
                        new_basin[row][len(new_basin[0])-2].append('<')
                    else:
                        new_basin[row][col-1].append('<')
                elif item == '>':
                    if col == len(new_basin[0])-2:
                        new_basin[row][1].append('>')
                    else:
                        new_basin[row][col+1].append('>')
                elif item == '^':
                    if row == 1:
                        new_basin[len(new_basin)-2][col].append('^')
                    else:
                        new_basin[row-1][col].append('^')
                elif item == 'v':
                    if row == len(new_basin)-2:
                        new_basin[1][col].append('v')
                    else:
                        new_basin[row+1][col].append('v')
                else:
                    new_basin[row][col].append(item)

    return new_basin


def can_stay(basin, elf_location):
    if len(basin[elf_location[0]][elf_location[1]]) > 0:
        return False
    else:
        return True


def can_move_right(basin, elf_location):
    if len(basin[elf_location[0]][elf_location[1]+1]) == 0:
        return True
    else:
        return False


def move_right(elf_location):
    return [elf_location[0], elf_location[1]+1]


def can_move_left(basin, elf_location):
    if len(basin[elf_location[0]][elf_location[1]-1]) == 0:
        return True
    else:
        return False


def move_left(elf_location):
    return [elf_location[0], elf_location[1]-1]


def can_move_up(basin, elf_location):
    if elf_location[0]-1 >= 0 and len(basin[elf_location[0]-1][elf_location[1]]) == 0:
        return True
    else:
        return False


def move_up(elf_location):
    return [elf_location[0]-1, elf_location[1]]


def can_move_down(basin, elf_location):
    if elf_location[0]+1 < len(basin) and len(basin[elf_location[0]+1][elf_location[1]]) == 0:
        return True
    else:
        return False


def move_down(elf_location):
    return [elf_location[0]+1, elf_location[1]]


# Load in all possible blizzard states at the beginning of the program
def solve_blizzard_frames(empty_basin):
    num_frames = len(basin)*len(basin[0])
    basins = []
    curr_basin = empty_basin
    print("Loading Blizzards...")
    for _ in range(num_frames):
        basins.append(curr_basin)
        curr_basin = move_blizzards(curr_basin)
    return basins


def search(init_basin, init_elf_location, end_location):
    minutes = 0
    visited = [text(init_basin, init_elf_location)]
    basins = solve_blizzard_frames(init_basin)
    curr_basin = init_basin
    queue = [(init_elf_location, minutes)]
    curr_minutes = minutes
    nodes_checked = 0

    while len(queue) > 0:
        nodes_checked += 1
        print(f"Checking node {nodes_checked}")
        curr_elf_location, curr_minutes = queue.pop(0)
        basin_num = curr_minutes % len(basins)
        curr_basin = basins[basin_num]
        if curr_elf_location == end_location:
            break

        possible_nodes = []
        next_basin = move_blizzards(curr_basin)
        curr_minutes += 1

        if can_stay(next_basin, curr_elf_location):
            possible_nodes.append((next_basin, curr_elf_location, curr_minutes))

        if can_move_right(next_basin, curr_elf_location):
            right_elf = move_right(curr_elf_location)
            possible_nodes.append((next_basin, right_elf, curr_minutes))

        if can_move_down(next_basin, curr_elf_location):
            down_elf = move_down(curr_elf_location)
            possible_nodes.append((next_basin, down_elf, curr_minutes))

        if can_move_left(next_basin, curr_elf_location):
            left_elf = move_left(curr_elf_location)
            possible_nodes.append((next_basin, left_elf, curr_minutes))

        if can_move_up(next_basin, curr_elf_location):
            up_elf = move_up(curr_elf_location)
            possible_nodes.append((next_basin, up_elf, curr_minutes))

        for node in possible_nodes:
            if text(node[0], node[1]) not in visited:
                queue.append((node[1], node[2]))
                visited.append(text(node[0], node[1]))

    return curr_minutes, curr_basin


basin, start_location, end_location = load_file("input.txt")
start_time = time.time()
# Pt1
minutes_1, basin_end = search(basin, start_location, end_location)

# Pt2
minutes_2, basin_restart = search(basin_end, end_location, start_location)
minutes_3, _ = search(basin_restart, start_location, end_location)

exec_time = time.time()-start_time
print(f"\nPart 1 Solution: {minutes_1}")
print(f"Part 2 Solution: {minutes_1+minutes_2+minutes_3}")
print(f"\nSolutions found in {exec_time} seconds")
