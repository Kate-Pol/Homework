# Question #1
# Python is easier to learn and understand comparing with other programing languages.
# Python has large built-in library.
# Many available frameworks.
# Python efficient, reliable, and much faster than most modern languages.
# One of the most popular languages. Used in data processing, machine learning.
# There are lots of tools and modules available, which makes things much more comfortable.

# Question #2
# Variables is a memory location for the value.
# Must begin with a letter, better small one.
# Cannot have numerical character at the beginning. But can have it in other location.
# Also, can contain other special characters.
# May contain few words, however in this case they should have underscore between.
# Can have any length.
# There are some reserved words which cannot be used as a variable, because Python uses them for other things.
# Examples correct variables: first_name ; last_name etc.
# Examples incorrect variables: 1_name ; int_number ; True_value etc.

print('Task 3')
major_version = 3
minor_version = .9
version = str(major_version + minor_version)
language = 'Python'
language_version = language + ' ' + version
print(language_version)


print(' ')
print('Task 4')
sum_less_100 = 0
number = 0
while number < 100:
    if number % 3 == 0 and number % 5 == 0:
        sum_less_100 += number
        print(sum_less_100)
    number +=1
print(sum_less_100)


print(' ')
print('Task 5')
last_name = 'polishchuk'
last_name_count = len(last_name)
fact_number = 1
number = 1
while number <= last_name_count:
    fact_number *= number
    number += 1
print(str(last_name_count) + '! = ' + str(fact_number))


print(' ')
print('Task 6')
string_to_truncate = 'I have a beautiful cat!'
total_count = len(string_to_truncate)
while len(string_to_truncate) != 0:
    print(string_to_truncate[0:(total_count)])
    total_count -= 1
    if total_count == 0:
        print('Nothing\'s left here')
        break


print(' ')
print('Task 7')
weight = 63
height = 1.7
bmi = weight / (height ** 2)
lower_bound = 18.5
upper_bound = 25
if bmi < lower_bound:
    print('Your BMI is less than normal')
elif bmi >= lower_bound and bmi <= upper_bound:
    print('Your BMI is normal')
elif bmi > upper_bound:
    print('Your BMI is greater than normal')