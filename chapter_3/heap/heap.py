# min heap
class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0

    def insert(self, data):
        self.cbt[self.next_index] = data
        self.up_heapify()
        self.next_index += 1

    def up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent = self.cbt[parent_index]
            child = self.cbt[child_index]

            if parent > child:
                self.cbt[parent_index] = child
                self.cbt[child_index] = parent

            child_index = parent_index

    def remove(self):
        if self.size() == 0:
            return None
        else:
            to_remove = self.cbt[0]
            self.swap()
            self.next_index -= 1
            self.down_heapify()

            return to_remove

    def swap(self):
        aux = self.cbt[0]
        self.cbt[0] = self.cbt[self.next_index - 1]
        self.cbt[self.next_index - 1] = aux

    def down_heapify(self):
        current_index = 0
        while current_index < self.next_index:
            current = self.cbt[current_index]
            left = None
            right = None

            left_index = 2 * current_index + 1
            if left_index < self.next_index:
                left = self.cbt[left_index]

            right_index = 2 * current_index + 2
            if right_index < self.next_index:
                right = self.cbt[right_index]

            min_element = current

            if right is not None:
                min_element = min(current, right)

            if left is not None:
                min_element = min(min_element, left)

            if min_element == current:
                return

            if min_element == left:
                self.cbt[current_index] = left
                self.cbt[left_index] = current
                current_index = left_index
            elif min_element == right:
                self.cbt[current_index] = right
                self.cbt[right_index] = current
                current_index = right_index

    def size(self):
        return self.next_index


heap = Heap(10)

heap.insert(10)
print(heap.cbt)

heap.insert(7)
print(heap.cbt)

heap.insert(11)
print(heap.cbt)

heap.insert(5)
print(heap.cbt)

heap.remove()
print(heap.cbt)

heap.remove()
print(heap.cbt)
