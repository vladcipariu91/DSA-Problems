def path_from_root_to_node(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    TODO: complete this method and return a list containing values of each node in the path
    from root to the data node
    """
    if root is None:
        return []

    if root.data == data:
        return [data]

    left_arr = path_from_root_to_node(root.left, data)
    right_arr = path_from_root_to_node(root.right, data)

    if len(left_arr) == 0 and len(right_arr) == 0:
        return []
    elif len(left_arr) != 0:
        left_arr.insert(0, root.data)
        return left_arr
    else:
        right_arr.insert(0, root.data)
        return right_arr
