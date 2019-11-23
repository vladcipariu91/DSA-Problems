class Node(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

    def __repr__(self):
        return str(self.value)


class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)


def dfs_recursion_start(start_node):
    print(dfs_recursion(start_node, start_node.value, start_node.value))


def dfs_recursion(node, path_sum, maximum):
    # print("calling node: {} path_sum: {} maximum: {}".format(node, path_sum, maximum))
    if node is None:
        return 0

    for each in node.children:
        maximum = dfs_recursion(each, path_sum + each.value, maximum)
        # print("value {} local max is {}".format(each.value, path_sum + each.value))

    return max(path_sum, maximum)


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node6 = Node(6)
node3 = Node(3)
node8 = Node(8)
node9 = Node(9)

graph = Graph([node0, node1, node2, node3, node6, node8, node9])
graph.add_edge(node0, node1)
graph.add_edge(node0, node2)
graph.add_edge(node1, node6)
graph.add_edge(node1, node3)
graph.add_edge(node2, node9)
graph.add_edge(node3, node8)

dfs_recursion_start(node0)
