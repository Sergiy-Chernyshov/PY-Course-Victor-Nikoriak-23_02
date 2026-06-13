#task1

import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


NUMBERS = [
    2,
    1099726899285419,
    1570341764013157,
    1637027521802551,
    1880450821379411,
    1893530391196711,
    2447109360961063,
    3,
    2772290760589219,
    3033700317376073,
    4350190374376723,
    4350190491008389,
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,
]


def is_prime(number):
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    limit = math.isqrt(number)

    for divisor in range(3, limit + 1, 2):
        if number % divisor == 0:
            return False

    return True


def filter_primes_simple(numbers):
    result = []

    for number in numbers:
        if is_prime(number):
            result.append(number)

    return result


def filter_primes_with_threads(numbers):
    with ThreadPoolExecutor() as executor:
        results = executor.map(is_prime, numbers)

    primes = []

    for number, is_number_prime in zip(numbers, results):
        if is_number_prime:
            primes.append(number)

    return primes


def filter_primes_with_processes(numbers):
    with ProcessPoolExecutor() as executor:
        results = executor.map(is_prime, numbers)

    primes = []

    for number, is_number_prime in zip(numbers, results):
        if is_number_prime:
            primes.append(number)

    return primes


def measure_time(function, numbers):
    start_time = time.perf_counter()

    result = function(numbers)

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return result, execution_time


def main():
    simple_result, simple_time = measure_time(filter_primes_simple, NUMBERS)
    threads_result, threads_time = measure_time(filter_primes_with_threads, NUMBERS)
    processes_result, processes_time = measure_time(filter_primes_with_processes, NUMBERS)

    print("Simple result:")
    print(simple_result)
    print("Time:", simple_time)

    print("\nThreadPoolExecutor result:")
    print(threads_result)
    print("Time:", threads_time)

    print("\nProcessPoolExecutor result:")
    print(processes_result)
    print("Time:", processes_time)

    print("\nAre results equal?")
    print(simple_result == threads_result == processes_result)


if __name__ == "__main__":
    main()