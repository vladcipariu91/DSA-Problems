from queue import Queue

from node import Node


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def __repr__(self):
        q = Queue()
        root = self.get_root()
        q.enq(root)

        res = str(root) + "\n"
        level_node_count = 2
        current_count = 0
        while q:
            node = q.deq()
            if node.has_left_child():
                q.enq(node.get_left_child())
                if current_count != 0:
                    if current_count == level_node_count - 1:
                        res += " " + str(node.get_left_child())
                    else:
                        res += " " + str(node.get_left_child()) + " | "
                else:
                    res += str(node.get_left_child()) + " | "
            else:
                if current_count != 0:
                    if current_count == level_node_count - 1:
                        res += " <empty>"
                    else:
                        res += " <empty> | "
                else:
                    res += "<empty> | "

            current_count += 1

            if node.has_right_child():
                q.enq(node.get_right_child())
                if current_count != 0:
                    if current_count == level_node_count - 1:
                        res += " " + str(node.get_right_child())
                    else:
                        res += " " + str(node.get_right_child()) + " | "
                else:
                    res += str(node.get_right_child()) + " | "
            else:
                if current_count != 0:
                    if current_count == level_node_count - 1:
                        res += " <empty>"
                    else:
                        res += " <empty> | "
                else:
                    res += "<empty> | "

            current_count += 1

            if current_count == level_node_count:
                level_node_count *= 2
                current_count = 0
                res += "\n"

        return res
