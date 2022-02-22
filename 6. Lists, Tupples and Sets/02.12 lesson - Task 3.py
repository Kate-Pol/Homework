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