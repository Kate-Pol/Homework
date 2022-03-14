# String into Dictionary
test_str = input('Please enter the string: ')
print(test_str)
space = ' '
new_dict = {ind: i for ind, i in enumerate(test_str.split(space))}
print(new_dict)