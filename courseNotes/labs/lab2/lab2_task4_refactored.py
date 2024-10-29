#get input from user for all academic scores
lab1_grade = int(input("Lab 1 score: "))
lab2_grade = int(input("Lab 2 score: "))
assignment_grade = int(input("Assignment score: "))
midterm_grade = int(input("Midterm score: "))
final_grade = int(input("Final exam score: "))

#course score, using builtin max function to select the higher lab score, rounded to have whole number for percentage
course_score = round(max(lab1_grade, lab2_grade) * 0.05 + assignment_grade * 0.2 + midterm_grade * 0.25 + final_grade * 0.5)

#output the course score to the user, added sentence to explain output
print(f"Your score for the entire course is {course_score}%.")