# Extracting numbers
lst_1 = [i for i in range(1,101)]
print('list 1:', lst_1)
lst_2 = []
for n in lst_1:
    if n % 7 == 0 and n % 5 != 0:
        lst_2.append(n)
print('list 2:', lst_2)