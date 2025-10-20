try:
    1 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")


bottles_of_beer = 10
try:
    amount_of_people = int(input("Please input amount of people:"))
    bottle_per_person = bottles_of_beer / amount_of_people
    print(bottle_per_person)
except (ValueError, ZeroDivisionError):
    print('Incorrect amount of people!')


bottles_of_beer = 10
try:
    amount_of_people = int(input("Please input amount of people:"))
    bottle_per_person = bottles_of_beer / amount_of_people
    print(bottle_per_person)
except ValueError:
    print('Your input is not a number')
except ZeroDivisionError:
    print('You are trying divide to zero')


try:
    bottles_of_beer = 10
    amount_of_people = int(input("Please input amount of people:"))
    bottle_per_person = bottles_of_beer / amount_of_people
    print(bottle_per_person)
except SyntaxError:
    print('Your input is not a number')



try:
    value = int("ABC")
except ValueError:
    print("A ValueError occurred!")
finally:
    print("The finally statement has executed!")



try:
    value = int(input("Please enter value"))
except ValueError:
    print("A ValueError occurred!")
else:
    print("No error occurred!")



try:
    value = int(input("Please enter value"))
except ValueError:
    print("A ValueError occurred!")
else:
    print("No error occurred!")
finally:
    print("The finally statement ran!")


number = int(input("Введите нечетное число: "))
if number % 2 != 1:
    raise ValueError("Did not get an odd number")



fruits = ['apple', 'banana', 'pear', 'orange']
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, 'two', 3.0, True]

print(fruits[0])  
print(numbers[2])  

fruits[1] = 'kiwi'
print(fruits)  

fruits.append('ananas')
print(fruits)  

del fruits[2]
print(fruits)  

l = [1, 2, 3]
l.clear()
print(l)  

l = [1, 2, 3]
l2 = l.copy()
print(l is l2)  # False 
print(l == l2)  # True

l = [1, 2, 3, 1, 1]
print(l.count(1))  # 3
print(l.count(2))  # 1
print(l.count(5))  # 0

l1 = [1, 2, 3]
l2 = ['a', 'b']
l1.extend(l2)
print(l1)  # [1,2,3,'a','b']

l = [1, 2, 3]
l.insert(1, 4)
print(l)  # [1, 4, 2, 3]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_elem = l.pop()
elem_num_4 = l.pop(3)
print(l)  # [1,2,3,5,6,7,8]
print(last_elem)  # 9
print(elem_num_4)  # 4


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l.reverse()
print(l)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

l = [3, 5, 1, 2]
l.sort()
print(l)  # [1, 2, 3, 5]