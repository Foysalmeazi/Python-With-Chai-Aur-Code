list_size = int(input('How many elements do you want in your list?\n'))
numbers = []

for i in range(list_size):
    # Ask for one number at a time and add it to the list immediately
    val = int(input(f"Enter number {i+1}: "))
    numbers.append(val)

even_sum = 0
obtained_num = []

for num in numbers:
    if num % 2 == 0:
        even_sum += num
        obtained_num.append(num)

print(f'Sum of even numbers: {even_sum}. The numbers are: {obtained_num}')