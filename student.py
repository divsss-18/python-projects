students={}
def add_student():
    name=input("enter student name:")
    marks=int(input("enter student marks:"))
    students[name]=marks
    print("Student added successfully")
def view_students():
    if len(students)==0:
        print("no student records found")
    else:
        for name,marks in students.items():
            print(name,"-",marks)
def search_students():
    name=input("enter name to search:")
    if name in students:
        print(name,"-",students[name])
    else:
        print("student not found")
def del_student():
    name=input("enter name to delete:")
    if name in students:
        del students[name]
        print("Student deleted successfully")
    else:
        print("student not found")
def update_student():
    name=input("enter student name to update:")
    if name in students():
     new_marks=int(input("enter student marks:"))
     students[name]=new_marks
     print("marks added successfully")
    else:
     print("student not found")
def top_scorer():
    if len(students) == 0:
        print("No Student Records Found")
    else:
        highest_marks = max(students.values())

        for name, marks in students.items():
            if marks == highest_marks:
                print("Top Scorer:")
                print(name, "-", marks)
    


 

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5.Exit")
    print("6.Update student")
    print("7.top scorer")

    choice=input("Enter your choice:")

    if choice =="1":
     add_student()

    elif choice=="2":
     view_students()

    elif choice=="3":
     search_students()

    elif choice == "4":
     del_student()

    elif choice == "5": 
     print("thankyou")
    elif choice == "6":
        top_scorer()

    elif choice == "7":
        top_scorer()
        break

    else:
        print("Invalid Choice")
  


