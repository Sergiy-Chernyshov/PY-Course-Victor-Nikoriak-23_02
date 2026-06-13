#Task1

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


text = input("Введіть рядок: ")

stack = Stack()

for char in text:
    stack.push(char)

reversed_text = ""

while not stack.is_empty():
    reversed_text += stack.pop()

print("Результат:", reversed_text)

print("\n")

#task 2
text = input("Введіть рядок: ")

stack = []
balanced = True

for ch in text:
    if ch == "(" or ch == "[" or ch == "{":
        stack.append(ch)
    elif ch == ")" or ch == "]" or ch == "}":
        if len(stack) == 0:
            balanced = False
            break

        last = stack.pop()

        if ch == ")" and last != "(":
            balanced = False
            break
        if ch == "]" and last != "[":
            balanced = False
            break
        if ch == "}" and last != "{":
            balanced = False
            break

if len(stack) != 0:
    balanced = False

if balanced:
    print("Дужки збалансовані")
else:
    print("Дужки не збалансовані")

print("\n")

#Task3

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) == 0:
            raise ValueError("Stack is empty")
        return self.items.pop()

    def get_from_stack(self, e):
        temp = []

        while len(self.items) > 0:
            value = self.items.pop()

            if value == e:
                while len(temp) > 0:
                    self.items.append(temp.pop())
                return value
            else:
                temp.append(value)

        while len(temp) > 0:
            self.items.append(temp.pop())

        raise ValueError(f"Element {e} not found in stack")


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if len(self.items) == 0:
            raise ValueError("Queue is empty")
        return self.items.pop(0)

    def get_from_queue(self, e):
        temp = []
        found = None

        while len(self.items) > 0:
            value = self.items.pop(0)

            if value == e and found is None:
                found = value
            else:
                temp.append(value)

        for value in temp:
            self.items.append(value)

        if found is None:
            raise ValueError(f"Element {e} not found in queue")

        return found


# Перевірка Stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Знайдено у stack:", stack.get_from_stack(20))
print("Stack після пошуку:", stack.items)

# Перевірка Queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("Знайдено у queue:", queue.get_from_queue(30))
print("Queue після пошуку:", queue.items)