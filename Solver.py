from heapq import *


def collect_trail(node):
    trail = []
    while node:
        trail.append(node.index)
        node = node.parent
    return trail


class Solver:
    def __init__(self, grid):
        root_node = Node(0, 0, None)
        self.finished = False
        self.search_head_node = root_node
        self.grid = grid
        self.trail = []
        self.visited_nodes = {0}
        self.node_heap = [root_node]

    def solve(self):
        while self.finished is False:
            self.update()

    def update(self):
        if self.finished:
            return
        if len(self.node_heap) > 0:
            node = heappop(self.node_heap)
            self.trail = collect_trail(node)
            if node.index == self.grid.res ** 2 - 1:
                self.finished = True
                return
            for i in self.grid.open_neighbors(node.index):
                if i not in self.visited_nodes:
                    next_node = Node(node.steps + 1, i, node)
                    heappush(self.node_heap, next_node)
                    self.visited_nodes.add(i)

    def show_visited_nodes(self):
        for i in self.visited_nodes:
            self.grid.grid[i].show_square("blue")

    def show_trail(self):
        for i in self.trail:
            self.grid.grid[i].show_square("red")


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
