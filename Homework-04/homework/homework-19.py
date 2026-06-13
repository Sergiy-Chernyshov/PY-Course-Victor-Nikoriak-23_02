# task1
def with_index(iterable, start=0):

    current_index = start
    for item in iterable:
        yield current_index, item
        current_index += 1

fruits = ['apple', 'banana', 'mango']
print("Список фруктів:")
for index, fruit in with_index(fruits):
    print(f"{index}: {fruit}")

print("\nНумерація символів (старт з 1):")
for i, char in with_index("ABC", start=1):
    print(f"Позиція {i} -> {char}")


gen = with_index(range(1000000), start=10)
print("\nПерший елемент великого генератора:")
print(next(gen))

print ("\n")

#Task2

def in_range(start, end=None, step=1):

    if end is None:
        end = start
        start = 0

    if step == 0:
        raise ValueError("in_range() arg 3 must not be zero")

    current = start

    if step > 0:
        while current < end:
            yield current
            current += step

    else:
        while current > end:
            yield current
            current += step

# Тест

# 1. Один аргумент (0 до 5)
print("in_range(5):", list(in_range(5)))

# 2. Два аргументи (2 до 8)
print("in_range(2, 8):", list(in_range(2, 8)))

# 3. Три аргументи з кроком (1 до 10 з кроком 2)
print("in_range(1, 10, 2):", list(in_range(1, 10, 2)))

# 4. Негативний крок (10 до 0)
print("in_range(10, 0, -2):", list(in_range(10, 0, -2)))

# 5. Перевірка ефективності (нескінченний цикл не створить гігантський список)
for i in in_range(1, 10**12, 10**11):
    print(f"Велике число: {i}")

print ("\n")

# task3

class CustomSequence:
    def __init__(self, data):
        self._data = list(data)

    def __getitem__(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("Індекс поза межами нашої послідовності")
        return self._data[index]

    def __iter__(self):
        """Логіка для циклу for-in"""
        # Найпростіший спосіб зробити об'єкт ітерованим —
        # використати yield, щоб створити генератор
        for item in self._data:
            yield item

    def __len__(self):
        """Дозволяє використовувати len(obj)"""
        return len(self._data)

    def __repr__(self):
        return f"CustomSequence({self._data})"

# Тест

# Створюємо екземпляр нашого класу
my_seq = CustomSequence(['Python', 'Java', 'C++', 'JavaScript'])

# 1. Використання в циклі for-in
print("Перебір у циклі:")
for lang in my_seq:
    print(f" - {lang}")

# 2. Доступ за індексом через []
print(f"\nДругий елемент (індекс 1): {my_seq[1]}")

# 3. Перевірка довжини
print(f"Кількість елементів: {len(my_seq)}")

# 4. Спроба звернутися до неіснуючого індексу
try:
    print(my_seq[10])
except IndexError as e:
    print(f"\nПомилка: {e}")