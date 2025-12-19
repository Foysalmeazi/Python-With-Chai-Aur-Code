for i in range(5):
    score = int(input("Enter Your Score: "))
    if score >= 80 and score <= 100:
        print("Excellent, Your Grade is A+ as you got:", score)
    elif score >= 70 and score < 80:
        print("Very Good, Your Grade is A as you got:", score)
    elif score >= 60 and score < 70:
        print("Good, Your Grade is A- as you got:", score)
    elif score >= 50 and score < 60:
        print("Fair Enough, Your Grade is B as you got:", score)
    elif score >= 33 and score < 50:
        print("Fair, Your Grade is D as you got:", score)
    else:
        print("Poor, You are fail as your score is:", score)

if(score>100):
    print('Check Your Score Again !')
    exit();



