
student_records = []
n = int(input('Enter Total Number of Students:'))

for i in range(0,n):
    name = input('Enter Student Name:')
    score = int(input('Enter Sudent Score:'))
    student_records.append([name,score])

score_only = []

for scr in student_records:
    score_only.append(scr[1])

unique_score = set(score_only)
sorted_uniquescore = sorted(unique_score)

if len (sorted_uniquescore)<2:
    pass
else:
    second_highest_score = sorted_uniquescore[1]

    runners_up = [name  for name,score in student_records if score == second_highest_score]
    runners_up.sort()
    
    for name in runners_up:
        print('The Runners UP Are:\n')
        print(name)


    



