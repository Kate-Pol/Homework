# Exclusive common numbers
import random
lst_1 = [random.randint(1,10) for i in range(10)]
lst_2 = [random.randint(1,10) for i in range(10)]
print(lst_1, lst_2)
print(set(lst_1).intersection(lst_2))
