import math


# Run this cell first!

class Node():
    def __init__(self, parent, position, children, index):
        self.parent = parent
        self.position = position
        self.children = children
        self.index = index

        self.g = 0
        self.f = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position


def calculate_distance(point_1, point_2):
    return math.sqrt((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2)


def shortest_path(M, start, goal):
    start_node = Node(None, M.intersections[start], M.roads[start], start)
    end_node = Node(None, M.intersections[goal], M.roads[goal], goal)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current:
                path.append(current.index)
                current = current.parent

            return path[::-1]

        for child_index in current_node.children:
            child_node = Node(current_node, M.intersections[child_index], M.roads[child_index], child_index)
            child_node.g = current_node.g + calculate_distance(current_node.position, child_node.position)
            child_node.h = calculate_distance(child_node.position, end_node.position)
            child_node.f = child_node.g + child_node.h

            for open_node in open_list:
                if child_node == open_node and child_node.g > open_node.g:
                    continue

            open_list.append(child_node)

    return None
