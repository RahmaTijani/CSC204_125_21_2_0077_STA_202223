###QUESTION 3
# Implementation of binary search algorithm
def binary_search(arr, end_point):
    arr.sort()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == end_point:
            return mid
        elif arr[mid] < end_point:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Implementing Queue using a single linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating the class Queue
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    # Creating the enqueue method-add an item to the queue
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    # Creating the dequeue method-removing an item from the queue
    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
##Testing
queue=Queue()
queue.enqueue(15)
queue.enqueue(10)
queue.enqueue(25)
queue.enqueue(50)
queue.enqueue(40)
print("The data on the queue")
queue.display() ##output: 15 10 25 50 40

print("Element to dequeue are: ")
dequeued_element=queue.dequeue()
print("Dequeued element: ", dequeued_element)

queue.display()