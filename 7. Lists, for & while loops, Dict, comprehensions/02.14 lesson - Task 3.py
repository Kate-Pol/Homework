# List comprehension exercise

lst_1 = [i for i in range(1, 11)]
lst_2 = [i * i for i in range(1, 11)]
combined_lst = list(zip(lst_1, lst_2))
print(combined_lst)