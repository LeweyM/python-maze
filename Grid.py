import collections
import random
from heapq import *

from Cell import Cell


def in_bounds(pos, res):
    return 0 <= pos[0] < res and 0 <= pos[1] < res


def index(pos, res):
    return pos[0] + (pos[1] * res)


def visited(pos, visited_set: set):
    return pos in visited_set


class Grid:

    def __init__(self, size, res, screen):
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
                self.grid.append(Cell(screen, x, y, cell_width))

    def finished(self):
        return len(self.grid) == len(self.visited)

    def show(self):
        for cell in self.grid:
            cell.show()

    def show_trail(self):
        for i in self.trail:
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

    class Node:
        def __init__(self, steps, index, parent):
            self.steps = steps
            self.index = index
            self.parent = parent

        def __eq__(self, other):
            return self.index == other.index

        def __lt__(self, other):
            return self.steps < other.steps

        def __le__(self, other):
            return self.steps <= other.steps

        def __gt__(self, other):
            return self.steps > other.steps

        def __ge__(self, other):
            return self.steps >= other.steps

        def __repr__(self):
            return "index:%s steps:%s" % (self.index, self.steps)

    def solve(self):
        root_node = self.Node(0, 0, None)
        node_heap = [root_node]
        visited_nodes = {0}

        while len(node_heap) > 0:
            node = heappop(node_heap)
            if node.index == self.res ** 2 - 1:
                self.collect_trail(node)
                return
            for i in self.open_neighbors(node.index):
                if i not in visited_nodes:
                    next_node = self.Node(node.steps + 1, i, node)
                    heappush(node_heap, next_node)
                    visited_nodes.add(i)

    def walk_to_next_junction(self, i):
        step_counter = 0
        while len(self.open_neighbors(i)) == 1 or i == (self.res ** 2) - 1:
            i = self.open_neighbors(i).pop()
            step_counter += 1
        return i, step_counter

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
