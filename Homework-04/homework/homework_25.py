#task1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnsortedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        count = 0
        current = self.head

        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head

        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next

        if not found:
            raise ValueError("Item not found")

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def append(self, item):
        temp = Node(item)

        if self.head is None:
            self.head = temp
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = temp

    def index(self, item):
        current = self.head
        position = 0

        while current is not None:
            if current.data == item:
                return position
            current = current.next
            position = position + 1

        raise ValueError("Item not found")

    def pop(self, pos=None):
        if self.head is None:
            raise IndexError("Pop from empty list")

        if pos is None:
            pos = self.size() - 1

        if pos < 0 or pos >= self.size():
            raise IndexError("Index out of range")

        current = self.head
        previous = None
        count = 0

        while count < pos:
            previous = current
            current = current.next
            count = count + 1

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        return current.data

    def insert(self, pos, item):
        if pos < 0 or pos > self.size():
            raise IndexError("Index out of range")

        temp = Node(item)

        if pos == 0:
            temp.next = self.head
            self.head = temp
            return

        current = self.head
        previous = None
        count = 0

        while count < pos:
            previous = current
            current = current.next
            count = count + 1

        temp.next = current
        previous.next = temp

    def slice(self, start, stop):
        if start < 0 or stop < 0 or start > stop or stop > self.size():
            raise IndexError("Invalid slice indexes")

        new_list = UnsortedList()
        current = self.head
        position = 0

        while current is not None:
            if position >= start and position < stop:
                new_list.append(current.data)

            current = current.next
            position = position + 1

        return new_list

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Перевірка
my_list = UnsortedList()

my_list.add(30)
my_list.add(20)
my_list.add(10)

print("Початковий список:")
my_list.print_list()

my_list.append(40)
print("Після append(40):")
my_list.print_list()

print("Індекс числа 20:", my_list.index(20))

my_list.insert(2, 25)
print("Після insert(2, 25):")
my_list.print_list()

print("pop():", my_list.pop())
print("Після pop():")
my_list.print_list()

print("pop(1):", my_list.pop(1))
print("Після pop(1):")
my_list.print_list()

new_list = my_list.slice(0, 2)
print("slice(0, 2):")
new_list.print_list()

print("\n")

#Task2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        removed_item = self.top.data
        self.top = self.top.next
        return removed_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.top.data

    def size(self):
        count = 0
        current = self.top

        while current is not None:
            count = count + 1
            current = current.next

        return count

    def display(self):
        current = self.top

        while current is not None:
            print(current.data)
            current = current.next


# Перевірка
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Верхній елемент:", stack.peek())
print("Розмір стеку:", stack.size())

print("Елементи стеку:")
stack.display()

print("Видалений елемент:", stack.pop())
print("Після видалення:")

stack.display()

print("\n")

#Task3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        removed_item = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.front.data

    def size(self):
        count = 0
        current = self.front

        while current is not None:
            count = count + 1
            current = current.next

        return count

    def display(self):
        current = self.front

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Перевірка
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Перший елемент:", queue.peek())
print("Розмір черги:", queue.size())

print("Елементи черги:")
queue.display()

print("Видалений елемент:", queue.dequeue())
print("Після видалення:")
queue.display()
