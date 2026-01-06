
original_number = int(input('Enter the number to get Factorial:'))

factorial = 1;


for i in range(original_number, 0, -1):
    factorial=factorial*i
    print(f"Multiplying by {i}, current total: {factorial}")

print(f"The factorial of {original_number} is {factorial}")



''''factorial_number = int(input("Enter a number: "))


original_num = factorial_number 

factorial = 1

while factorial_number > 0:
    factorial = factorial * factorial_number
    print(f"Multiplying by {factorial_number}, current total: {factorial}")
    factorial_number = factorial_number - 1

# Use the SAVED value for the final print
print(f"The factorial of {original_num} is {factorial}")'''


