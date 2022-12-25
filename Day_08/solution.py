import numpy as np

# This solution has a bit of a different format than previous days.
# All the solutions are stored in methods for the class representing the field of trees
# I think the operations are a little more readable this way, but the code is so much longer
# I probably won't do this again unless there's a clear benefit to using OOP in solving the problem


class Field:
    def __init__(self, filename):
        arr = []
        num_rows = 0
        with open(filename) as file:
            for line in file:
                line = line.strip()
                row = []
                num_rows += 1

                for tree_height in line:
                    row.append(int(tree_height))
                arr.append(row)

        self.num_rows = num_rows
        self.num_cols = len(arr[0])
        self.trees = np.array(arr)

    def _visible_down(self, row, col):
        height = self.trees[row, col]
        for i in range(row+1, self.num_rows):
            if self.trees[i, col] >= height:
                return False

        return True

    def _visible_up(self, row, col):
        height = self.trees[row, col]
        for i in range(0, row):
            if self.trees[i, col] >= height:
                return False

        return True

    def _visible_left(self, row, col):
        height = self.trees[row, col]
        for j in range(0, col):
            if self.trees[row, j] >= height:
                return False

        return True

    def _visible_right(self, row, col):
        height = self.trees[row, col]
        for j in range(col+1, self.num_cols):
            if self.trees[row, j] >= height:
                return False

        return True

    def is_visible(self, row, col):
        return self._visible_up(row, col) or self._visible_down(row, col) or \
            self._visible_left(row, col) or self._visible_right(row, col)

    def num_visible(self):
        visible = self.num_rows*2 + self.num_cols*2 - 4
        for row in range(1, self.num_rows - 1):
            for col in range(1, self.num_cols - 1):
                if self.is_visible(row, col):
                    visible += 1
        return visible

    def view_distance_down(self, row, col):
        height = self.trees[row, col]
        distance = 0
        for i in range(row+1, self.num_rows):
            distance += 1
            if self.trees[i, col] >= height:
                break
        return distance

    def view_distance_up(self, row, col):
        height = self.trees[row, col]
        distance = 0
        for i in range(row-1, -1, -1):
            distance += 1
            if self.trees[i, col] >= height:
                break
        return distance

    def view_distance_left(self, row, col):
        height = self.trees[row, col]
        distance = 0
        for j in range(col-1, -1, -1):
            distance += 1
            if self.trees[row, j] >= height:
                break
        return distance

    def view_distance_right(self, row, col):
        height = self.trees[row, col]
        distance = 0
        for j in range(col+1, self.num_cols):
            distance += 1
            if self.trees[row, j] >= height:
                break
        return distance

    def max_scenic_score(self):
        max_score = 0
        for row in range(1, self.num_rows-1):
            for col in range(1, self.num_cols-1):
                score = self.view_distance_left(row, col) * self.view_distance_right(row, col) * \
                        self.view_distance_up(row, col) * self.view_distance_down(row, col)
                if score > max_score:
                    max_score = score
        return max_score


field = Field("input.txt")

# Pt 1
print(field.num_visible())

# Pt 2
print(field.max_scenic_score())
