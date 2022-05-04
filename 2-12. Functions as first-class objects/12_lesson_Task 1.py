# Detect the number of local variables declared in a function

def foo():
    a = 1
    b = 2
    c = 3

print(foo.__code__.co_nlocals)

#Exp.: co_nlocals - Number of local variables