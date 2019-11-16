"""
    1. All nodes have a color
    2. All nodes have two children (use NULL nodes)
        All NULL nodes are colored black
    3. If a node is red, its children must be black
    4. The root node must be black (optional)
        We'll go ahead and implement without this for now
    5. Every path to its descendant NULL nodes must contain the same number of black nodes
"""


class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.parent = parent
        self.color = color
        self.left = None
        self.right = None


def grandparent(node):
    if node.parent is None:
        return None
    return node.parent.parent


def parent_sibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp is None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left


class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):
        if node.parent is None:
            return

        if node.parent.color == 'black':
            return

        if parent_sibling(node).color == 'red':
            parent_sibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            self.rebalance(grandparent(node))

        gp = grandparent(node)
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)

        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    def rotate_left(self, node):
        # Save off the parent of the sub-tree we're rotating
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if p is not None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        if p is not None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def search(self, find_val):
        return False
