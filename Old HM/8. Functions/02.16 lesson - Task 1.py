def eucledian_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
    if a == b:
        a == b
    return a

if __name__ == '__main__':
    print(eucledian_gcd(20,25))