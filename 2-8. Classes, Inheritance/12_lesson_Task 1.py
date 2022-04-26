#Class - School 
class Person():
    def __init__(self, name, last_name, age):
      self.name = name
      self.last_name = last_name
      self.age = age

class Student(Person):
    def __init__(self, name, last_name, age, class_No):
        super().__init__(name, last_name, age)
        self.start_year = 0
        self.class_No = class_No
        
    def year_study(self, year_study):
        self.start_year += year_study           

class Teacher(Person):
    def __init__(self, name, last_name, age, course_name, salary):
        super().__init__(name, last_name, age)
        self.course_name = course_name
        self.salary = salary
    
    def salary_increase(self, salary):
        self.salary += salary
        
student = Student('John', 'Smith', 10, '4A')
teacher = Teacher('Barbara', 'McKenzy', 40, 'Geography', 50000)

print(f'Student {student.name} {student.last_name} is in class {student.class_No}')
print(teacher.name, teacher.last_name, teacher.course_name, teacher.salary)
teacher.salary_increase(2500)
print('New salary is:', teacher.salary)