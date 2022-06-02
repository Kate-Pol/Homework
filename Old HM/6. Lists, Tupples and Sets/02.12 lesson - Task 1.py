# The greatest number
import random
lst = []
for i in range(0, 10):
    n = random.randint(0, 50)
    lst.append(n)
print(lst)
start = float('-inf')
while lst:
    value = lst.pop()
    if start < value:
        start = value
print(start)