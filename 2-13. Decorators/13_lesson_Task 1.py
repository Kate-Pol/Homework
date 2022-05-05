import functools

def my_decor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{args}, {kwargs}')     
    return wrapper

@my_decor
def my_func(name, last_name):
    print(f'My name {name} last name {last_name}')
    
print(my_func('Kate', 'Polishchuk'))
    