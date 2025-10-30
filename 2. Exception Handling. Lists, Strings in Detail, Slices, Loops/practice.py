"""🧠 Practice:

1. Create a list numbers with numbers from 1 to 10.
Using a for loop, print each number from the list raised to the power of two.
Then, using a for loop, find the sum of all numbers in the numbers list.

2. Create a string text with any text.
Using a for loop, print each character from the text string.

3. Using string slicing, print the first 5 and the last 5 characters of the text string.

4. Create a list of numbers from 1 to 20.
Using a for loop, print all numbers from the list that are divisible by 3 without a remainder.

5. Using a while loop, find the sum of all numbers from 1 to 100.

6. Create an infinite loop using while True, which asks the user to input a number and prints its square.
Add a condition to exit the loop when the user enters "0" or "exit".

7. Create a list of words words, including some repeating words.
Using a for loop, print all unique words from the list.

8. Count vowels:
Ask the user to input a text string, and then use string methods to count the number of vowels (a, e, i, o, u) in the string.

9. Word replacement:
Create a string containing a sentence and ask the user to enter a word.
Replace all occurrences of that word in the sentence with the word "replaced", and print the modified sentence.

10. Create a list with duplicate elements.
Use list methods to remove duplicates and print the updated list.

11. Create a list with random numbers.
Find the largest and smallest number (you are not allowed to use built-in methods like max() or min()).

12. FizzBuzz – a classic interview task:
Write a program that prints numbers from 1 to n, replacing some of them according to divisibility rules:

For numbers divisible by 3 — print "Fizz".

For numbers divisible by 5 — print "Buzz".

For numbers divisible by both 3 and 5 — print "FizzBuzz".

For all other numbers — print the number itself.

Example for n = 15:
    
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

12.1 Bonus:
Modify the program so that the user manually inputs both divisors and the value of n.
(Instead of fixed 3, 5, and 15 — use any numbers entered by the user.)"""

#1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number ** 2)

summa = 0
for number in numbers:
    summa += number

print("The sum of all numbers is:", summa)


#2
some_string = "Today is a good day"
for char in some_string:
    print(char)

#3
substring_first = some_string[:5]
print(substring_first)

substring_second = some_string[-5:]
print(substring_second)

#4
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for numb in numbers_list:
    if numb % 3 == 0:
        print(f"Number divisible by 3: {number}")

#5
number = 1
count = 0
while number <= 100:
    count += number
    number += 1
    
print("The sum of numbers from 1 to 100 is:", count)
    