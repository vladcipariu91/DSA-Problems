def dfs_recursion_start(self, start_node):
    visited = {}
    self.dfs_recursion(start_node, visited)


def dfs_recursion(self, node, visited):
    if node is None:
        return False

    visited[node.value] = True
    print(node.value)

    for each in node.children:
        if each.value not in visited:
            self.dfs_recursion(each, visited)
