class PriorityQueue:

    def __init__(self):
        self.min_heap = []

    def append(self, value):
        self.min_heap.append(value)
        heap_size = len(self.min_heap)
        if heap_size == 1:
            return
        else:
            inserted_index = heap_size - 1
            parent_index = (inserted_index - (2 - inserted_index % 2)) // 2
            while self.min_heap[parent_index] > self.min_heap[inserted_index] and inserted_index != 0:
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

        if left_index >= len(self.min_heap) or right_index >= len(self.min_heap):
            return result

        while self.min_heap[current_index] > self.min_heap[left_index] or \
                self.min_heap[current_index] > self.min_heap[right_index]:

            if self.min_heap[current_index] > self.min_heap[left_index]:
                self.swap(current_index, left_index)

                current_index = left_index
            elif self.min_heap[current_index] > self.min_heap[right_index]:
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


q = PriorityQueue()
q.append(3)
q.append(1)
q.append(2)
q.append(3)
q.append(1)
q.append(1)
q.append(3)
print(q)

print(q)
