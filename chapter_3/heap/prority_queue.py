class PriorityQueue(object):

    def __init__(self):
        self.min_heap = []

    def append(self, node):
        self.min_heap.append(node)
        heap_size = len(self.min_heap)
        if heap_size == 1:
            return
        else:
            inserted_index = heap_size - 1
            parent_index = (inserted_index - (2 - inserted_index % 2)) // 2
            while self.min_heap[parent_index].f > self.min_heap[inserted_index].f and inserted_index != 0:
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

        while (left_index < len(self.min_heap) and self.min_heap[current_index].f > self.min_heap[left_index].f) or \
                (right_index < len(self.min_heap) and self.min_heap[current_index].f > self.min_heap[right_index].f):

            if self.min_heap[current_index].f > self.min_heap[left_index][1]:
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
