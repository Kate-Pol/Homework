print('Task 1 - from classroom')
print('Please enter CMYB values on real scale from 0.0 to 1.0:')
cyan = float(input('Please enter first color C: '))
magenta = float(input('Please enter second color M: '))
yellow = float(input('Please enter third color Y: '))
black = float(input('Please enter fourth color B: '))
white = 1 - black
red = 255 * white * (1 - cyan)
green = 255 * white * (1 - magenta)
blue = 255 * white * (1 - yellow)
print('Output WRGB values are:')
print(f'white number= {white}')
print(f'red number= {red}')
print(f'green number= {green}')
print(f'blue number= {blue}')


print(' ')
print('Task 1')
# Random number
print('Try to guess the number from 1 to 10')
import random
secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Your guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Congratulations!! You won***')
        break
else:
    print(f'You wrong. Correct number is {secret_number}')


print(' ')
print('Task 2')
# Birthday greetings program
first_name = input('First name: ')
age = int(input('Age: '))
print(f'Hello {first_name}, on your next birthday you\'ll be {age + 1} years old***')


print(' ')
print('Task 3')
# Words combination
from itertools import permutations
word = input('Create an input word: ')
letters = [x.lower() for x in word]
print(letters)
for y in list(permutations(letters)):
    print(''.join(y))


print(' ')
print('Task 4')
# The math quiz program
expression_value = 25 + 5 * 10
expression = '25 + 5 * 10'
answer = int(input(f'Please solve following mathematical expression: {expression} = '))
if answer == expression_value:
    print('You are right! Good job:)')
else:
    print(f'You are wrong. Correct answer is {expression_value}')

