class Root:
    def __init__(self):
        self.size = 0
        self.inodes = []

    def add_directory(self, directory):
        self.inodes.append(directory)

    def add_file(self, file):
        self.size += file.size
        self.inodes.append(file)


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.inodes = []

    def add_directory(self, directory):
        self.inodes.append(directory)

    def add_file(self, file):
        self.size += file.size
        curr_node = self.parent

        # Add file size to each parent directory
        while type(curr_node) is not Root:
            curr_node.size += file.size
            curr_node = curr_node.parent

        # Add file size to root
        curr_node.size += file.size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
