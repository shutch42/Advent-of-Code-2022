current_positions = []
positions_considered = []
directions = ['N', 'S', 'W', 'E']


def empty_positions(positions):
    max_row = max(positions, key=lambda x: x[0])[0]
    max_col = max(positions, key=lambda x: x[1])[1]
    min_row = min(positions, key=lambda x: x[0])[0]
    min_col = min(positions, key=lambda x: x[1])[1]

    total_area = (max_row - min_row + 1) * (max_col - min_col + 1)
    return total_area - len(positions)


def print_positions(positions):
    max_row = max(positions, key=lambda x: x[0])[0]
    max_col = max(positions, key=lambda x: x[1])[1]
    min_row = min(positions, key=lambda x: x[0])[0]
    min_col = min(positions, key=lambda x: x[1])[1]

    for i in range(min_row, max_row+1):
        for j in range(min_col, max_col+1):
            if (i, j) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


with open("input.txt") as file:
    for row, line in enumerate(file):
        for col, char in enumerate(line):
            if char == '#':
                current_positions.append((row, col))
                positions_considered.append((row, col))

for _ in range(10):
    for i, position in enumerate(current_positions):
        row = position[0]
        col = position[1]
        N = (row-1, col)
        NE = (row-1, col+1)
        NW = (row-1, col-1)
        E = (row, col+1)
        W = (row, col-1)
        S = (row+1, col)
        SE = (row+1, col+1)
        SW = (row+1, col-1)
        surrounding_positions = [N, NE, NW, E, W, S, SE, SW]
        positions_taken = [position in current_positions for position in surrounding_positions]
        if positions_taken.count(True) == 0:
            # No surrounding positions taken, no need to move
            positions_considered[i] = position
        else:
            # Check directions for next move
            north_available = [position in current_positions for position in [N, NE, NW]].count(True) == 0
            south_available = [position in current_positions for position in [S, SE, SW]].count(True) == 0
            east_available = [position in current_positions for position in [E, NE, SE]].count(True) == 0
            west_available = [position in current_positions for position in [W, NW, SW]].count(True) == 0

            # If no directions work, don't move
            positions_considered[i] = position

            # Check directions in order of turn
            for direction in directions:
                if direction == 'N' and north_available:
                    positions_considered[i] = N
                    break
                elif direction == 'S' and south_available:
                    positions_considered[i] = S
                    break
                elif direction == 'W' and west_available:
                    positions_considered[i] = W
                    break
                elif direction == 'E' and east_available:
                    positions_considered[i] = E
                    break

    for i, position in enumerate(positions_considered):
        if positions_considered.count(position) == 1:
            current_positions[i] = positions_considered[i]

    directions.append(directions.pop(0))

    print_positions(current_positions)

print(empty_positions(current_positions))
