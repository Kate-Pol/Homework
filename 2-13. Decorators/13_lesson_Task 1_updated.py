import functools

def my_decor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'called {func.__name__} with {args} and {kwargs}') 
        f = func(*args, **kwargs)    
    return wrapper

@my_decor
def my_func(name, last_name):
    return (f'{name} + {last_name}')
    
my_func('Kate', 'Polishchuk')
    
