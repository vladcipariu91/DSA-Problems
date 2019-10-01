from node import Node
from queue import Queue
from tree import Tree

tree = Tree("apple")

tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))

tree.get_root().get_left_child().set_left_child(Node("dates"))
# tree.get_root().get_left_child().set_right_child(Node("elderberry"))

# tree.get_root().get_right_child().set_left_child(Node("fig"))
# tree.get_root().get_right_child().set_right_child(Node("grape"))


def bfs(tree):
    q = Queue()
    root = tree.get_root()
    q.enq(root)
    visit_order = []

    while q:
        node = q.deq()
        visit_order.append(node.value)
        if node.has_left_child():
            q.enq(node.get_left_child())
        if node.has_right_child():
            q.enq(node.get_right_child())

    print(visit_order)


print(tree)
