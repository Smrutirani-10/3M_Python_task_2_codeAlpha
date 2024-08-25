# Grade calculation function
def get_grades(num_subjects):
    grades = []
    for i in range(1, num_subjects + 1):
        while True:
            try:
                grade = float(input(f"Enter the grade for subject {i}: "))
                #Assuming grade scale is 0 to 100 for calculation.
                if 0 <= grade <= 100:  
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter valid  number.")
    return grades

#Avarage  calculation Function
def calculate_average(grades):
    return sum(grades) / len(grades)
#displaying the Student details
def display_results(student_name, grades, average):
    print(f"\nResults for {student_name}:")
    print(f"Grades of The Subject: {grades}")
    print(f"Total grade score: {sum(grades):.2f}")
    print(f"Average grade: {average:.2f}")

    #Grade system for Student average mark:

    if average >= 90:
        print("Grade : O")
    elif average >= 80:
        print("Grade : E")
    elif average >= 70:
        print("Grade : A")
    elif average >= 60:
        print("Grade : B")
    elif average >= 50:
        print("Grade : C")
    elif average >= 40 :
        print("Grade : D")
    else:
        print("Grade : F")

def main():
    no_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects  : "))
    
    #For multiple students
    for i in range(no_students):
        student_name = input(f"\nEnter the {i+1} - student's name: ")
        grades = get_grades(num_subjects)
        average = calculate_average(grades)
        display_results(student_name, grades, average)


if True:
    main()

