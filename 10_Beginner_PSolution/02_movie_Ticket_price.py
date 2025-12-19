for i in range(5):
    age = int(input("Enter your age: "))
    day = input("Enter the day: ").lower()
    price = 12 if age >= 18 else 8
    if day == "wednesday":
        price -= 2
    print("Your movie ticket price is: $", price)
