print('Task 1')
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


print('  ')
print('Task 2')
# Exclusive common numbers
import random
lst_1 = []
while len(lst_1) < 10:
    n = random.randint(0, 10)
    lst_1.append(n)
print(lst_1)
lst_2 = []
while len(lst_2) < 10:
    n = random.randint(0, 10)
    lst_2.append(n)
print(lst_2)
def intersection(lst_1, lst_2):
    return list(set(lst_1) & set(lst_2))
print(intersection(lst_1, lst_2))


print('  ')
print('Task 3')
# Extracting numbers
first_number = 0
lst_1 = []
while len(lst_1) < 100:
    first_number += 1
    lst_1.append(first_number)
print('list 1:', lst_1)
lst_2 = []
for n in lst_1:
    if n % 7 == 0 and n % 5 != 0:
        lst_2.append(n)
print('list 2:', lst_2)