x = None
if x is None:
    print("var included None")

for i in range(5):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for _ in range(3):
    print('It will be printed 3 times')

# It will be printed 3 times
# It will be printed 3 times
# It will be printed 3 times


numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value = min(numbers)  
max_value = max(numbers)  
print(min_value)
print(max_value)

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  
print(total)


text = "Hello, world"
length = len(text)  
print(length)

numbers = [1, 2, 3, 4, 5]
length = len(numbers)  
print(length)


numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(sorted_numbers)


"""Practice:

1. Find the largest and smallest value in a list.
2. Find the average (arithmetic mean) of all numbers in a list.
3. Find the second largest value in a list.
Example: [10, 2, 5, 8, 0] → 8
4. Check if a list is already sorted.
5. Given two numbers, print all odd numbers between them.
6. Given two numbers, find the sum of all values between them.
7. Given two numbers, print all numbers between them in reverse order.
Example: (10, 6) → [10, 9, 8, 7, 6]
8. Hard one! Using a for loop, range, and list properties — find the n-th Fibonacci number."""

#1
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value = min(numbers)  
max_value = max(numbers)  
print(min_value)
print(max_value)

#2
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
average_number = sum(numbers) / len(numbers)
print(f"Average value: {average_number}")

#3
numbers = [10, 2, 5, 8, 0]
unique_sorted_numbers = sorted(set(numbers))
print(sorted_numbers[-2])

numbers = [10, 2, 5, 8, 0]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers) 
second_largest = sorted_numbers[1]
print(f"The second largest number is: {second_largest}")


#4
numbers = [1, 2, 3, 4, 5]

if numbers == sorted(numbers):
    print("The list is sorted in ascending order.")
elif numbers == sorted(numbers, reverse=True):
    print("The list is sorted in descending order.")
else:
    print("The list is not sorted.")
