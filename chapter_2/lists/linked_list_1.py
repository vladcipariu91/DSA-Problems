class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)


def print_nodes(node):
    while node is not None:
        print(node.value)
        node = node.next


def create_linked_list(input_list):
    head = None
    if len(input_list) > 0:
        head = Node(input_list[0])
        current_node = head
        for i in range(1, len(input_list)):
            current_node.next = Node(input_list[i])
            current_node = current_node.next

    return head


def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)
