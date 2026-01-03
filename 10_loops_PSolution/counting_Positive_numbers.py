
numbers = [-1, 3, -4, 6, 7, 8, 9, -4, -6, 5, -7, -8]

count = 0
found_numbers = [] # A list to store the numbers we find

for num in numbers:
    if num > 0 and num%2==0:           # Checks for positive and even numbers
        found_numbers.append(num) # Adds the number to our list
        count += 1

# Using an f-string for easy printing
print(f"Total positive even numbers are: {count}. And they are: {found_numbers}")

