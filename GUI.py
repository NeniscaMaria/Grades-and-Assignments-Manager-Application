from tkinter import *
from UI import *


class GUI(UI):
    def __init__(self,__students,__assignments,__grades,__undoRedo):
        UI.__init__(self, __students, __assignments, __grades, __undoRedo)
        self.__window=Tk()
        #here I write the name of the project
        self.__window.title('Assignments')
        self.__window.config(background='black')
        
        #here we create the labels and the text entry boxes for students
        self.__labelStudent=Label(self.__window,text='Students:',bg='black',fg='white',font='none 10 bold').grid(row=0,column=0,sticky=E)
        self.__labelStudentID=Label(self.__window,text='StudentID:',bg='black',fg='white',font='none 10 bold').grid(row=0,column=1,sticky=E)
        self.__textEntryStudentsID=Entry(self.__window,width=10,bg='white')
        self.__textEntryStudentsID.grid(row=0,column=2,sticky=E)
        self.__labelStudentName=Label(self.__window,text='Name:',bg='black',fg='white',font='none 10 bold').grid(row=0,column=3,sticky=E)
        self.__textEntryStudentsName=Entry(self.__window,width=30,bg='white')
        self.__textEntryStudentsName.grid(row=0,column=4,sticky=E)
        self.__labelStudentGroup=Label(self.__window,text='Group:',bg='black',fg='white',font='none 10 bold').grid(row=0,column=5,sticky=E)
        self.__textEntryStudentsGroups=Entry(self.__window,width=5,bg='white')
        self.__textEntryStudentsGroups.grid(row=0,column=6,sticky=E)
        
        #now we create the submit boxes
        self.__buttonStudentAdd=Button(self.__window,text='ADD',width=6,command=self.__addStudent).grid(row=0,column=7,sticky=E)
        self.__buttonStudentRemove=Button(self.__window,text='REMOVE',width=6,command=self.__removeStudent).grid(row=0,column=8,sticky=E)
        self.__buttonStudentUpdate=Button(self.__window,text='UPDATE',width=6,command=self.__updateStudent).grid(row=0,column=9,sticky=E)
        
        #here we create the labels and the text entry boxes for assignments
        self.__labelAssignments=Label(self.__window,text='Assignments:',bg='black',fg='white',font='none 10 bold').grid(row=1,column=0,sticky=E)
        self.__labelAssignmentID=Label(self.__window,text='AssignmentID:',bg='black',fg='white',font='none 10 bold').grid(row=1,column=1,sticky=E)
        self.__textEntryAssignmentID1=Entry(self.__window,width=10,bg='white')
        self.__textEntryAssignmentID1.grid(row=1,column=2,sticky=E)
        self.__labelAssignmentDescription=Label(self.__window,text='Description:',bg='black',fg='white',font='none 10 bold').grid(row=1,column=3,sticky=E)
        self.__textEntryAssignmentDescription=Entry(self.__window,width=30,bg='white')
        self.__textEntryAssignmentDescription.grid(row=1,column=4,sticky=E)
        self.__labelAssignmentDeadline=Label(self.__window,text='Deadline:',bg='black',fg='white',font='none 10 bold').grid(row=1,column=5,sticky=E)
        self.__textEntryAssignmentDeadline=Entry(self.__window,width=5,bg='white')
        self.__textEntryAssignmentDeadline.grid(row=1,column=6,sticky=E)
        
        #now we create the submit boxes
        self.__buttonAssignmentAdd=Button(self.__window,text='ADD',width=6,command=self.__addAssignment).grid(row=1,column=7,sticky=E)
        self.__buttonAssignmentRemove=Button(self.__window,text='REMOVE',width=6,command=self.__removeAssignment).grid(row=1,column=8,sticky=E)
        self.__buttonAssignmentUpdate=Button(self.__window,text='UPDATE',width=6,command=self.__updateAssignment).grid(row=1,column=9,sticky=E)
    
        #here we create the labels and the text entry boxes for grades
        self.__labelGrades=Label(self.__window,text='Grades:',bg='black',fg='white',font='none 10 bold').grid(row=2,column=0,sticky=E)
        self.__labelGradesStudentID=Label(self.__window,text='StudentID:',bg='black',fg='white',font='none 10 bold').grid(row=2,column=1,sticky=E)
        self.__textEntryGradesStduentsID=Entry(self.__window,width=10,bg='white')
        self.__textEntryGradesStduentsID.grid(row=2,column=2,sticky=E)
        self.__labelGradesAssignmentID=Label(self.__window,text='AssignmentID:',bg='black',fg='white',font='none 10 bold').grid(row=2,column=3,sticky=E)
        self.__textEntryAssignmentID=Entry(self.__window,width=10,bg='white')
        self.__textEntryAssignmentID.grid(row=2,column=4,sticky=E)
        self.__labelGradesValue=Label(self.__window,text='Grade:',bg='black',fg='white',font='none 10 bold').grid(row=2,column=5,sticky=E)
        self.__textEntryGradesValue=Entry(self.__window,width=5,bg='white')
        self.__textEntryGradesValue.grid(row=2,column=6,sticky=E)
        
        #now we create the submit boxes
        self.__buttonGradesAdd=Button(self.__window,text='ADD',width=6,command=self.__grade).grid(row=2,column=7,sticky=E)
        
        #here we create the labels and boxes for assigning
        self.__labelAssiging=Label(self.__window,text='Assigning:',bg='black',fg='white',font='none 10 bold').grid(row=3,column=0,sticky=E)
        self.__labelAssignStudent=Label(self.__window,text='StudentID:',bg='black',fg='white',font='none 10 bold').grid(row=3,column=1,sticky=E)
        self.__textEntryAssignStudentID=Entry(self.__window,width=10,bg='white')
        self.__textEntryAssignStudentID.grid(row=3,column=2,sticky=E)
        self.__labelAssignGroup=Label(self.__window,text='Group:',bg='black',fg='white',font='none 10 bold').grid(row=4,column=1,sticky=E)
        self.__textEntryAssignGroup=Entry(self.__window,width=10,bg='white')
        self.__textEntryAssignGroup.grid(row=4,column=2,sticky=E)
        self.__labelAssignAssignment=Label(self.__window,text='AssignmentID:',bg='black',fg='white',font='none 10 bold').grid(row=3,column=3,sticky=E)
        self.__textEntryAssignAssignmentID=Entry(self.__window,width=30,bg='white')
        self.__textEntryAssignAssignmentID.grid(row=3,column=4,sticky=E)
        self.__labelAssignAssignment1=Label(self.__window,text='AssignmentID:',bg='black',fg='white',font='none 10 bold').grid(row=4,column=3,sticky=E)
        self.__textEntryAssignAssignmentID1=Entry(self.__window,width=30,bg='white')
        self.__textEntryAssignAssignmentID1.grid(row=4,column=4,sticky=E)
        
        #here we create the submit boxes
        self.__buttonAssign=Button(self.__window,text='ASSIGN',width=6,command=self.__assignStudent).grid(row=3,column=7,sticky=E)
        self.__buttonAssign1=Button(self.__window,text='ASSIGN',width=6,command=self.__assignGroup).grid(row=4,column=7,sticky=E)
        
        #here we create the labels and submit boxes for the listings
        self.__labelLists=Label(self.__window,text='List:',bg='black',fg='white',font='none 10 bold').grid(row=6,column=0,sticky=E)
        self.__buttonList1=Button(self.__window,text='Students',width=7,command=self.__listStudent).grid(row=6,column=1,sticky=E)
        self.__buttonList2=Button(self.__window,text='Assignments',width=10,command=self.__listAssignment).grid(row=6,column=2,sticky=W)
        self.__buttonList3=Button(self.__window,text='Grades',width=5,command=self.__listGrades).grid(row=6,column=2,sticky=E)
    
        #here we create the labels and submit boxes for the statistics
        self.__labelStat=Label(self.__window,text='Statistics:',bg='black',fg='white',font='none 10 bold').grid(row=7,column=0,sticky=E)
        self.__labelStat1=Label(self.__window,text='AssignmentID:',bg='black',fg='white',font='none 10 bold').grid(row=7,column=1,sticky=E)
        self.__textEntryStat1=Entry(self.__window,width=10,bg='white')
        self.__textEntryStat1.grid(row=7,column=2,sticky=W)
        self.__buttonStat1=Button(self.__window,text='STAT',width=5,command=self.__stat).grid(row=7,column=3,sticky=W)
        self.__buttonStat2=Button(self.__window,text='LATE',width=5,command=self.__late).grid(row=7,column=3)
        self.__buttonStat3=Button(self.__window,text='TOP',width=5,command=self.__top).grid(row=7,column=3,sticky=E)
        self.__buttonStat4=Button(self.__window,text='ALL',width=5,command=self.__all).grid(row=7,column=4,sticky=W)
        
        #here we create the help and undo/redo buttons
        self.__buttonHelp=Button(self.__window,text='Help',width=5,command=self.__help).grid(row=8,column=9,sticky=E)
        self.__buttonUndo=Button(self.__window,text='UNDO',width=5,command=self.__undo).grid(row=8,column=0,sticky=E)
        self.__buttonRedo=Button(self.__window,text='REDO',width=5,command=self.__redo).grid(row=8,column=1,sticky=W)  
        
        #here we create the output box
        self.__output=Text(self.__window,width=100,height=25,wrap=WORD, background='white')
        self.__output.grid(row=10,column=1,columnspan=6,sticky=W)
        
    def __popUp(self,message):
        popup=Tk()
        popup.wm_title("!!")
        message=str(message)+"\n Check the Help meniu for instructions"
        label=Label(popup,text=message,font='Verdana 10')
        label.pack(side="top", fill='x', pady=10)
        button1=Button(popup,text='Okay',command=popup.destroy)
        button1.pack()
        popup.mainloop()
        
    def __assignGroup(self,undoable=True):
        group=self.__textEntryAssignGroup.get()
        assignmentID=self.__textEntryAssignAssignmentID1.get()
        command='group '+group+ ' assignment '+assignmentID
        try:
            UI.checkCommand(self, command)
            self._assign.assignToGroup(command)
            #here you put the way to undo/redo the command in the list of operations
            if undoable==True:
                v=command.split()
                group=int(v[1])
                assignmentID=int(v[3])
                x='deassignGroup '+str(group)+" "+str(assignmentID)
                commandUndo=FunctionCall(UI.deassignGroup,self,x)
                commandRedo=FunctionCall(UI.assignGroup,self,command)
                operation=Operation(commandRedo,commandUndo)
                self._undoRedo.add(operation)
        except ValueError as ve:
            self.__popUp(ve)
                        
    def __assignStudent(self,undoable=True):
        studentID=self.__textEntryAssignStudentID.get()
        assignmentID=self.__textEntryAssignAssignmentID.get()
        command='student '+studentID+ ' assignment '+assignmentID
        try:
            UI.checkCommand(self, command)
            self._assign.assignToStudent(command)
            #here you put the way to undo/redo the command in the list of operations
            if undoable==True:
                v=command.split(" ")
                studentID=int(v[1])
                assignmentID=int(v[3])
                commandRedo=FunctionCall(UI.assignStudent,self,command)
                x='deassignStudent '+str(studentID)+" "+str(assignmentID)
                commandUndo=FunctionCall(UI.deassignStudent,self,x)
                operation=Operation(commandRedo,commandUndo)
                self._undoRedo.add(operation)
        except ValueError as ve:
            self.__popUp(ve)
                    
    def __help(self):
        self.__output.delete(0.0, END)
        self.__output.insert(END,"ATTENTION! All the text boxes are case sensitive!\n\n")
        self.__output.insert(END,"When removing a student/an assignment is enough to insert only the ID.\n\n")
        self.__output.insert(END,"When you want to update a student, complete the studentID field with the ID of the student you want to update, and complete the group field with the group in which you want to transfer the student.\n\n")
        self.__output.insert(END,"When you want to update an assignment, complete the following fields as shown below:\n")
        self.__output.insert(END,"\t->assignmentID field: with the ID of the assignment you want to update\n")
        self.__output.insert(END,"\t->description field:->complete it with the new description\n")
        self.__output.insert(END,"\t\t->complete it with 'None' if you don't want to change the description\n")
        self.__output.insert(END,"\t->deadline field:->complete it with the new deadline\n")
        self.__output.insert(END,"\t\t->complete it with 'None' if you don't want to change the deadline\n\n")
        self.__output.insert(END,"Instructions for statistics:\n")
        self.__output.insert(END,"\t->STAT:if you want all students who received a given assignment, ordered alphabetically. This is the only one that requires an assignmentID.\n")
        self.__output.insert(END,"\t->LATE:if you want all students who are late in handing in at least one assignment. These are all the students who have an ungraded assignment for which the deadline has passed.\n")
        self.__output.insert(END,"\t->TOP:if you want the students with the best school situation, sorted in descending order of the average grade received for all assignments.\n")
        self.__output.insert(END,"\t->ALL:if you want all assignments for which there is at least one grade, sorted in descending order of the average grade received by all students who received that assignment.\n")
        
    def __undo(self):
        try:
            commandUndo=self._undoRedo.undo()
            if commandUndo==False:
                self.__popUp("No more undos can be done!")
        except ValueError as ve:
            self.__popUp(ve)  
        
    def __redo(self):
        try:
            commandRedo=self._undoRedo.redo()
            if commandRedo==False:
                self.__popUp("No more redos can be done!")
        except ValueError as ve:
            self.__popUp(ve)
        
    def __addStudent(self,undoable=True):  
        ID=self.__textEntryStudentsID.get()
        name=self.__textEntryStudentsName.get()
        group=self.__textEntryStudentsGroups.get()
        command='add '+ID+" "+name+" "+group
        try:
            UI.checkCommand(self, command)
            self._controllerStudent.addStudent(command,self._groups,self._idlist,self._assignmentDict) 
            #the following are for when we will undo/redo an operation
            self._controllerGrades.restoreStudentGrades(ID,self._removedStudents)
            self._assign.restoreStudents(self._removedStudentsAssignment, ID)
            #here you put the way to undo/redo in the list of operations
            if undoable==True:
                command1='remove student '+str(ID)
                commandUndo=FunctionCall(UI.remove,self,command1)
                commandRedo=FunctionCall(UI.add,self,command)
                operation=Operation(commandRedo,commandUndo)
                self._undoRedo.add(operation)
        except ValueError as ve:
            self.__popUp(ve)
        
    def __removeStudent(self,undoable=True):
        ID=self.__textEntryStudentsID.get()
        command='remove student '+ID
        try:
            UI.checkCommand(self, command)
            command1=self._controllerStudent.removeStudent(command,self._groups)
            self._assign.removeStudent(command,self._removedStudentsAssignment)
            self._controllerGrades.removeStudent(command,self._removedStudents)
            #here you put the way to undo/redo the command in the list of operations
            if undoable==True:
                commandRedo=FunctionCall(UI.remove,self,command) 
                commandUndo=FunctionCall(UI.add,self,command1)
                operation=Operation(commandRedo,commandUndo)
                self._undoRedo.add(operation)
        except ValueError as ve:
            self.__popUp(ve)
            
    def __updateStudent(self,undoable=True):
        ID=self.__textEntryStudentsID.get()
        group=self.__textEntryStudentsGroups.get()
        command='update student '+ID+" "+group
        try:
            UI.checkCommand(self, command)
            command1=self._controllerStudent.updateStudent(command,self._groups)
            #here you put the way to undo/redo the command in the list of operations
            if undoable==True:
                commandUndo=FunctionCall(UI.update,self,command1)
                commandRedo=FunctionCall(UI.update,self,command)
                operation=Operation(commandRedo,commandUndo)
                self._undoRedo.add(operation)
        except ValueError as ve:
            self.__popUp(ve)
            
    def __addAssignment(self,undoable=True):
        ID=self.__textEntryAssignmentID1.get()
        description=self.__textEntryAssignmentDescription.get()
        deadline=self.__textEntryAssignmentDeadline.get()
        command='add '+ID+" description "+description+" deadline "+deadline
        try:
            UI.checkCommand(self, command)
            self._controllerAssignments.addAssignment(command)
            self._controllerGrades.restoreGradesAssignment(ID,self._removedAssignments)
            self._assign.restoreAssignments(self._removedAssignmentsAssignments, ID)
            #here you put the way to undo/redo the command in the list of operations
            if undoable==True:
                command1="remove assignment "+str(ID)
                commandUndo=FunctionCall(UI.remove,self,command1)
                commandRedo=FunctionCall(UI.add,self,command) 
                operation=Operation(commandRedo,commandUndo)
                self._undoRedo.add(operation)
        except ValueError as ve:
            self.__popUp(ve)
            
    def __removeAssignment(self,undoable=True):
        ID=self.__textEntryAssignmentID1.get()
        command='remove assignment '+ID
        try:
            UI.checkCommand(self, command)
            command1=self._controllerAssignments.removeAssignment(command)
            self._assign.removeAssignment(command,self._removedAssignmentsAssignments)
            self._controllerGrades.removeAssignment(command,self._removedAssignments)
            #here you put the way to undo/redo the command in the list of operations
            if undoable==True:
                commandUndo=FunctionCall(UI.add,self,command1)
                commandRedo=FunctionCall(UI.remove,self,command) 
                operation=Operation(commandRedo,commandUndo)
                self._undoRedo.add(operation)
        except ValueError as ve:
            self.__popUp(ve)
         
    
    def __updateAssignment(self,undoable=True):
        ID=self.__textEntryAssignmentID1.get()
        description=self.__textEntryAssignmentDescription.get()
        if description=="":
            description="None"
        deadline=self.__textEntryAssignmentDeadline.get()
        if deadline=="":
            deadline="None"
        command='update assignment '+ID+" description "+description+" deadline "+deadline
        try:
            UI.checkCommand(self, command)
            command1=self._controllerAssignments.updateAssignment(command)
            #here you put the way to undo/redo the command in the list of operations
            if undoable==True:
                commandUndo=FunctionCall(UI.update,self,command1)
                commandRedo=FunctionCall(UI.update,self,command)
                operation=Operation(commandRedo,commandUndo)
                self._undoRedo.add(operation)
        except ValueError as ve:
            self.__popUp(ve)
    
    def __grade(self,undoable=True):      
        studentID=self.__textEntryGradesStduentsID.get()
        assignmentID=self.__textEntryAssignmentID.get()
        gradeValue=self.__textEntryGradesValue.get()
        command='grade '+gradeValue+ ' to student '+studentID+ ' for '+assignmentID
        try:
            UI.checkCommand(self, command)
            self._controllerGrades.add(command)
            #here you put the way to undo/redo the command in the list of operations
            if undoable==True:
                command1='removeGrade '+str(gradeValue)+" from student "+str(studentID)+" for "+str(assignmentID)
                commandUndo=FunctionCall(UI.removeGrade,self,command1)
                commandRedo=FunctionCall(UI.grade,self,command) 
                operation=Operation(commandRedo,commandUndo)
                self._undoRedo.add(operation)
        except ValueError as ve:
            self.__popUp(ve)
            
    def __listStudent(self):
        self.__output.delete(0.0, END)
        listOfStudents=self._repoStudents.getAll()
        i=0
        self.__output.insert(END,"The students are:\n")
        while i<len(listOfStudents):
            self.__output.insert(END,str(i+1)+") "+str(listOfStudents[i])+'\n')
            i+=1
        if i==0:
            self.__output.insert(END,"There are no students.")
        
    def __listAssignment(self):
        self.__output.delete(0.0, END)
        '''
        THIS FUNCTION PRINTS ALL THE ASSIGNMENTS
        INPUT:ASSIGNMENTS=THE REPOSITORY OF THE ASSIGNMENTS
        OUTPUT:-
        '''
        listOfAssignments=self._repoAssignments.getAll()
        i=0
        self.__output.insert(END,"The assignmnents are:\n")
        while i<len(listOfAssignments):
            self.__output.insert(END,str(i+1)+") "+str(listOfAssignments[i])+'\n')
            i+=1
        if i==0:
            self.__output.insert(END,"There are no assignments.")
    
    def __listGrades(self):
        self.__output.delete(0.0, END)
        '''
        THIS FUNCTION PRINTS ALL THE GRADES EXISTING IN THE REPOSITORY
        ''' 
        listOfGrades=self._repoGrades.getAll()
        if len(listOfGrades)==0:
            self.__output.insert(END,"There are no grades yet.")
        else:
            i=0
            while i<len(listOfGrades):
                self.__output.insert(END,str(i+1)+") "+str(listOfGrades[i])+'\n') 
                i+=1    
    
    def __stat(self):
        self.__output.delete(0.0, END)
        assignmentID=self.__textEntryStat1.get()
        if assignmentID=='':
            self.__popUp("Plese complete the 'AssignmentID' field")
            return
        command='stat assignment '+assignmentID+ ' alpha'
        statistics=Statistics(self._idlist,self._repoGrades,self._assignmentDict,self._repoStudents)
        try:
            listStat=statistics.stat(command)
            if len(listStat)==0:
                self.__output.insert(END,"There are no students with this assignment.\n")
            for i in range(len(listStat)):
                self.__output.insert(END,str(i+1)+") "+str(listStat[i])+'\n') 
        except ValueError as ve:
            self.__output.insert(END,ve)
        
    def __late(self):
        self.__output.delete(0.0, END)
        repoOfLateStudents=self._assign.getLate()
        lateStudents=repoOfLateStudents.getAll()
        if len(lateStudents)==0:
            self.__output.insert(END,"There are no late students.\n")
        else:
            i=0
            self.__output.insert(END,"The late students are:\n")
            while i<len(lateStudents):
                self.__output.insert(END,str(i+1)+") "+str(lateStudents[i])+'\n')
                i+=1
    
    def __top(self):
        '''
        THIS LIST listTop WILL HAVE THE FOLLOWING MEANING:
            [[studentID,averageGrade],[studentID1,averageGrade1],...]
        '''
        self.__output.delete(0.0, END)
        statistics=Statistics(self._idlist,self._repoGrades,self._assignmentDict,self._repoStudents)
        try:
            listTop=statistics.top()
            for i in range(len(listTop)):
                studentID=listTop[i][0]
                avg_grade=listTop[i][1]
                student=self._repoStudents.search(studentID)
                self.__output.insert(END,str(i+1)+") "+str(student)+" with average grade of: "+str(avg_grade)+'\n')
        except ValueError as ve:
            self.__popUp(ve)
           
    def __all(self):
        self.__output.delete(0.0, END)
        statistics=Statistics(self._idlist,self._repoGrades,self._assignmentDict,self._repoStudents)
        try:
            listAll=statistics.all()
            for i in range(len(listAll)):
                assignmentID=listAll[i][0]
                avg_grade=listAll[i][1]
                self.__output.insert(END,str(i+1)+") Assignment "+str(assignmentID)+" with average grade of: "+str(avg_grade)+'\n')
        except ValueError as ve:
            self.__popUp(ve)
            
    def run(self):
        self.__window.mainloop()
    
    def populateStudents(self):
        UI.populateStudents(self)
    
    def populateAssignments(self):
        UI.populateAssignments(self)
 
'''     
students=Repository()
assignments=Repository()
grades=Repository() 
undoRedo=UndoRedo()
userInterface=GUI(students,assignments,grades,undoRedo)
userInterface.populateStudents()
userInterface.populateAssignments()
userInterface.run()'''
