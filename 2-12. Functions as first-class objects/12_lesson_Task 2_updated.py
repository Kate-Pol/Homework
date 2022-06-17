# Function returns another function:

def outside_func():
    def inside_func():
        name = "Kate"
        print(f'My name is {name}')
    return inside_func

print(outside_func())
