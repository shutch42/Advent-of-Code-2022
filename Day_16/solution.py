from copy import deepcopy
max_pressure = 0
best_path = None
all_paths = []


class Valve:
    def __init__(self, rate, tunnels):
        self.rate = int(rate)
        self.open = False
        self.tunnels = tunnels
        self.distance = 1000
        self.parent = None


class ValveGraph:
    def __init__(self, filename):
        self.valves = {}
        self.node_distances = {}
        self.curr_valve = "AA"
        self.pressure_active = 0
        self.pressure_released = 0
        with open(filename) as file:
            for line in file:
                [valve_data, tunnel_data] = line.strip().split("; ")
                [valve_name, flow_rate] = valve_data.split(" has flow rate=")
                tunnels = tunnel_data.split(",")
                tunnel_names = []
                for tunnel in tunnels:
                    tunnel_names.append(tunnel[len(tunnel) - 2:len(tunnel)])
                self.valves[valve_name[len(valve_name)-2:len(valve_name)]] = Valve(flow_rate, tunnel_names)

        # Save distance to each node in a dict (of nodes) mapped to another dict (of distances per node)
        for valve in self.valves:
            self._dijkstra(valve)
            self.node_distances[valve] = {}
            for dist_valve in self.valves:
                self.node_distances[valve][dist_valve] = self.valves[dist_valve].distance

    def _dijkstra(self, src):
        # Find the distance from a source node to every other node in the graph
        queue = []

        for valve in self.valves:
            self.valves[valve].distance = 1000
            self.valves[valve].parent = None
            if valve != src:
                queue.append(self.valves[valve])

        self.valves[src].distance = 0
        queue.insert(0, self.valves[src])

        while len(queue) > 0:
            u = queue.pop(queue.index(min(queue, key=lambda x: x.distance)))
            for v in u.tunnels:
                tmp_key = u.distance + 1
                if tmp_key < self.valves[v].distance:
                    self.valves[v].distance = tmp_key
                    self.valves[v].parent = u

    def move_options(self):
        # Find usable options in current state
        # Filter out valves with 0 rate, and previously opened valves
        options = []
        for node in self.valves:
            if self.valves[node].rate != 0 and node != self.curr_valve and not self.valves[node].open:
                options.append(node)

        return options


def search(valves, steps, path):
    # DFS of all viable moves in graph
    # Tracks maximum pressure up to 30 steps (for pt1)
    # Records all paths up to 26 steps (for pt2)
    global max_pressure
    global best_path
    options = valves.move_options()
    if steps <= 26:
        all_paths.append(path)
    if len(options) > 0:
        for i, option in enumerate(options):
            if len(path) == 1:
                print(f"checking branch {i+1}")
            # steps_to_option = valves.valves[option].distance
            steps_to_option = valves.node_distances[valves.curr_valve][option]
            next_steps = steps + steps_to_option + 1
            if next_steps > 30:
                if valves.pressure_released > max_pressure:
                    max_pressure = valves.pressure_released
                    best_path = path

            else:
                next_valves = deepcopy(valves)
                next_path = deepcopy(path)
                next_valves.curr_valve = option
                next_valves.valves[valves.curr_valve].open = True
                next_valves.pressure_released += next_valves.valves[option].rate * (30 - next_steps)
                next_path.append((option, next_steps))
                search(next_valves, next_steps, next_path)
    else:
        if valves.pressure_released > max_pressure:
            max_pressure = valves.pressure_released
            best_path = path

    return max_pressure


graph = ValveGraph("input.txt")
option_count = len(graph.move_options())

# Part 1
print(search(graph, 0, [("AA", 0)]))
print(best_path)
print("Press enter to continue")
input()

# Part 2
max_pressure_pt2 = 0
best_path_pt2 = 0
num_paths = len(all_paths)
for i, path_1 in enumerate(all_paths):
    print(f"checking path {i} out of {num_paths}")
    if len(path_1) == 1:
        continue
    for path_2 in all_paths:
        if len(path_2) == 1:
            continue
        overlap = False
        for item_1 in path_1:
            if item_1[0] != 'AA':
                for item_2 in path_2:
                    if item_1[0] == item_2[0]:
                        overlap = True
                        break
            if overlap:
                break
        if overlap:
            continue
        else:
            path_1_score = 0
            for item in path_1:
                path_1_score += graph.valves[item[0]].rate * (26 - item[1])
            path_2_score = 0
            for item in path_2:
                path_2_score += graph.valves[item[0]].rate * (26 - item[1])
            total_score = path_1_score + path_2_score
            if total_score > max_pressure_pt2:
                max_pressure_pt2 = total_score
                best_path_pt2 = (path_1, path_2)

print(max_pressure_pt2)
print(best_path_pt2)
