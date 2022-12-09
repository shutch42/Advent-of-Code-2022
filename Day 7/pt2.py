from filetree import File, Directory, Root

TOTAL_STORAGE = 70000000
SPACE_NEEDED = 30000000

root = Root()
curr_dir = root

# Handle commands and output to create file tree
with open("input.txt") as file:
    for line in file:
        if line[0] == '$':
            # Command entered
            # Break command into tokens
            tokens = line[2:len(line)].strip().split(" ")

            # If the command is cd, navigate to the correct directory
            if tokens[0] == 'cd':
                if tokens[1] == '/':
                    curr_dir = root
                elif tokens[1] == '..':
                    curr_dir = curr_dir.parent
                else:
                    for node in curr_dir.inodes:
                        if type(node) is Directory and node.name == tokens[1]:
                            curr_dir = node
                            break

        else:
            # Handle output from ls
            info = line.strip().split(" ")

            if info[0] == 'dir':
                name = info[1]
                new_dir = Directory(name, curr_dir)
                curr_dir.add_directory(new_dir)
            else:
                size = int(info[0])
                name = info[1]
                file = File(name, size)
                curr_dir.add_file(file)


current_storage = root.size
space_remaining = TOTAL_STORAGE - current_storage
size_to_delete = SPACE_NEEDED - space_remaining


# Search all directories for smallest directory to delete that is capable of freeing enough space
def search_min_size(curr_dir, min_size):
    for node in curr_dir.inodes:
        if type(node) is Directory:
            min_size = search_min_size(node, min_size)

    if size_to_delete < curr_dir.size < min_size:
        return curr_dir.size
    else:
        return min_size


print(search_min_size(root, root.size))
