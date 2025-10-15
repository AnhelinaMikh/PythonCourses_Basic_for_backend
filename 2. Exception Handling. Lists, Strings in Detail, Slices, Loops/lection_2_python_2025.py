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