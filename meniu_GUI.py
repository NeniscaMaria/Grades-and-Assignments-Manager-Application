from tkinter import *
from GUI import *

window=Tk()
window.title("data")
window.config(background='black')

def popUp(self,message):
    popup=Tk()
    popup.wm_title("!!")
    message=str(message)+"\n Check the Help meniu for instructions"
    label=Label(popup,text=message,font='Verdana 10')
    label.pack(side="top", fill='x', pady=10)
    button1=Button(popup,text='Okay',command=popup.destroy)
    button1.pack()
    popup.mainloop()

def fileRepo():
    students=FileRepository('assignment05_07_students.txt')
    assignments=FileRepository('assignment05_07_assignments.txt')
    grades=FileRepository('assignment05_07_grades.txt')
    undoRedo=UndoRedo()
    userInterface=GUI(students,assignments,grades,undoRedo) 
    window.destroy()
    userInterface.run()

def memoRepo():
    students=Repository()
    assignments=Repository()
    grades=Repository() 
    undoRedo=UndoRedo()
    userInterface=GUI(students,assignments,grades,undoRedo) 
    userInterface.populateStudents()
    userInterface.populateAssignments()
    window.destroy()
    userInterface.run()

def binRepo():
    try:
        students=BinaryRepository('assignment05_07_studentsBinary')
        assignments=BinaryRepository('assignment05_07_assignmentsBinary')
        grades=BinaryRepository('assignment05_07_gradesBinary')
        undoRedo=UndoRedo()
        userInterface=GUI(students,assignments,grades,undoRedo) 
        window.destroy()
        userInterface.run()
    except ValueError as ve:
        popUp(ve)
    
def jsonRepo():
    try:
        students=JsonRepository('jsonStudents')
        assignments=JsonRepository('jsonAssignments')
        grades=JsonRepository('jsonGrades')
        undoRedo=UndoRedo()
        userInterface=GUI(students,assignments,grades,undoRedo)
        window.destroy() 
        userInterface.run()
    except ValueError as ve:
        popUp(ve)

def sqlRepo():
    try:
        students=SQLRepository('students.db')
        assignments=SQLRepository('assignments.db')
        grades=SQLRepository('grades.db')
        undoRedo=UndoRedo()
        userInterface=GUI(students,assignments,grades,undoRedo) 
        window.destroy()
        userInterface.run()
    except ValueError as ve:
        popUp(ve)       

def mainGUI():
    labelStudent=Label(window,text='Please choose the way you want your data to be saved:',bg='black',fg='white',font='none 10 bold').grid(row=0,column=0,sticky=W)
    labelPermanently=Label(window,text='1)permanently:-this will use the file repository',bg='black',fg='white',font='none 10 bold').grid(row=1,column=0,sticky=W)
    labelTemporarly=Label(window,text='2)temporary:-this will use the in memory repository',bg='black',fg='white',font='none 10 bold').grid(row=2,column=0,sticky=W)
    labelBinary=Label(window,text='3)binary:-this will use a binary file repository',bg='black',fg='white',font='none 10 bold').grid(row=3,column=0,sticky=W)
    labelJson=Label(window,text='4)json:-this will use the json data',bg='black',fg='white',font='none 10 bold').grid(row=4,column=0,sticky=W)
    labelSQL=Label(window,text='5)SQL:-this will use the sql data base',bg='black',fg='white',font='none 10 bold').grid(row=5,column=0,sticky=W)
    
    buttonChoice=Button(window,text='Choose',width=6,command=fileRepo).grid(row=1,column=2,sticky=W)
    buttonChoice1=Button(window,text='Choose',width=6,command=memoRepo ).grid(row=2,column=2,sticky=W)
    buttonChoice2=Button(window,text='Choose',width=6,command=binRepo ).grid(row=3,column=2,sticky=W)
    buttonChoice3=Button(window,text='Choose',width=6,command=jsonRepo ).grid(row=4,column=2,sticky=W)
    buttonChoice4=Button(window,text='Choose',width=6,command=sqlRepo).grid(row=5,column=2,sticky=W)
    
    window.mainloop()
    