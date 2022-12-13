def move_up(position, height_map):
    curr_row = position[0]
    curr_col = position[1]
    if curr_row - 1 >= 0 and height_map[curr_row][curr_col] + 1 >= height_map[curr_row - 1][curr_col]:
        return curr_row - 1, curr_col
    else:
        return None


def move_down(position, height_map):
    curr_row = position[0]
    curr_col = position[1]
    if curr_row + 1 < len(height_map) and height_map[curr_row][curr_col] + 1 >= height_map[curr_row + 1][curr_col]:
        return curr_row + 1, curr_col
    else:
        return None


def move_left(position, height_map):
    curr_row = position[0]
    curr_col = position[1]
    if curr_col - 1 >= 0 and height_map[curr_row][curr_col] + 1 >= height_map[curr_row][curr_col - 1]:
        return curr_row, curr_col - 1
    else:
        return None


def move_right(position, height_map):
    curr_row = position[0]
    curr_col = position[1]
    if curr_col + 1 < len(height_map[0]) and height_map[curr_row][curr_col] + 1 >= height_map[curr_row][curr_col + 1]:
        return curr_row, curr_col + 1
    else:
        return None


def get_path(initial_node, target_node, height_map):
    # Apply breadth-first search to get the shortest path
    visited = [initial_node]
    queue = [initial_node]
    parent_map = {}
    found = False

    while len(queue) > 0:
        curr_node = queue.pop(0)
        if curr_node == target_node:
            found = True
            break

        possible_nodes = [move_up(curr_node, height_map), move_down(curr_node, height_map),
                          move_left(curr_node, height_map), move_right(curr_node, height_map)]
        for next_node in possible_nodes:
            if next_node is not None and next_node not in visited:
                queue.append(next_node)
                parent_map[next_node] = curr_node
                visited.append(next_node)

    curr_node = target_node
    path = [curr_node]
    if found:
        while curr_node in parent_map:
            curr_node = parent_map[curr_node]
            path.append(curr_node)
    path.reverse()

    return path


def print_path(initial_node, target_node, height_map):
    path = get_path(initial_node, target_node, height_map)
    line = ""
    for i, row in enumerate(height_map):
        for j, height in enumerate(row):
            if height == 1.5:
                letter = "S"
            elif height == 25.5:
                letter = "E"
            else:
                letter = chr(height + 96)

            if (i, j) in path:
                line += f"\x1b[0;32;40m{letter}\x1b[0m"
            else:
                line += f"{letter}"
        print(line)
        line = ""
