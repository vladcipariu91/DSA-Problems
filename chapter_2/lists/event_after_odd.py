class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def even_after_odd(head):
    if head is None:
        return head

    odd = None
    even = None
    even_head = None
    odd_head = None
    current = head

    while current:
        if current.data % 2 == 1:
            if odd is None:
                odd = current
                odd_head = odd
            else:
                odd.next = current
                odd = current
        else:
            if even is None:
                even = current
                even_head = even
            else:
                even.next = current
                even = current

        current = current.next

    if odd_head is None:
        return even_head

    odd.next = even_head
    return odd_head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]

    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 1, 4, 6, 8]
solution = [1, 2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)
