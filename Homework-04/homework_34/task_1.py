# Task1

from threading import Thread


counter = 0
rounds = 100_000


class Counter(Thread):
    def run(self):
        global counter

        for _ in range(rounds):
            counter += 1


thread1 = Counter()
thread2 = Counter()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Counter =", counter)

print("\n")



