import functools

def arg_rules(type_: type, max_length: int, contains: list):
        def dec(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                        if len(args) > 1 or len(kwargs) > 0:
                                print('too many arguments')
                                return False
                        if type(args[0]) != type_:
                                print(f'argument not correct type')
                                return False
                        if len(args[0]) > max_length:
                                print('too long string')
                                return False
                        for w in contains:
                                if w not in args[0]:
                                        print('no key word in argument')
                                        return False
                        f = func(*args, **kwargs)
                        return f
                return wrapper
        return dec


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
        return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
print(create_slogan('S@SH05'))
