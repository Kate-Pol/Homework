#Doggy age
class Dog:

    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        human_age = int(self.dog_age * self.age_factor)
        return human_age

dog_age = Dog(10)

print(dog_age.human_age())