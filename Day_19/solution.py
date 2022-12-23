from copy import deepcopy
blueprints = []

with open("input.txt") as file:
    for i, line in enumerate(file):
        blueprints.append({})
        sections = line.strip().split(': ')[1].split('. ')
        ore_robot = sections[0]
        blueprints[i]['ore robot'] = {'ore': int(ore_robot.split('costs ')[1].split(' ore')[0])}
        clay_robot = sections[1]
        blueprints[i]['clay robot'] = {'ore': int(clay_robot.split('costs ')[1].split(' ore')[0])}
        obsidian_robot = sections[2]
        blueprints[i]['obsidian robot'] = {'ore': int(obsidian_robot.split('costs ')[1].split(' ore')[0]),
                                           'clay': int(obsidian_robot.split('and ')[1].split(' clay')[0])}
        geode_robot = sections[3]
        blueprints[i]['geode robot'] = {'ore': int(geode_robot.split('costs ')[1].split(' ore')[0]),
                                        'obsidian': int(geode_robot.split('and ')[1].split(' obsidian')[0])}


def search(blueprint, max_depth):
    init_bots = {'ore': 1,
                 'clay': 0,
                 'obsidian': 0,
                 'geode': 0}
    init_materials = {'ore': 0,
                      'clay': 0,
                      'obsidian': 0,
                      'geode': 0}
    max_geodes_recorded = 0
    max_path = []

    max_ore = 0
    max_clay = 0
    max_obsidian = 0
    for bot in blueprint:
        if blueprint[bot]['ore'] > max_ore:
            max_ore = blueprint[bot]['ore']
        if 'clay' in blueprint[bot] and blueprint[bot]['clay'] > max_clay:
            max_clay = blueprint[bot]['clay']
        if 'obsidian' in blueprint[bot] and blueprint[bot]['obsidian'] > max_obsidian:
            max_obsidian = blueprint[bot]['obsidian']

    states = {}

    ###############################
    # Helper functions start here #
    ###############################
    def add_material_step(bots, materials):
        for bot in bots:
            materials[bot] += bots[bot]

    def can_add_ore_bot(materials):
        ore_required = blueprint['ore robot']['ore']
        return ore_required <= materials['ore']

    def add_ore_bot(bots, materials, path):
        ore_required = blueprint['ore robot']['ore']
        materials['ore'] -= ore_required
        bots['ore'] += 1
        path.append(("Add ore bot", bots, materials))

    def can_add_clay_bot(materials):
        ore_required = blueprint['clay robot']['ore']
        return ore_required <= materials['ore']

    def add_clay_bot(bots, materials, path):
        ore_required = blueprint['clay robot']['ore']
        materials['ore'] -= ore_required
        bots['clay'] += 1
        path.append(("Add clay bot", bots, materials))

    def can_add_obsidian_bot(materials):
        ore_required = blueprint['obsidian robot']['ore']
        clay_required = blueprint['obsidian robot']['clay']
        return ore_required <= materials['ore'] and clay_required <= materials['clay']

    def add_obsidian_bot(bots, materials, path):
        ore_required = blueprint['obsidian robot']['ore']
        clay_required = blueprint['obsidian robot']['clay']
        materials['ore'] -= ore_required
        materials['clay'] -= clay_required
        bots['obsidian'] += 1
        path.append(("Add obsidian bot", bots, materials))

    def can_add_geode_bot(materials):
        ore_required = blueprint['geode robot']['ore']
        obsidian_required = blueprint['geode robot']['obsidian']
        return ore_required <= materials['ore'] and obsidian_required <= materials['obsidian']

    def add_geode_bot(bots, materials, path):
        ore_required = blueprint['geode robot']['ore']
        obsidian_required = blueprint['geode robot']['obsidian']
        materials['ore'] -= ore_required
        materials['obsidian'] -= obsidian_required
        bots['geode'] += 1
        path.append(("Add geode bot", bots, materials))

    def check_state(depth, bots, materials):
        bots_tuple = (bots['ore'], bots['clay'], bots['obsidian'], bots['geode'])
        if depth in states:
            if bots_tuple in states[depth]:
                compare_materials = states[depth][bots_tuple]
                greater_than = False
                less_than = False
                for material in compare_materials:
                    if materials[material] < compare_materials[material]:
                        less_than = True
                    elif materials[material] > compare_materials[material]:
                        greater_than = True
                if less_than and not greater_than:
                    return False
                else:
                    states[depth][bots_tuple] = materials
                    return True
            else:
                states[depth][bots_tuple] = materials
                return True
        else:
            states[depth] = {bots_tuple: materials}
            return True

    def search_helper(depth, bots, materials, path):
        nonlocal max_geodes_recorded
        nonlocal max_depth
        nonlocal max_path

        if depth == max_depth:
            if materials['geode'] > max_geodes_recorded:
                max_geodes_recorded = materials['geode']
                max_path = path
            return

        # Check if more materials have been reached using the same number of bots
        if not check_state(depth, bots, materials):
            return

        # Check option for making another geode bot (always add if possible)
        if can_add_geode_bot(materials):
            new_path, copy_bot_geode, copy_materials_geode = deepcopy(path), deepcopy(bots), deepcopy(materials)
            add_material_step(copy_bot_geode, copy_materials_geode)
            add_geode_bot(copy_bot_geode, copy_materials_geode, new_path)
            search_helper(depth + 1, copy_bot_geode, copy_materials_geode, new_path)
            del new_path, copy_bot_geode, copy_materials_geode
        else:
            # Check option for making another ore bot
            if bots['ore'] < max_ore and can_add_ore_bot(materials):
                new_path, copy_bot_ore, copy_materials_ore = deepcopy(path), deepcopy(bots), deepcopy(materials)
                add_material_step(copy_bot_ore, copy_materials_ore)
                add_ore_bot(copy_bot_ore, copy_materials_ore, new_path)
                search_helper(depth+1, copy_bot_ore, copy_materials_ore, new_path)
                del new_path, copy_bot_ore, copy_materials_ore

            # Check option for making another clay bot
            if bots['clay'] < max_clay and can_add_clay_bot(materials):
                new_path, copy_bot_clay, copy_materials_clay = deepcopy(path), deepcopy(bots), deepcopy(materials)
                add_material_step(copy_bot_clay, copy_materials_clay)
                add_clay_bot(copy_bot_clay, copy_materials_clay, new_path)
                search_helper(depth+1, copy_bot_clay, copy_materials_clay, new_path)
                del new_path, copy_bot_clay, copy_materials_clay

            # Check option for making another obsidian bot
            if bots['obsidian'] < max_obsidian and can_add_obsidian_bot(materials):
                new_path, copy_bot_obsidian, copy_materials_obsidian = \
                    deepcopy(path), deepcopy(bots), deepcopy(materials)
                add_material_step(copy_bot_obsidian, copy_materials_obsidian)
                add_obsidian_bot(copy_bot_obsidian, copy_materials_obsidian, new_path)
                search_helper(depth+1, copy_bot_obsidian, copy_materials_obsidian, new_path)
                del new_path, copy_bot_obsidian, copy_materials_obsidian

            # Check option for no new bots made
            if materials['ore'] < max_ore or materials['clay'] < max_clay or materials['obsidian'] < max_obsidian:
                new_path, copy_bots, copy_materials = deepcopy(path), deepcopy(bots), deepcopy(materials)
                add_material_step(copy_bots, copy_materials)
                new_path.append(("No new bot", copy_bots, copy_materials))
                search_helper(depth+1, copy_bots, copy_materials, new_path)
                del new_path, copy_bots, copy_materials

    # Call the helper function to complete the search
    search_helper(0, init_bots, init_materials, [])
    return max_geodes_recorded, max_path


# Part 1
quality_sum = 0
for i, blueprint in enumerate(blueprints):
    print(f"Checking blueprint {i+1}")
    geodes, path = search(blueprint, 24)
    quality_level = geodes*(i+1)
    quality_sum += quality_level

print(f"Sum of quality levels: {quality_sum}")


# Part 2
product_geodes = 1
for i, blueprint in enumerate(blueprints[:3]):
    print(f"Searching blueprint {i+1}")
    geodes, path = search(blueprint, 32)
    product_geodes *= geodes

print(f"Product of geodes found: {product_geodes}")
