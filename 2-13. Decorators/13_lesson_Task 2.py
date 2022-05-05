import functools

def stop_words(words):
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            new_str = func(*args, **kwargs).replace(words[0], '*').replace(words[1], '*')
            return new_str
        return wrapper
    return decor             

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f'{name} drinks pepsi in his brand new BMW!'
 
    assert create_slogan("Steve") == 'Steve drinks * in his brand new *!'
    
print(create_slogan('Steve'))