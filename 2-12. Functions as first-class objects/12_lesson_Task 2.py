# Function returns another function:

def A():
    print('This is function A')
    
def B():
    print('This is function B')
    return A

returned_function = B()
print(returned_function())