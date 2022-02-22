import copy
import time

start = time.time()


class A:
    def __init__(self):
        self.a = [0] * 1000000


b = A()
c = copy.deepcopy(b)


for i in range(len(c.a)):
    c.a[i] = 1000

print((time.time() - start) * 1000)
