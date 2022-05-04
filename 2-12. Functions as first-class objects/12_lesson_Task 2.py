# Function returns another function:

def outside_func(text):
    def inside_func(name):
        return f'My name is {name}'
    return inside_func(text)

print(outside_func('Kate'))