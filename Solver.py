from heapq import *


class Solver:
    def __init__(self, grid):
        self.trail = []
        self.grid = grid

    def solve(self):
        root_node = Node(0, 0, None)
        node_heap = [root_node]
        visited_nodes = {0}

        while len(node_heap) > 0:
            node = heappop(node_heap)
            if node.index == self.grid.res ** 2 - 1:
                return self.collect_trail(node)
            for i in self.grid.open_neighbors(node.index):
                if i not in visited_nodes:
                    next_node = Node(node.steps + 1, i, node)
                    heappush(node_heap, next_node)
                    visited_nodes.add(i)

    def collect_trail(self, node):
        while node:
            self.trail.append(node.index)
            node = node.parent
        return self.trail


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
