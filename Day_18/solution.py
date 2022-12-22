import sys

from helper import *

# Load data into dictionary of cube info
with open("input.txt") as file:
    for line in file:
        coordinates = line.strip().split(",")
        x = int(coordinates[0])
        y = int(coordinates[1])
        z = int(coordinates[2])
        point = (x, y, z)
        cube_coverage[point] = deepcopy(empty_dict)
        check_sides(point, cube_coverage)

# Pt1
surface_area = 0
for point in cube_coverage:
    for side in cube_coverage[point]:
        if not cube_coverage[point][side]:
            surface_area += 1
print(surface_area)

# Pt2 - Simulate submerging the object in water to find outer surface area
max_x = max(cube_coverage, key=lambda c: c[0])[0] + 1
min_x = min(cube_coverage, key=lambda c: c[0])[0] - 1
max_y = max(cube_coverage, key=lambda c: c[1])[1] + 1
min_y = min(cube_coverage, key=lambda c: c[1])[1] - 1
max_z = max(cube_coverage, key=lambda c: c[2])[2] + 1
min_z = min(cube_coverage, key=lambda c: c[2])[2] - 1

initial_point = (min_x, min_y, min_z)
water_coverage[initial_point] = deepcopy(empty_dict)

# Python limits the recursion depth to a value too low for the expand_water function
# Therefore, we have to make the depth a bit larger
sys.setrecursionlimit(10000)
expand_water(initial_point, min_x, max_x, min_y, max_y, min_z, max_z)

surface_area = 0
for point in water_coverage:
    # Remove edges on bounds of water area
    if point[0] == min_x:
        water_coverage[point]["left"] = True
    elif point[0] == max_x:
        water_coverage[point]["right"] = True
    if point[1] == min_y:
        water_coverage[point]["back"] = True
    elif point[1] == max_y:
        water_coverage[point]["front"] = True
    if point[2] == min_z:
        water_coverage[point]["bottom"] = True
    elif point[2] == max_z:
        water_coverage[point]["top"] = True

    for side in water_coverage[point]:
        if not water_coverage[point][side]:
            surface_area += 1

print(surface_area)
