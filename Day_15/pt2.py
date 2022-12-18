# Note:
# This solution is pretty inefficient in time complexity and can use some improvement
# However, it uses memory reasonably well, it runs, and it will return the correct answer after about a minute

class Pair:
    def __init__(self, sensor, beacon):
        self.sensor = [int(sensor[0]), int(sensor[1])]
        self.beacon = [int(beacon[0]), int(beacon[1])]


pairs = []

# Read all beacons and sensors from file
with open("input.txt") as file:
    for line in file:
        locations = line.strip().split(": ")
        sensor_coordinates = locations[0].split("x=")[1].split(", y=")
        beacon_coordinates = locations[1].split("x=")[1].split(", y=")
        pairs.append(Pair(sensor_coordinates, beacon_coordinates))


# Find coverage for range of rows
min_row = min_x = 0
max_row = max_x = 4000000

for target_row in range(min_row, max_row + 1):
    print(target_row)
    row_range = []
    for pair in pairs:
        sensor_x = pair.sensor[0]
        sensor_y = pair.sensor[1]
        beacon_x = pair.beacon[0]
        beacon_y = pair.beacon[1]

        distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
        middle_row = sensor_y
        if middle_row - distance <= target_row <= middle_row + distance:
            offset = abs(target_row - middle_row)
            row_distance = distance - offset
            row_range.append([max(sensor_x - row_distance, min_x), min(sensor_x + row_distance, max_x)])

    row_range.sort(key=lambda x: x[0])
    i = 0
    while i + 1 < len(row_range):
        elem1 = row_range[i]
        elem2 = row_range[i+1]
        while elem1[1] >= elem2[0] - 1:
            if elem2[1] > elem1[1]:
                elem1 = [elem1[0], elem2[1]]
            row_range.pop(i+1)
            row_range[i] = elem1
            if i+1 < len(row_range):
                elem2 = row_range[i+1]
            else:
                break
        i += 1
    if len(row_range) > 1:
        y = target_row
        x = row_range[1][0]-1
        print(x, y)
        print(x*4000000 + y)
        break
