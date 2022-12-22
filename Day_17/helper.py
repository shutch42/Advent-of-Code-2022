class Rock:
    def __init__(self, row, col, pts):
        self.row = row
        self.col = col
        self.pts = pts

    def move_down(self):
        self.row -= 1
        for i in range(len(self.pts)):
            self.pts[i][0] -= 1

    def move_left(self):
        self.col -= 1
        for i in range(len(self.pts)):
            self.pts[i][1] -= 1

    def move_right(self):
        self.col += 1
        for i in range(len(self.pts)):
            self.pts[i][1] += 1


class HorizontalLine(Rock):
    def __init__(self, row, col):
        pts = [[row, col],
               [row, col + 1],
               [row, col + 2],
               [row, col + 3]]

        Rock.__init__(self, row, col, pts)


class Plus(Rock):
    def __init__(self, row, col):
        pts = [[row + 1, col],
               [row, col + 1],
               [row + 1, col + 1],
               [row + 2, col + 1],
               [row + 1, col + 2]]

        Rock.__init__(self, row, col, pts)


class RightAngle(Rock):
    def __init__(self, row, col):
        pts = [[row, col],
               [row, col + 1],
               [row, col + 2],
               [row + 1, col + 2],
               [row + 2, col + 2]]

        Rock.__init__(self, row, col, pts)


class VerticalLine(Rock):
    def __init__(self, row, col):
        pts = [[row, col],
               [row + 1, col],
               [row + 2, col],
               [row + 3, col]]

        Rock.__init__(self, row, col, pts)


class Square(Rock):
    def __init__(self, row, col):
        pts = [[row, col],
               [row + 1, col],
               [row, col + 1],
               [row + 1, col + 1]]
        Rock.__init__(self, row, col, pts)