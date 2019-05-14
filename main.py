from UI import *
from Meniu import *
from undo_redo import *
from meniu_GUI import *
from repoIterable import RepositoryIterable

def main():
    print("Choose which which UI you wish to use: ")
    print("1)UI")
    print("2)GUI")
    print("Insert only the number of the command!")
    ok=0
    while(ok==0):
        choice1=input("Please insert the command:")
        if choice1=='1':
            ok=1
        elif choice1=='2':
            ok=1
        else:
            print("Invalid command!")
            
    if choice1=='1':
        print("Choose the way you want your data to be saved:")
        print("1)permanently:-this will use the file repository")
        print("2)temporary:-this will use the in memory repository")
        print("3)binary:-this will use a binary file repository")
        print("4)json:-this will use the json data")
        print("5)sql:-this will use the sql data base")
        print("Insert only the number of the command!")
        ok=0
        while(ok==0):
            choice=input("Please insert the command:")
            if choice=='1':
                printMeniu()
                students=FileRepository('assignment05_07_students.txt')
                assignments=FileRepository('assignment05_07_assignments.txt')
                grades=FileRepository('assignment05_07_grades.txt')
                undoRedo=UndoRedo()
                userInterface=UI(students,assignments,grades,undoRedo) 
                userInterface.run() 
                ok=1
            elif choice=='2':
                printMeniu()
                students=RepositoryIterable()
                assignments=RepositoryIterable()
                grades=RepositoryIterable() 
                undoRedo=UndoRedo()
                userInterface=UI(students,assignments,grades,undoRedo) 
                userInterface.populateStudents()
                userInterface.populateAssignments()
                userInterface.run() 
                ok=1
            elif choice=='3':
                try:
                    printMeniu()
                    students=BinaryRepository('assignment05_07_studentsBinary')
                    assignments=BinaryRepository('assignment05_07_assignmentsBinary')
                    grades=BinaryRepository('assignment05_07_gradesBinary')
                    undoRedo=UndoRedo()
                    userInterface=UI(students,assignments,grades,undoRedo) 
                    userInterface.run() 
                    ok=1
                except ValueError as ve:
                    print(ve)
            elif choice=='4':
                try:
                    printMeniu()
                    students=JsonRepository('jsonStudents')
                    assignments=JsonRepository('jsonAssignments')
                    grades=JsonRepository('jsonGrades')
                    undoRedo=UndoRedo()
                    userInterface=UI(students,assignments,grades,undoRedo) 
                    userInterface.run() 
                    ok=1
                except ValueError as ve:
                    print(ve)
            elif choice=='5':
                try:
                    printMeniu()
                    students=SQLRepository('students.db')
                    assignments=SQLRepository('assignments.db')
                    grades=SQLRepository('grades.db')
                    undoRedo=UndoRedo()
                    userInterface=UI(students,assignments,grades,undoRedo) 
                    userInterface.run() 
                    ok=1
                except ValueError as ve:
                    print(ve)
            else:
                print("Invalid command!")
    if choice1=='2':
        mainGUI()
    
main()


                   

        
        
        