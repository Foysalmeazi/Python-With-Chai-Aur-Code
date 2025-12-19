
for i in range(5):

    age = int(input("Enter your age: "))

    if age < 13:
        print("You are child as your age is:", age)
    elif age >= 13 and age < 20:
        print("You are Teenager as your age is:", age)
    elif age >= 20 and age < 60:
        print("You are Older as your age is:", age)
    else:
        print("You are Senior person as your age is:", age)



