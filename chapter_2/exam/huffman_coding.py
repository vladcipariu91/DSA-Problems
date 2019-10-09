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


class PriorityQueue(object):

    def __init__(self):
        self.min_heap = []

    def append(self, char_to_count):
        self.min_heap.append(char_to_count)
        heap_size = len(self.min_heap)
        if heap_size == 1:
            return
        else:
            inserted_index = heap_size - 1
            parent_index = (inserted_index - (2 - inserted_index % 2)) // 2
            while self.min_heap[parent_index][1] > self.min_heap[inserted_index][1] and inserted_index != 0:
                self.swap(parent_index, inserted_index)

                inserted_index = parent_index
                parent_index = (inserted_index - (2 - inserted_index % 2)) // 2

    def pop(self):
        if len(self.min_heap) == 0:
            return None

        result = self.min_heap[0]
        self.min_heap[0] = self.min_heap[len(self.min_heap) - 1]
        self.min_heap.pop(len(self.min_heap) - 1)

        current_index = 0
        left_index = 2 * current_index + 1
        right_index = 2 * current_index + 2

        if left_index >= len(self.min_heap) and right_index >= len(self.min_heap):
            return result

        while (left_index < len(self.min_heap) and self.min_heap[current_index][1] > self.min_heap[left_index][1]) or \
                (right_index < len(self.min_heap) and self.min_heap[current_index][1] > self.min_heap[right_index][1]):

            if self.min_heap[current_index][1] > self.min_heap[left_index][1]:
                self.swap(current_index, left_index)

                current_index = left_index
            elif self.min_heap[current_index][1] > self.min_heap[right_index][1]:
                self.swap(current_index, right_index)

                current_index = right_index
            else:
                break

            left_index = 2 * current_index + 1
            right_index = 2 * current_index + 2

            if left_index >= len(self.min_heap) or right_index >= len(self.min_heap):
                break

        return result

    def swap(self, current_index, child_index):
        temp = self.min_heap[current_index]
        self.min_heap[current_index] = self.min_heap[child_index]
        self.min_heap[child_index] = temp

    def __repr__(self):
        return str(self.min_heap)

    def __len__(self):
        return len(self.min_heap)


class HuffmanTree:

    def __init__(self, text):
        self.__p_q = PriorityQueue()
        self.codes_map = {}
        occurrence_map = {}
        for c in text:
            if c in occurrence_map:
                occurrence_map[c] += 1
            else:
                occurrence_map[c] = 1

        for k, v in occurrence_map.items():
            self.__p_q.append((k, v))

        self.root = self.__build()
        self.__generate_codes(self.root, [], 0)

    def __build(self):
        root = None
        while self.__p_q:
            first = self.__p_q.pop()
            second = self.__p_q.pop()

            parent = Node(first[1] + second[1])

            if isinstance(first[0], Node):
                left_child = first[0]
            else:
                left_child = Node(first[0])

            if isinstance(second[0], Node):
                right_child = second[0]
            else:
                right_child = Node(second[0])

            parent.left = left_child
            parent.right = right_child

            if len(self.__p_q) != 0:
                self.__p_q.append((parent, parent.value))
            else:
                root = parent

        return root

    def get_code(self, value):
        if value in self.codes_map:
            return self.codes_map[value]
        else:
            return None

    def __generate_codes(self, node, arr, index):
        if node.left:
            if len(arr) == index:
                arr.append("0")
            else:
                arr[index] = "0"
            self.__generate_codes(node.left, arr, index + 1)

        if node.right:
            if len(arr) == index:
                arr.append("1")
            else:
                arr[index] = "1"
            self.__generate_codes(node.right, arr, index + 1)

        if node.is_leaf():
            code = ""
            for it in arr:
                if it == "":
                    break
                code += it

            self.codes_map[node.value] = code

    def __repr__(self):
        q = Queue()
        root = self.root
        q.enq(root)

        res = str(root) + "\n"
        level_node_count = 2
        current_count = 0
        while q:
            node = q.deq()
            if node.left:
                q.enq(node.left)
                if current_count != 0:
                    if current_count == level_node_count - 1:
                        res += " " + str(node.left)
                    else:
                        res += " " + str(node.left) + " | "
                else:
                    res += str(node.left) + " | "
            else:
                if current_count != 0:
                    if current_count == level_node_count - 1:
                        res += " <empty>"
                    else:
                        res += " <empty> | "
                else:
                    res += "<empty> | "

            current_count += 1

            if node.right:
                q.enq(node.right)
                if current_count != 0:
                    if current_count == level_node_count - 1:
                        res += " " + str(node.right)
                    else:
                        res += " " + str(node.right) + " | "
                else:
                    res += str(node.right) + " | "
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


class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def is_leaf(self):
        return self.left is None and self.right is None

    def __repr__(self):
        return f"Node({self.value})"


# q = PriorityQueue()
# q.append(3)
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(1)
# q.append(1)
# q.append(3)
# print(q)
#
# print(q)

tree = None


def huffman_encoding(data):
    global tree
    tree = HuffmanTree(data)

    code = ""
    for it in data:
        part_code = tree.get_code(it)
        if part_code:
            code += part_code

    return code


def huffman_decoding(data, tree):
    current = tree.root
    result = ""
    for it in data:
        if it == "0":
            current = current.left
        else:
            current = current.right

        if current.is_leaf():
            result += current.value
            current = tree.root

    return result


print(huffman_encoding("this is a test"))
print(huffman_decoding("01111101100010110001011101001111110001", tree))
