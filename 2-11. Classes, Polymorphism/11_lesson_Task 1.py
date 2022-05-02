class Animal:
  
    def talk(self):
        print('All animals can talk')

class Dog(Animal):
    def talk(self):
        print('woof, woof')

class Cat(Animal):
    def talk(self):
        print('meow')

def inp():
    user_inp = (input('Print an animal (cat, dog or others): ')).lower()
    if user_inp == 'cat':
        return c.talk()
    elif user_inp == 'dog':
        return d.talk()
    else:
        return a.talk()
    
a = Animal()
d = Dog()
c = Cat()

d.talk()
c.talk()
a.talk()
print(inp())