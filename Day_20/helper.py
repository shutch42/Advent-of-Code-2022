items = []


def move(key):
    # Find current item index and value
    item_indices = [item[0] for item in items]
    index = item_indices.index(key)
    value = items[index][1]

    # Remove item from list and calculate next index
    item = items.pop(index)
    next_index = index + value
    next_index %= len(items)

    # Insert item in new position
    items.insert(next_index, item)
