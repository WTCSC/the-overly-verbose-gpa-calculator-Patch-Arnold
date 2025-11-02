[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/38izMa6v)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21071838)
# 📚 GPA Calculator

This Python script calculates your overall GPA, analyzes semester performance, and checks whether your GPA goal is achievable by improving your grades.

# 🚀 Features

Calculates your overall GPA from a list of grades

Lets you analyze first or second semester performance

Compares your semester GPA to your total GPA and gives feedback

Lets you set a goal GPA (1.0–4.0) and checks if you can reach it by improving grades

# 💻 How It Works

The program starts with a list of grades stored as strings:

grades_not_floated = ["3.5", "4.0", "2.7", "2.2", "3.9", "1.3"]

It converts those to floating-point numbers and calculates:

The total GPA (average of all grades)

The semester GPA, depending on whether you pick semester 1 or 2

You’re asked which semester to analyze:

Which semester do you want to analyze?

First semester - first half of classes

Second semester - second half of classes
Enter 1 or 2:

The program calculates your semester GPA and prints whether it’s higher or lower than your overall GPA.

Finally, you enter your goal GPA, and the program checks whether it’s possible to reach that goal by changing one or more grades to 4.0.

# 🧠 Example Output

Calculating... beep boop... Your GPA is: 2.933333333333333
Which semester do you want to analyze?

First semester - first half of classes

Second semester - second half of classes
Enter 1 or 2: 1

Your first semester GPA is 3.4
Your total GPA is 2.93
Your total GPA is more than your first semester GPA, time to hit those books!


# 🧩 Goal GPA Logic

After you enter your desired goal GPA (from 1.0 to 4.0), the program simulates raising each grade to 4.0 one at a time.
If the goal GPA can be met that way, it tells you how many grades you’d need to raise.
Otherwise, it reports that it’s not possible with just one grade change.

# 🧰 Requirements

Python 3 or higher

No external libraries required

# 🏁 How to Run

Open Studio Visual code and copy this link into the clone from github category:

https://github.com/WTCSC/the-overly-verbose-gpa-calculator-Patch-Arnold.git

Open your terminal or command prompt

Run:

python3 gpacalc.py

Follow the prompts to view your GPA analysis

# ✨ Credits

Created with Python and Github.