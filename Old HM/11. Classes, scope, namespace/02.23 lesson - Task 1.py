#Task 1 - A Person Class
class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.full_name = (f'{first} {last}')

    def talk(self):
        return(f'Hello, my name {self.full_name} and I am {self.age} years old.')

per_1 = Person('Carl', 'Jonhson', 26)

print(f'{per_1.full_name}, {per_1.age}')
print(per_1.talk())
print(per_1.full_name)