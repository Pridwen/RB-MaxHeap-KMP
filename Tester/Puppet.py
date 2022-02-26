class MaxHeap:
    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.heap = []
        if arr is not None:
            for root in arr:
                self.push(root)

    @staticmethod
    def get_parent(i):
        return int((i-1)/2)

    @staticmethod
    def get_left_child(i):
        return 2*i+1

    @staticmethod
    def get_right_child(i):
        return 2*i+2

    def has_parent(self, i):
        return self.get_parent(i) >= 0

    def has_left_child(self, i):
        return self.get_left_child(i) < len(self.heap)

    def has_right_child(self, i):
        return self.get_right_child(i) < len(self.heap)

    def push(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap)-1)

    def pop(self):
        if len(self.heap) != 0:
            self.swap(len(self.heap) - 1, 0)
            root = self.heap.pop()
        else:
            root = "\nHeap is empty"
        return root

    def peek(self):
        if len(self.heap) != 0:
            print(self.heap[0])
        else:
            return "\nHeap is empty"

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapifyUp(self, i):
        while self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]:
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)

    def heapifyDown(self, i):
        while self.has_left_child(i):
            max_child = self.get_max_child(i)
            if max_child == -1:
                break
            if self.heap[i] < self.heap[max_child]:
                self.swap(i, max_child)
                i = max_child
            else:
                break

    def get_max_child(self, i):
        if self.has_left_child(i):
            left_child = self.get_left_child(i)
            if self.has_right_child(i):
                right_child = self.get_right_child(i)
                if self.heap[left_child] > self.heap[right_child]:
                    return left_child
                else:
                    return right_child
            else:
                return left_child
        else:
            return -1

    def Heap_Sort(self):
        ordered = MaxHeap()
        while len(self.heap) != 0:
            ordered.push(self.pop())
        ordered.print_heap()

    def print_heap(self):
        print(self.heap)


if __name__ == '__main__':
    array = [43, 97, 55, 3, 126, 14, 8, 1]
    newHeap = MaxHeap(array)
    print("Initial array")
    print(array)
    print("\nMax Heap-ified the array")
    newHeap.print_heap()
    newHeap.push(50)
    print("\nMax Heap after inserting a value")
    newHeap.print_heap()
    print("\nThis is the biggest number in Max Heap before inserting a value bigger than the current Max")
    newHeap.peek()
    print("\nAnd after")
    newHeap.push(200)
    newHeap.peek()
    newHeap.print_heap()
    print("\nNow I revert it by pop-ing the root")
    newHeap.pop()
    newHeap.print_heap()
    print("\nThis is the Heap Sort of the Max Heap")
    newHeap.Heap_Sort()
    print("\nHeap is now empty unlike in the original coding")
    newHeap.push(44)
    newHeap.print_heap()
