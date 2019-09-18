class Stack:
    def __init__(self):
        self.arr = [0 for _ in range(10)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):
        if self.next_index == len(self.arr):
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]
        for index, it in enumerate(old_arr):
            self.arr[index] = it

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.next_index -= 1
            self.num_elements -= 1
            return self.arr[self.next_index]


foo = Stack()
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(4)
foo.push(5)
foo.push(6)
foo.push(7)
foo.push(8)
foo.push(9)
foo.push(10) # The array is now at capacity!
foo.push(11) # This one should cause the array to increase in size
print(foo.arr) # Let's see what the array looks like now!
print("Pass" if len(foo.arr) == 20 else "Fail") # If we successfully doubled the array size, it should now be 20.
