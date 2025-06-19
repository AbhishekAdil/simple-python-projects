# Student Report Card Generator

# Understanding the flow of the project

# step 1: First of all we take inputs 
# step 2: create a list of subjects, and take inputs from the users 
# step 3: calculate the total and avg. , and assign Grades

'''
understand the concept of f string:-

F-string allows you to format selected parts of a string.
To specify a string as an f-string, simply put an "f" in front of the string literal, like this:

txt = f"The price is 49 dollars"
print(txt)

*** Placeholders and Modifiers ***

To format values in an f-string, add placeholders {}, a placeholder can contain variables, 
operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is {price} dollars"
print(txt)

'''
# lets start the code

# defining grades

def calc_grade(avg):
    if avg >= 90:
        return "A+"
    
    elif avg >= 80:
        return "A"
    
    elif avg >= 70:
        return "B"
    
    elif avg >= 60:
        return "C"
    
    elif avg >= 50:
        return "D"
    
    elif avg >= 40:
        return "E"
    
    else:
        return "F"


print("Welcome to the Student Report Card Generator\n")

name  = input("Enter student's name: ")
roll_no = input("Enter the roll no. : ")
class_name = input("Enter your class/grade: ")

subjects = ["Physics", "Chemistry", "Maths", "Biology", "English", "IT"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (out of 100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break    # after entering one value

            else:
                print("Marks should be between 0 to 100")

        except ValueError:
            print("Print enter a valid number")

# to total all the marks
# using sum function , pass marks list

total = sum(marks)

avg = total/len(subjects)

grade = calc_grade(avg)

print("\n Student Report Card Generated")
print("-" * 30)
print(f"Name    : {name}")
print(f"Roll No : {roll_no}")
print(f"Class   : {class_name}")
print("-" * 30)

# to print the marks and the subjects

for i in range(len(subjects)):
    print(f"{subjects[i]:10} : {marks[i]}/100")   # 10 -> maximum numbers of characters 
print("-" * 30)

print(f"Total   : {total}/{100 * len(subjects)}")
print(f"Average : {avg}")
print(f"Grade   : {grade}")