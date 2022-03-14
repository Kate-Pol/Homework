# List comprehension exercise

lst_new = list(zip([i for i in range(1, 11)], [i * i for i in range(1, 11)]))
print(lst_new)