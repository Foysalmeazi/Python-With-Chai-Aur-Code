distance = int(input('Enter the distance:'))

if(distance < 2):
    print("Go by walk")
elif(distance <=20):
    print("By Motor Bike")
elif(distance>30):
    print("By a Car")
else:
    print("I dont know")
