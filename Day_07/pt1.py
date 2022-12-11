from filetree import File, Directory, Root

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


# Search all directories
# Add together directories under size 100000
def search_size(curr_dir):
    size = 0
    for node in curr_dir.inodes:
        if type(node) is Directory:
            size += search_size(node)

    if curr_dir.size < 100000:
        return curr_dir.size + size
    else:
        return size


print(search_size(root))
