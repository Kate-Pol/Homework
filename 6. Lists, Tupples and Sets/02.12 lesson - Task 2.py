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
