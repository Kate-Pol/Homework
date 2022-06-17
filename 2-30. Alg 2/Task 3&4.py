number = input('Enter a number: ')


def str_sum(number):
    str_sum = 0
    for i in number:
        if i.isdigit() == True:
            a = int(i)
            str_sum += a
        else: 
            raise ValueError('Need to have all digits')
    return str_sum

print(str_sum(number))
