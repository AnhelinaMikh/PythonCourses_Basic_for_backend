#Lecture 1. Introduction. Typing. Variables. Strings and Numbers. Boolean Algebra. Branching.

print("Hello, World!")

name = "Alice"
age = 30
print("Name:", name, "Age:", age)

name = "Alice"
age = 30
print(f"Name: {name} Age: {age}")

greeting = "Hello, World!"
name = "Alice"
full_greeting = greeting + " " + name
print(full_greeting)  

var = 25

total = var + 10
print(total) 
difference = var - 5
print(difference)  

mul = var * 2
print(mul)  

div = var / 2
print(div)  

full_div = var // 2
print(full_div)  

reminder = var % 20
print(reminder)  

power = var ** 2
print(power)  


age = 30
name = "Alice"
message = name + str(age)
print(message)  

age = input("Input your age")
age = int(age)
print("After 10 years you will have " + str(age + 10) + " years old.")
print(f"After 10 years you will have {age + 10} years old.")


num1 = int(input("Input your number"))
num2 = int(input("Input your number"))
sum = num1 + num2
print("Sum = " + str(sum))

#PRACTICE
#1 Create variables a and b and assign them the values ​​10 and 20, respectively. Perform addition, subtraction, multiplication, and division on these variables and print the results.
a = 10
b = 20
print(a + b)
print(a-b)
print(a*b)
print(b/a)

#2Create a variable text with the value "Python." Multiply this string by 3 and print the result.
text = "Python"
result_text = text * 3
print(result_text)

#3 Create a variable name with the value of your name and a variable age with your age. Create a string containing a message like "My name is [name], I am [age] years old." and print it.
name_2 = "Anhelina"
age_2 = 37
print(f"My name is {name_2}, i'm {age} years old")

#4 Write a program that calculates the expression (5 + 3) * 2 ** 2 and prints the result.
print((5 + 3) * 2 ** 2)

#5Try adding a string and a number without casting and fix the error using explicit type conversion.
string = "Its string"
number_3 = str(3)
sum_sn = string + number_3
print(sum_sn)


print(bool(''))  # False
print(bool('asdasd'))  # True
empty_string = ''
not_empty_string = 'some text'
print(bool(empty_string))  # False
print(bool(not_empty_string))  # True

bool(4)  # True
bool(0)  # False
bool(-3)  # True
positive = 5
negative = -4
zero = 0
bool(positive)  # True
bool(zero)  # False
bool(negative)  # True
bool(positive - 5)  # False
bool(0.0)  # False


result = 5 > 3  # True
another_result = 3 > 5  # False
compare_the_same_values = 3 > 3  # False
small_value = 4
big_value = 6
compare_variables = big_value > small_value  # True
compare_variables = small_value > big_value  # False
compare_strings = 'ab' > 'baa'  # False, базовое сравнение строк происходит по алфавиту

result = 5 >= 3  # True
another_result = 3 >= 5  # False
compare_the_same_values = 3 >= 3  # True
small_value = 4
big_value = 6
compare_variables = big_value >= small_value  # True
compare_variables = small_value >= big_value  # False
compare_strings = 'ab' >= 'baa'  # False

result = 5 <= 3  # True
another_result = 3 <= 5  # False
compare_the_same_values = 3 <= 3  # True
small_value = 4
big_value = 6
compare_variables = big_value <= small_value  # False
compare_variables = small_value <= big_value  # True
compare_strings = 'ab' <= 'baa'  # True

result = 5 == 3  # False
another_result = 3 == 5  # False
compare_the_same_values = 3 == 3  # True
small_value = 4
big_value = 6
compare_variables = big_value == small_value  # False
compare_variables = small_value == big_value  # False
compare_strings = 'ab' == 'baa'  # False

True and True  # True
False and True  # False
False and False  # False
True and False  # False
True and ''  # ''
'a' and 0  # 0
0 and ''  # 0
10 and ''  # ''
'bla' and 23  # 23

True or True  # True
False or True  # True
False or False  # False
True or False  # True
True or ''  # True
'a' or 0  # 'a'
0 or ''  # ''
10 or ''  # 10
'bla' or 23  # 'bla'

not True  # False
not False  # True
not ''  # True
not 33  # False

'ab' in 'bcde'  # False
'ab' in 'abcd'  # True

a = 500
b = 600
print(a is b)  
c = 500
d = c
print(c is d)  # True


age = int(input('Please enter your age:'))
name = input('Please enter your name:')

age > 18 and 'v' not in name

age < 10 or name == 'Kate'

age // 3 == 1 and len(name) > 4 or str(age) in name


#if, elif, else
a = 100
b = 'bla'
if a: print('will be printed')
if a > 50:
    print('will be printed')
if 'c' in b:
    print('wont be printed')
print("will be printed in any case")


user_age = int(input('Input your age: '))
user_name = input('Input your name: ')

if user_age > 100:
    print('User is misleading us')
elif user_age >= 18:
    print('Everything is OK')
else:
    print('Not fine')

if user_age % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

if 'a' in user_name.lower():
    print('We’re not even going to check them')
elif 'v' in user_name.lower():
    if user_age % 2 == 0:
        print('You have won a prize!')
    else:
        print('You didn’t win a prize.')
