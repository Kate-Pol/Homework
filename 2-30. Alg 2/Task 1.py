st = 'Бла-бла-бла'

def rev(st):
    if len(st) == 0:
        return st
    else: 
        return rev(st[1:]) + (st[0])
        
print(rev(st))
