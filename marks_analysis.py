#student marks analysis
import numpy as num
import csv
class Student():
    
    def __init__(self,name,roll_no,maths,physics,chemistry):
        self.name=name
        self.roll_no=roll_no
        self.maths=maths
        self.physics=physics
        self.chemistry=chemistry
    def total(self):
        return self.maths+self.physics+self.chemistry
    def average(self):
        return (self.maths+self.physics+self.chemistry)/3
    def grade(self):

        avg = self.average()

        if avg >= 90:
            return "A+"

        elif avg >= 80:
            return "A"

        elif avg >= 70:
            return "B"

        elif avg >= 60:
            return "C"

        else:
            return "D"

    
    def display(self):
        print(f"Name={self.name}\nRoll_no={self.roll_no}\nMaths score={self.maths}\nPhysics score={self.physics}\nChemistry score={self.chemistry}\nAverage={self.average()}\nTotal={self.total()}\nGrade={self.grade()}")
students=[]

def student_data():
    #students=[]
    n=int(input("Enter number of students in the class:"))
    for i in range(n):
        name=input("Enter name of the student:")
        roll_no=int(input("Enter roll number of the student:"))
        maths=int(input("Enter maths marks:"))
        physics=int(input("Enter physics marks:"))
        chemistry=int(input("Enter chemistry marks:"))
        stu=Student(name,roll_no,maths,physics,chemistry)
        students.append(stu)
def display_data(students):
    for i in students:
         i.display()#This is calling with object that we created(object style calling)
    #Student.diaplay(i)-> refers to calss (class style calling)
def maths_marks(students):
    maths=[]
    for i in students:
        maths.append(i.maths)
    maths_array=num.array(maths)
    print("Maths scores=",maths)
    return maths_array
def physics_marks(students):
    physics=[]
    for i in students:
        physics.append(i.physics)
    physics_array=num.array(physics)
    print("Physics scores=",physics)
    return physics_array
def chemistry_marks(students):
    chemistry=[]
    for i in students:
        chemistry.append(i.chemistry)
    chemistry_array=num.array(chemistry)
    print("Chemistry scores=",chemistry)
    return chemistry_array
def max_scores(maths_array,physics_array,chemistry_array):
    print("Max score in Mathsematics=",num.max(maths_array))
    print("Max score in Physical Science=",num.max(physics_array))
    print("Max score in Chemistry=",num.max(chemistry_array))

def topper(students):

    highest = students[0]

    for student in students:

        if student.total() > highest.total():

            highest = student

    print("Topper:", highest.name)
    print("Total Marks:", highest.total())

"""def student_details(students):
    name=input("Enter a name:")
    for i in students:
        if i.name==name:
            i.display()
            return 
    print(f"Student with name {name} is not found")"""
def student_details(students):
    num=int(input("Enter roll number of the student:"))
    for i in students:
        if i.roll_no==num:
            i.display()
            return
    print("Student not found!!")


def consistency(maths_array,physics_array,chemistry_array):
    print("---Consistency levels of Subjects---")
    print("Mathematics=%f\nPhysics=%f,Chemistry=%f"%(num.std(maths_array),num.std(physics_array),num.std(chemistry_array)))


def average_score(maths_array,physics_array,chemistry_array):
    print("Average score of Mathematics=%f\nAverage score of Physical science=%f\nAverage score of Chemistry=%f"%(num.mean(maths_array),num.mean(physics_array),num.mean(chemistry_array)))

def save_to_file():

    with open("student_records.csv", mode="w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Roll Number",
            "Maths",
            "Physics",
            "Chemistry",
            "Total",
            "Average",
            "Grade"
        ])

        for student in students:

            writer.writerow([
                student.name,
                student.roll_no,
                student.maths,
                student.physics,
                student.chemistry,
                student.total(),
                student.average(),
                student.grade()
            ])

    print("Data saved successfully!")
    
def menu():

    while True:

        print("1. Enter Student Data")
        print("2. Display All Students")
        print("3. Show Subject Scores")
        print("4. Show Maximum Scores")
        print("5. Show Average Scores")
        print("6. Show Topper")
        print("7. Search Student")
        print("8. Show Consistency")
        print("9. Save Data")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            student_data()

        elif choice == 2:

            if len(students) == 0:
                print("No student data available!")
            else:
                display_data(students)

        elif choice == 3:

            if len(students) == 0:
                print("No student data available!")
            else:
                maths_marks(students)
                physics_marks(students)
                chemistry_marks(students)

        elif choice == 4:

            if len(students) == 0:
                print("No student data available!")
            else:
                maths_array = maths_marks(students)
                physics_array = physics_marks(students)
                chemistry_array = chemistry_marks(students)

                max_scores(
                    maths_array,
                    physics_array,
                    chemistry_array
                )

        elif choice == 5:

            if len(students) == 0:
                print("No student data available!")
            else:
                maths_array = maths_marks(students)
                physics_array = physics_marks(students)
                chemistry_array = chemistry_marks(students)

                average_score(
                    maths_array,
                    physics_array,
                    chemistry_array
                )

        elif choice == 6:

            if len(students) == 0:
                print("No student data available!")
            else:
                topper(students)

        elif choice == 7:

            if len(students) == 0:
                print("No student data available!")
            else:
                student_details(students)

        elif choice == 8:

            if len(students) == 0:
                print("No student data available!")
            else:
                maths_array = maths_marks(students)
                physics_array = physics_marks(students)
                chemistry_array = chemistry_marks(students)

                consistency(
                    maths_array,
                    physics_array,
                    chemistry_array
                )

        elif choice == 9:
            if len(students)==0:
                print("No data to save in file")
            else:
                save_to_file()
        elif choice==10:
            print("Thanks for using our Student score analyzer😊")
            break
        else:
            print("Invalid choice")


menu()
#Successfully completed my project😊
#I'm very very happy❤️