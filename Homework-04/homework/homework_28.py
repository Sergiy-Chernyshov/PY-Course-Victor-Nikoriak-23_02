#task1

def cocktail_sort(arr):

    left = 0
    right = len(arr) - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        right -= 1

        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        left += 1

    return arr


numbers = [5, 1, 4, 2, 8, 0, 2]
print("До сортування:", numbers)

sorted_numbers = cocktail_sort(numbers.copy())
print("Після сортування:", sorted_numbers)

print("\n")

# Task2

def merge(arr, left, mid, right):

    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    k = 0
    idx = left
    while idx <= right:
        arr[idx] = temp[k]
        idx += 1
        k += 1


def merge_sort_recursive(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort_recursive(arr, left, mid)
    merge_sort_recursive(arr, mid + 1, right)

    merge(arr, left, mid, right)


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    merge_sort_recursive(arr, 0, len(arr) - 1)
    return arr


numbers = [38, 27, 43, 3, 9, 82, 10]
print("До сортування:", numbers)

mergeSort(numbers)

print("Після сортування:", numbers)

print("\n")

#Task3

import random
import time


def insertion_sort_range(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_hybrid(arr, low, high, partition_limit):
    while low < high:
        if high - low + 1 <= partition_limit:
            insertion_sort_range(arr, low, high)
            return

        p = partition(arr, low, high)

        if p - low < high - p:
            quicksort_hybrid(arr, low, p - 1, partition_limit)
            low = p + 1
        else:
            quicksort_hybrid(arr, p + 1, high, partition_limit)
            high = p - 1


def sort_with_limit(data, partition_limit):
    arr = data.copy()
    if len(arr) > 1:
        quicksort_hybrid(arr, 0, len(arr) - 1, partition_limit)
    return arr


def benchmark():
    random.seed(42)

    list_sizes = [1000, 5000, 10000]
    limits = [0, 5, 10, 20, 30, 50]  # 0 = майже "чистий" quicksort
    repeats = 5

    print("=== Аналіз швидкості (секунди, менше = краще) ===")
    print(f"{'N':>8} {'limit':>8} {'avg_time':>12}")

    for n in list_sizes:
        base = [random.randint(-100000, 100000) for _ in range(n)]

        for limit in limits:
            total = 0.0

            for _ in range(repeats):
                start = time.perf_counter()
                result = sort_with_limit(base, limit)
                end = time.perf_counter()
                total += (end - start)

                if result != sorted(base):
                    print("Помилка сортування!")
                    return

            avg_time = total / repeats
            print(f"{n:>8} {limit:>8} {avg_time:>12.6f}")

        print("-" * 32)


def demo_random_sort():
    numbers = [random.randint(0, 99) for _ in range(20)]
    print("Випадковий список:", numbers)

    limit = 20
    sorted_numbers = sort_with_limit(numbers, limit)

    print(f"Відсортовано (partition_limit={limit}):", sorted_numbers)


if __name__ == "__main__":
    demo_random_sort()
    print()
    benchmark()