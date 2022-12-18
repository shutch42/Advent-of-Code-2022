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


# Find coverage for target row
target_row = 2000000
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
        distance -= offset
        row_range.append([sensor_x - distance, sensor_x + distance])


# Find union of coverage ranges for row
row_range.sort(key=lambda x: x[0])
print(row_range)
i = 0
while i < len(row_range):
    elem1 = row_range[i]
    elem2 = row_range[i+1]
    while elem1[1] >= elem2[0]:
        if elem2[1] > elem1[1]:
            elem1 = [elem1[0], elem2[1]]
        row_range.pop(i+1)
        row_range[i] = elem1
        if i+1 < len(row_range):
            elem2 = row_range[i+1]
        else:
            break
    i += 1

# Calculate sum of range areas
coverage = 0
for bounds in row_range:
    coverage += bounds[1] - bounds[0]
print(coverage)


