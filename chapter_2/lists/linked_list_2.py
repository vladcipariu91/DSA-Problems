class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next

        print(result)
        return result


linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print("Pass" if (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")
