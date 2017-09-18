import random
def scores_and_grades(scores):
    letter = ""
    if (scores > 90):
        letter = "A"
    elif (scores >= 80):
        letter = "B"
    elif (scores >= 70):
        letter = "C"
    elif (scores >= 60):
        letter = "D"
    else:
        letter = "F"
    print("Score: " + str(scores) + "; Your grade is " + letter)
print("Scores and Grades")
for i in range(10):
    randomnum = random.randint(60, 100)
    scores_and_grades(randomnum)