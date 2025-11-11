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