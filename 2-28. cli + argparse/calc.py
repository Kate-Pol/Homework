import sys 
import math

args = sys.argv

if '-h' in args or '--help' in args: 
    print('Those are main calculator funstions: \n+ addition; \n- subtraction; \n* multiplication; \n/ division.')

def calculate():
    if '+' in args:
        add = int(args[1]) + int(args[2])
        print(add)
        if '-v' in args:
            print(f'{args[1]} + {args[2]} = {add}')
    
    elif '-' in args:
        sub = int(args[1]) - int(args[2])
        print(sub)
        if '-v' in args:
            print(f'{args[1]} - {args[2]} = {sub}')
    
    elif '*' in args:
        mult = int(args[1]) * int(args[2])
        print(mult)
        if '-v' in args:
            print(f'{args[1]} * {args[2]} = {mult}')
        
    elif '/' in args:
        div = int(args[1]) / int(args[2])
        print(div)
        if '-v' in args:
            print(f'{args[1]} / {args[2]} = {div}')

calculate()
