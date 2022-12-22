from copy import deepcopy
cube_coverage = {}
water_coverage = {}
empty_dict = {"top": False,
              "bottom": False,
              "front": False,
              "back": False,
              "left": False,
              "right": False}


def check_sides(point, coverage):
    x = point[0]
    y = point[1]
    z = point[2]

    point_right = (x + 1, y, z)
    if point_right in coverage:
        coverage[point]["right"] = True
        coverage[point_right]["left"] = True

    point_left = (x - 1, y, z)
    if point_left in coverage:
        coverage[point]["left"] = True
        coverage[point_left]["right"] = True

    point_front = (x, y + 1, z)
    if point_front in coverage:
        coverage[point]["front"] = True
        coverage[point_front]["back"] = True

    point_back = (x, y - 1, z)
    if point_back in coverage:
        coverage[point]["back"] = True
        coverage[point_back]["front"] = True

    point_top = (x, y, z + 1)
    if point_top in coverage:
        coverage[point]["top"] = True
        coverage[point_top]["bottom"] = True

    point_bottom = (x, y, z - 1)
    if point_bottom in coverage:
        coverage[point]["bottom"] = True
        coverage[point_bottom]["top"] = True


def expand_water(point, min_x, max_x, min_y, max_y, min_z, max_z):
    x = point[0]
    y = point[1]
    z = point[2]

    if x+1 <= max_x:
        point_right = (x + 1, y, z)
        if point_right not in cube_coverage and point_right not in water_coverage:
            water_coverage[point_right] = deepcopy(empty_dict)
            check_sides(point, water_coverage)
            check_sides(point_right, water_coverage)
            expand_water(point_right, min_x, max_x, min_y, max_y, min_z, max_z)

    if x-1 >= min_x:
        point_left = (x - 1, y, z)
        if point_left not in cube_coverage and point_left not in water_coverage:
            water_coverage[point_left] = deepcopy(empty_dict)
            check_sides(point, water_coverage)
            check_sides(point_left, water_coverage)
            expand_water(point_left, min_x, max_x, min_y, max_y, min_z, max_z)

    if y+1 <= max_y:
        point_front = (x, y + 1, z)
        if point_front not in cube_coverage and point_front not in water_coverage:
            water_coverage[point_front] = deepcopy(empty_dict)
            check_sides(point, water_coverage)
            check_sides(point_front, water_coverage)
            expand_water(point_front, min_x, max_x, min_y, max_y, min_z, max_z)

    if y-1 >= min_y:
        point_back = (x, y - 1, z)
        if point_back not in cube_coverage and point_back not in water_coverage:
            water_coverage[point_back] = deepcopy(empty_dict)
            check_sides(point, water_coverage)
            check_sides(point_back, water_coverage)
            expand_water(point_back, min_x, max_x, min_y, max_y, min_z, max_z)

    if z+1 <= max_z:
        point_top = (x, y, z + 1)
        if point_top not in cube_coverage and point_top not in water_coverage:
            water_coverage[point_top] = deepcopy(empty_dict)
            check_sides(point, water_coverage)
            check_sides(point_top, water_coverage)
            expand_water(point_top, min_x, max_x, min_y, max_y, min_z, max_z)

    if z-1 >= min_z:
        point_bottom = (x, y, z - 1)
        if point_bottom not in cube_coverage and point_bottom not in water_coverage:
            water_coverage[point_bottom] = deepcopy(empty_dict)
            check_sides(point, water_coverage)
            check_sides(point_bottom, water_coverage)
            expand_water(point_bottom, min_x, max_x, min_y, max_y, min_z, max_z)
