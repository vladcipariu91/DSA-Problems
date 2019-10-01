from collections import deque


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here
    can use a for loop (try one or both ways)
    """

    def insert_with_loop(self, new_value):
        new_node = Node(new_value)
        if self.root is None:
            self.root = new_node
            return

        node = self.root

        while node:
            if self.compare(node, new_node) == -1:
                if node.left is None:
                    node.left = new_node
                    node = None
                else:
                    node = node.left
            elif self.compare(node, new_node) == 1:
                if node.right is None:
                    node.right = new_node
                    node = None
                else:
                    node = node.right
            else:
                node = None

    """
    define insert here (can use recursion)
    try one or both ways
    """

    def insert_with_recursion(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        self.insert(self.root, new_node)

    def insert(self, node, new_node):
        if self.compare(node, new_node) == -1:
            if node.left is None:
                node.left = new_node
            else:
                self.insert(node.left, new_node)
        elif self.compare(node, new_node) == 1:
            if node.right is None:
                node.right = new_node
            else:
                self.insert(node.right, new_node)

    def search(self, value):
        return self.search_rec(self.root, value)

    def search_rec(self, node, value):
        if node:
            if node.value == value:
                return True

            if value < node.value:
                return self.search_rec(node.left, value)
            elif value > node.value:
                return self.search_rec(node.right, value)
        else:
            return False

    def delete(self, value):
        self.deleteNode(self.root, value)

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

        # Given a binary search tree and a key, this function

    # delete the key and returns the new root
    def deleteNode(self, root, key):

        # Base Case
        if root is None:
            return root

            # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if key < root.key:
            root.left = self.deleteNode(root.left, key)

            # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif key > root.key:
            root.right = self.deleteNode(root.right, key)

            # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                return temp

            elif root.right is None:
                temp = root.left
                return temp

                # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.key)

        return root

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(7)
tree.insert_with_loop(3)
tree.insert_with_loop(4)
tree.insert_with_loop(10)
tree.insert_with_loop(6)
tree.insert_with_loop(9)
tree.insert_with_loop(8)
tree.insert_with_loop(8.5)
tree.delete(5)
print(tree)
