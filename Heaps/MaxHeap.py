import copy
from time import sleep


class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        if arr is None:
            pass
        else:
            for root in arr:
                self.push(root)

    @staticmethod
    def get_parent(i):
        return int((i - 1) / 2)

    @staticmethod
    def get_left_child(i):
        return 2 * i + 1

    @staticmethod
    def get_right_child(i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.get_parent(i) >= 0

    def has_left_child(self, i):
        return self.get_left_child(i) < len(self.heap)

    def has_right_child(self, i):
        return self.get_right_child(i) < len(self.heap)

    def push(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) != 0:
            self.swap(len(self.heap) - 1, 0)
            root = self.heap.pop()
            self.heapifyDown(0)
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
        aux = copy.deepcopy(self)
        while len(aux.heap) != 0:
            ordered.push(aux.pop())
        ordered.print_heap()
        del ordered

    def print_heap(self):
        print(self.heap)


def build_array():
    global array
    print("\tType in the numbers and when you're done type STOP")
    try:
        array = []

        while True:
            array.append(int(input()))

    except:
        print("Array created successfully!")
        sleep(3)
        print(array)
        print("\n\n")


def show_heap():
    print("\tCurrent heap:")
    newHeap.print_heap()
    print("\n")


if __name__ == '__main__':
    answer = True
    while answer:
        print("1)\tCreate and show me the array\n"
              "2)\tMax-Heap transformation\n"
              "3)\tShow me the heap\n"
              "4)\tInsert value into heap\n"
              "5)\tDelete max value from heap\n"
              "6)\tShow the biggest value\n"
              "7)\tDo a Heap-Sort on current Max Heap\n"
              "8)\tExit program\n")
        choice = int(input("Choose an option: "))
        if choice == 1:
            build_array()
        elif choice == 2:
            print("\tMax Heap-ified the array")
            newHeap = MaxHeap(array)
            newHeap.print_heap()
            print("\n")
        elif choice == 3:
            show_heap()
        elif choice == 4:
            x = int(input("\tValue to insert: "))
            newHeap.push(x)
            sleep(2)
            print("Successful operation\n")
        elif choice == 5:
            newHeap.pop()
            print("\tRemoving biggest value")
            sleep(2)
            print("Successful operation\n")
        elif choice == 6:
            print("\tFound the max value in the heap: ")
            newHeap.peek()
            print("\n")
        elif choice == 7:
            print("\nThis is the Heap Sort at this step")
            newHeap.Heap_Sort()
            print("\n")
        elif choice == 8:
            print("\tGo to sleep")
            sleep(2)
            print("1 Sheep")
            sleep(2)
            print("2 Sheep")
            sleep(2)
            print("3 Sheep")
            sleep(2)
            print("4 She.. *yawn*")
            sleep(3)
            print("\tGood night, sweet prince")
            answer = False
        else:
            print("\tINVALID choice, try again\n\n")
            sleep(2)
    # print("\nShow me the biggest value")
    # newHeap.peek()
    # print("\nInsert value bigger than the previous one")
    # newHeap.push(333)
    # newHeap.print_heap()
    # print("\nNow I revert it")
    # newHeap.pop()
    # newHeap.print_heap()
    # print("\nThis is the Heap Sort at this step")
    # newHeap.Heap_Sort()
    # print("\nAdd new elements")
    # newHeap.push(33)
    # newHeap.push(201)
    # newHeap.push(15)
    # newHeap.push(14)
    # newHeap.print_heap()
    # print("\nThe new Heap Sort")
    # newHeap.Heap_Sort()
