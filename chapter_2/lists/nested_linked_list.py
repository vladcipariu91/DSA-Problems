# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


def merge(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None and list2:
        return list1

    print("__merge({}, {})".format(list1.head, list2.head))
    return LinkedList(__merge_lists(list1.head, list2.head))


def __merge_lists(head1, head2):
    if head1 is None:
        print("returning head2: {}".format(head2))
        return head2
    if head2 is None:
        print("returning head1: {}".format(head1))
        return head1

    if head1.value < head2.value:
        print("__merge({}, {})".format(head1.next, head2))
        head1.next = __merge_lists(head1.next, head2)
        print("returning head1 {} head1.next: {}".format(head1, head1.next))
        return head1
    else:
        print("__merge({}, {})".format(head2.next, head1))
        head2.next = __merge_lists(head2.next, head1)
        print("returning head2: {} head2.next: {}".format(head2, head2.next))
        return head2


class NestedLinkedList(LinkedList):
    def flatten(self):
        node = self.head

        result = None
        while node:
            result = merge(result, node.value)
            node = node.next

        return result


# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)
nested_linked_list = NestedLinkedList(Node(linked_list))

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)
nested_linked_list.append(second_linked_list)

print(nested_linked_list.flatten().to_list())
