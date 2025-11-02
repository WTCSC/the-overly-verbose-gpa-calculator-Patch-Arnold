#print (f"Welcome to the Overly Verbose GPA Calculator!")
#length = float(input(f"How many classes are you in?"))
####grades = [
#    'a' = input(f"What is your first class's grade? from 0 to 4"),
#    'b',
#    'c',
#    'd',
#    'e'
#]



grades_not_floated = [
    "3.5",
    "4.0",
    "2.7",
    "2.2",
    "3.9",
    "1.3"
]
grades = [float(item) for item in grades_not_floated]
total = sum(grades)
count = len(grades)
GPA = total/count
print(f"Calculating... beep boop... Your GPA is: {GPA}")
semester = input("Which semester do you want to analyze? 1. First semester - first half of classes 2. Second semester - second half of classes. Enter 1 or 2:  ")
if semester == "1":
    sem1tot = sum(grades[:3])
    sem1count = len(grades[:3])
    sem1GPA = sem1tot/sem1count
    print(f"Your first semester GPA is {sem1GPA}")
    print(f"your total GPA is {GPA}")
    if GPA > sem1GPA:
        print(f"Your total GPA is more then your first semester GPA, time to hit those books!")
    elif GPA < sem1GPA:
        print(f"Nice! Your first semester GPA is higher than your overall GPA. You're trending upward!")
    else:
        print("You stayed consistent with your current GPA")
elif semester == "2":
    sem2tot = sum(grades[3:])
    sem2count = len(grades[3:])
    sem2GPA = sem2tot/sem2count
    print(f"Your first semester GPA is {sem2GPA}")
    print(f"your total GPA is {GPA}")
    if GPA > sem2GPA:
        print(f"Your total GPA is more then your second semester GPA, time to hit those books!")
    elif GPA < sem2GPA:
        print(f"Nice! Your second semester GPA is higher than your overall GPA. You're trending upward!")
    else:
        print("You stayed consistent with your current GPA")
goal_not_floated = input(f"What is your goal GPA? From 1.0 to 4.0")
goal = float(goal_not_floated)
if goal > 4.0 or goal < 1.0:
    print("Not an attainable goal, not 1.0 to 4.0")
else:
    if goal == GPA:
        print("Your current GPA matches your goal.")
    else:
        for i in range(len(grades)):
            grades[i] = 4.0
            gradesum=sum(grades)
            if (gradesum/count) == goal:
                print(f"If you raise {i} grade to 4.0, you can met your goal.")
                break
        else:
            print("No grades can be changed to acheive that goal GPA... Might have to work harder in more then one class!")
            
        