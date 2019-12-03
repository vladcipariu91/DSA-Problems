import math
import networkx as nx
import pickle
import plotly.plotly as py
import random
from plotly.graph_objs import *
from plotly.offline import init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)

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


def reconstruct_path(node):
    path = []
    current_node = node
    while current_node:
        path.append(current_node.index)
        current_node = current_node.parent

    return path[::-1]


def shortest_path(M, start, goal):
    start_node = Node(None, M.intersections[start], M.roads[start], start)
    end_node = Node(None, M.intersections[goal], M.roads[goal], goal)

    min_heap = PriorityQueue()
    frontier = {}
    explored = set()

    min_heap.append(start_node)
    frontier[start_node.index] = start_node

    while not min_heap.is_empty():
        current_node = min_heap.pop()

        if current_node.index in frontier:
            del frontier[current_node.index]

        explored.add(current_node.index)

        # goal test
        if current_node == end_node:
            return reconstruct_path(current_node)

        for child_index in current_node.children:
            child_node = Node(current_node, M.intersections[child_index], M.roads[child_index], child_index)

            if child_node.index in explored:
                continue

            child_node.g = current_node.g + calculate_distance(current_node.position, child_node.position)
            child_node.h = calculate_distance(child_node.position, end_node.position)
            child_node.f = child_node.g + child_node.h

            if child_node.index in frontier and child_node.g > frontier[child_node.index].g:
                continue

            min_heap.append(child_node)
            frontier[child_node.index] = child_node

    return None


class PriorityQueue(object):

    def __init__(self):
        self.min_heap = []

    def append(self, node):
        self.min_heap.append(node)
        heap_size = len(self.min_heap)
        if heap_size == 1:
            return
        else:
            inserted_index = heap_size - 1
            parent_index = (inserted_index - (2 - inserted_index % 2)) // 2
            while self.min_heap[parent_index].f > self.min_heap[inserted_index].f and inserted_index != 0:
                self.swap(parent_index, inserted_index)

                inserted_index = parent_index
                parent_index = (inserted_index - (2 - inserted_index % 2)) // 2

    def pop(self):
        if len(self.min_heap) == 0:
            return None

        result = self.min_heap[0]
        self.min_heap[0] = self.min_heap[len(self.min_heap) - 1]
        self.min_heap.pop(len(self.min_heap) - 1)

        current_index = 0
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        if left_index >= len(self.min_heap) and right_index >= len(self.min_heap):
            return result

        while (left_index < len(self.min_heap) and self.min_heap[current_index].f > self.min_heap[left_index].f) or \
                (right_index < len(self.min_heap) and self.min_heap[current_index].f > self.min_heap[right_index].f):

            if self.min_heap[current_index].f > self.min_heap[left_index].f:
                self.swap(current_index, left_index)

                current_index = left_index
            elif self.min_heap[current_index].f > self.min_heap[right_index].f:
                self.swap(current_index, right_index)

                current_index = right_index
            else:
                break

            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2

            if left_index >= len(self.min_heap) or right_index >= len(self.min_heap):
                break

        return result

    def swap(self, current_index, child_index):
        temp = self.min_heap[current_index]
        self.min_heap[current_index] = self.min_heap[child_index]
        self.min_heap[child_index] = temp

    def is_empty(self):
        return len(self.min_heap) == 0

    def __repr__(self):
        return str(self.min_heap)

    def __len__(self):
        return len(self.min_heap)


# MAP_40_ANSWERS = [
#     (5, 34, [5, 16, 37, 12, 34]),
#     (5, 5, [5]),
#     (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
# ]
#
#
# def test(shortest_path_function):
#     map_40 = load_map('map-40.pickle')
#     correct = 0
#     for start, goal, answer_path in MAP_40_ANSWERS:
#         path = shortest_path_function(map_40, start, goal)
#         if path == answer_path:
#             correct += 1
#         else:
#             print("For start:", start,
#                   "Goal:     ", goal,
#                   "Your path:", path,
#                   "Correct:  ", answer_path)
#     if correct == len(MAP_40_ANSWERS):
#         print("All tests pass! Congratulations!")
#     else:
#         print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")
#
#
# class Map:
#     def __init__(self, G):
#         self._graph = G
#         self.intersections = nx.get_node_attributes(G, "pos")
#         self.roads = [list(G[node]) for node in G.nodes()]
#
#     def save(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self._graph, f)
#
#
# def load_map(name):
#     with open(name, 'rb') as f:
#         G = pickle.load(f)
#     return Map(G)
#
#
# def show_map(M, start=None, goal=None, path=None):
#     G = M._graph
#     pos = nx.get_node_attributes(G, 'pos')
#     edge_trace = Scatter(
#         x=[],
#         y=[],
#         line=Line(width=0.5, color='#888'),
#         hoverinfo='none',
#         mode='lines')
#
#     for edge in G.edges():
#         x0, y0 = G.node[edge[0]]['pos']
#         x1, y1 = G.node[edge[1]]['pos']
#         edge_trace['x'] += [x0, x1, None]
#         edge_trace['y'] += [y0, y1, None]
#
#     node_trace = Scatter(
#         x=[],
#         y=[],
#         text=[],
#         mode='markers',
#         hoverinfo='text',
#         marker=Marker(
#             showscale=False,
#             # colorscale options
#             # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
#             # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
#             colorscale='Hot',
#             reversescale=True,
#             color=[],
#             size=10,
#             colorbar=dict(
#                 thickness=15,
#                 title='Node Connections',
#                 xanchor='left',
#                 titleside='right'
#             ),
#             line=dict(width=2)))
#     for node in G.nodes():
#         x, y = G.node[node]['pos']
#         node_trace['x'].append(x)
#         node_trace['y'].append(y)
#
#     for node, adjacencies in enumerate(G.adjacency_list()):
#         color = 0
#         if path and node in path:
#             color = 2
#         if node == start:
#             color = 3
#         elif node == goal:
#             color = 1
#         # node_trace['marker']['color'].append(len(adjacencies))
#         node_trace['marker']['color'].append(color)
#         node_info = "Intersection " + str(node)
#         node_trace['text'].append(node_info)
#
#     fig = Figure(data=Data([edge_trace, node_trace]),
#                  layout=Layout(
#                      title='<br>Network graph made with Python',
#                      titlefont=dict(size=16),
#                      showlegend=False,
#                      hovermode='closest',
#                      margin=dict(b=20, l=5, r=5, t=40),
#
#                      xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
#                      yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))
#
#     iplot(fig)
