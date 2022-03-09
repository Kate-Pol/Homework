#Task 1 - A Person Class
class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.full_name = first + ' ' + last

    def talk(self):
        return 'Hello, my name {} and I am {} years old.'.format(self.full_name, self.age)

per_1 = Person('Carl', 'Jonhson', 26)

print('{}, {}, {}'.format(per_1.first, per_1.last, per_1.age))
print(per_1.talk())