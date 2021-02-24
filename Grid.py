import collections
import random

from Cell import Cell


def in_bounds(pos, res):
    return 0 <= pos[0] < res and 0 <= pos[1] < res


def index(pos, res):
    return pos[0] + (pos[1] * res)


def visited(pos, visited_set: set):
    return pos in visited_set


class Grid:

    def __init__(self, size, res, ui):
        self.trail = []
        self.size = size
        self.res = res
        self.grid = []
        self.visited = {0}
        self.stack = collections.deque()

        self.current = 0
        self.stack.append(0)

        cell_width = size // res

        for y in range(res):
            for x in range(res):
                self.grid.append(Cell(ui, x, y, cell_width))

    def finished(self):
        return len(self.grid) == len(self.visited)

    def show(self):
        for cell in self.grid:
            cell.show()

    def show_trail(self, trail):
        for i in trail:
            self.grid[i].show_red()

    def update(self):
        current_cell = self.grid[self.current]
        neighbors = [pos for pos in current_cell.get_neighbor_indicies()
                     if in_bounds(pos, self.res) and index(pos, self.res) not in self.visited]
        if len(neighbors) > 0:
            next_index = index(random.choice(neighbors), self.res)

            current_cell.open(self.grid[next_index])
            self.visited.add(next_index)
            self.stack.append(next_index)

            self.current = next_index
        elif len(self.stack) > 0:
            self.current = self.stack.popleft()

    def open_neighbors(self, i):
        return [index(j, self.res) for j in self.grid[i].get_neighbor_indicies()
                if in_bounds(j, self.res)
                and self.open_between(i, index(j, self.res))]

    def open_between(self, i, j):
        # i left of j
        if i + 1 == j and self.grid[j].left is False:
            return True
        # i right of j
        if i - 1 == j and self.grid[i].left is False:
            return True
        # i above j
        if i + self.res == j and self.grid[j].top is False:
            return True
        # i below j
        if i - self.res == j and self.grid[i].top is False:
            return True

    def collect_trail(self, node):
        while node:
            self.trail.append(node.index)
            node = node.parent
