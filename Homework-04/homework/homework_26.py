#Task1

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # елемент не знайдено

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


numbers = [1, 3, 5, 7, 9, 11, 15]
x = 7

result = binary_search_recursive(numbers, x, 0, len(numbers) - 1)
print("Binary Search:")
print("Індекс елемента:", result)

def fibonacci_search(arr, target):
    n = len(arr)

    fib2 = 0   # (m-2)-те число Фібоначчі
    fib1 = 1   # (m-1)-те число Фібоначчі
    fib = fib1 + fib2  # m-те число Фібоначчі

    # шукаємо найменше число Фібоначчі, яке >= n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    while fib > 1:
        i = min(offset + fib2, n - 1)

        if arr[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i

    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1


numbers = [1, 3, 5, 7, 9, 11, 15]
x = 11

result = fibonacci_search(numbers, x)
print("\nFibonacci Search:")
print("Індекс елемента:", result)

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0  # кількість елементів

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # оновлюємо значення
                return

        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    def __contains__(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return True

        return False

    def __len__(self):
        return self.count


# Перевірка
ht = HashTable()

ht.put("apple", 10)
ht.put("banana", 20)
ht.put("orange", 30)

print("\nHashTable:")
print("apple" in ht)     # True
print("grape" in ht)     # False
print(len(ht))           # 3