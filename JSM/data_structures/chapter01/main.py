# 프로그램 1-1

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


best = Student('Lee', 101)
print(best.get_name())
print(best.get_id())

# 프로그램 1-2

a = []
b = [None] * 10
c = [40, 10, 70, 60]
print(c[0])
print(c[-1])
c.pop()
c.pop(0)
c.append(90)
print(len(c))


# 프로그램 1-3

import random
import time
random.seed(time.time())
a = [ ]
for i in range(100):
    a.append(random.randint(1, 1000))

start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))


# 프로그램 1-4

a = [1, 5, 4, 6, 8, 11, 3, 12]
even = list(filter(lambda x: (x%2 == 0), a))
print(even)
ten_times = list(map(lambda x: x * 10, a))
print(ten_times)

b = [[0, 1, 8], [7, 2, 2], [5, 3, 10], [1, 4, 5]]
b.sort(key=lambda x: x[2])
print(b)
