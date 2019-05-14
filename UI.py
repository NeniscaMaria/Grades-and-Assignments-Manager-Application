from controllerStudent import *
from controllerAssignment import *
from controllerGrades import *
from assigning import *
from random import choice
from statistics import *
from Meniu import *
import unittest


class UI():
    def __init__(self,__students,__assignments,__grades,__undoRedo):
        
        self._repoStudents=__students
        self._repoAssignments=__assignments
        self._repoGrades=__grades
        self._undoRedo=__undoRedo
        self._controllerStudent=controllerStudent(self._repoStudents,self._undoRedo)
        self._controllerAssignments=controllerAssignmnet(self._repoAssignments,self._undoRedo)
        self._idlist=[]
        self._assignmentDict={}
        self._groups={}
        self._controllerGrades=ControllerGrades(self._repoGrades,self._repoStudents,self._repoAssignments,self._idlist,self._assignmentDict,self._undoRedo)
        '''
        ->the assignment dict will have as keys the students' id and as value the
        list of assignments that were assigned to the student with that id. The list of assignments
        also represents the list of ungraded assignments.
        
        ->the self.__groups will be a dict which will have the group number is the key and
        as value the list on the id's of students in that group
        '''  
        self._assign=Assign(self._idlist,self._assignmentDict,self._repoStudents,self._repoAssignments,self._groups,self._undoRedo)
        '''
        self.__removedStudents is of the form:
        {studentID:[all the grades that this student had],studentID1:[the same],...}
        this will come in handy when we will undo the removing of a student
        '''
        self._removedStudents={}
        '''
        self.__removedAssignments is of the form:
        {assignmentID:[all the grades of this assignment],assignmentID1:[the same],...}
        this will come in handy when we will undo the removing of an assignment
        '''
        self._removedAssignments={}
        self._removedStudentsAssignment={}
        '''
        ^^ this has the form:
        {studentID:[list of assignments of student],...}
        '''
        self._removedAssignmentsAssignments={}
        '''
        ^^^= this has the form:
        {assignmentID:[all the students that had this assignments],...}
        '''
        self.initialize()
        
        
    def initialize(self):
        lst=self._repoStudents.getAll()
        for i in range(len(lst)):
            student=lst[i]
            ID=student.get_id()
            group=student.get_group()
            
            if group not in self._groups:
                self._groups.update({group:[ID]})
            elif student.get_id() not in self._groups[group]:
                self._groups[group].append(ID)
                 
            if ID not in self._idlist:
                self._idlist.append(ID)
                
            if ID not in self._assignmentDict:
                self._assignmentDict.update({ID:[]})
                
    def run(self):
        commands={'add':self.add,
                  'remove':self.remove,
                  'update':self.update,
                  'list':self.list,
                  'student':self.assignStudent,
                  'group':self.assignGroup,
                  'grade':self.grade,
                  'stat':self.stat,
                  'late':self.late,
                  'top':self.top,
                  'all':self.all,
                  'undo':self.undo,
                  'redo':self.redo,
                  'removeGrade':self.removeGrade,
                  'deassignStudent':self.deassignStudent,
                  'deassignGroup':self.deassignGroup
                  }
                
        while True:
            #printMeniu()
            command=input("Please input a command:")
            if command=='x':
                return
            try:
                self.checkCommand(command)
                v=command.split()
                commands[v[0]](command,True)
            except ValueError as ve:
                print(ve)
    
   
    def removeGrade(self,x,undoable=False):
        '''
        THIS IS A FUNCTION THAT HELPS UNDOING THE ADDITION OF A GRADE
        x=the command 
        '''
        self._controllerGrades.removeGrade(x)
        
    def undo(self,x="",undoable=False):
        try:
            commandUndo=self._undoRedo.undo()
            if commandUndo==False:
                print("No more undos can be done!")
        except ValueError as ve:
            print(ve)
    
    def redo(self,x="",undoable=False):
        try:
            commandRedo=self._undoRedo.redo()
            if commandRedo==False:
                print("No more redos can be done!")
        except ValueError as ve:
            print(ve)
    
    def stat(self,command,undoable=False):
        statistics=Statistics(self._idlist,self._repoGrades,self._assignmentDict,self._repoStudents)
        try:
            listStat=statistics.stat(command)
            for i in range(len(listStat)):
                print(str(i+1)+") "+str(listStat[i])) 
        except ValueError as ve:
            print(ve)
    
    def late(self,command='late',undoable=False):
        repoOfLateStudents=self._assign.getLate()
        lateStudents=repoOfLateStudents.getAll()
        if len(lateStudents)==0:
            print("There are no late students.")
        else:
            i=0
            print("The late students are:")
            while i<len(lateStudents):
                print(str(i+1)+") "+str(lateStudents[i]))
                i+=1
    
    def top(self,command='top',undoable=False):
        '''
        THIS LIST listTop WILL HAVE THE FOLLOWING MEANING:
            [[studentID,averageGrade],[studentID1,averageGrade1],...]
        '''
        statistics=Statistics(self._idlist,self._repoGrades,self._assignmentDict,self._repoStudents)
        try:
            listTop=statistics.top()
            for i in range(len(listTop)):
                studentID=listTop[i][0]
                avg_grade=listTop[i][1]
                student=self._repoStudents.search(studentID)
                print(str(i+1)+") "+str(student)+" with average grade of: "+str(avg_grade))
        except ValueError as ve:
            print(ve)
        
    def all(self,command='all',undoable=False):
        statistics=Statistics(self._idlist,self._repoGrades,self._assignmentDict,self._repoStudents)
        try:
            listAll=statistics.all()
            for i in range(len(listAll)):
                assignmentID=listAll[i][0]
                avg_grade=listAll[i][1]
                print(str(i+1)+") Assignment "+str(assignmentID)+" with average grade of: "+str(avg_grade))
        except ValueError as ve:
            print(ve)
             
    def add(self,command,undoable=False):
        #undoable=shows if the operation is undoable
        #True=shows that it is
        #False=shows that it is not, therefore it will not be added in the history
        v=command.split(" ")
        try:
            if len(v)==5:
                self._controllerStudent.addStudent(command,self._groups,self._idlist,self._assignmentDict) 
                #the following are for when we will undo/redo an operation
                self._controllerGrades.restoreStudentGrades(v[1],self._removedStudents)
                self._assign.restoreStudents(self._removedStudentsAssignment, v[1])
                #here you put the way to undo/redo in the list of operations
                if undoable==True:
                    command1='remove student '+str(v[1])
                    commandUndo=FunctionCall(UI.remove,self,command1)
                    commandRedo=FunctionCall(UI.add,self,command)
                    operation=Operation(commandRedo,commandUndo)
                    self._undoRedo.add(operation)
            else:
                self._controllerAssignments.addAssignment(command)
                self._controllerGrades.restoreGradesAssignment(v[1],self._removedAssignments)
                self._assign.restoreAssignments(self._removedAssignmentsAssignments, v[1])
                #here you put the way to undo/redo the command in the list of operations
                if undoable==True:
                    command1="remove assignment "+str(v[1])
                    commandUndo=FunctionCall(UI.remove,self,command1)
                    commandRedo=FunctionCall(UI.add,self,command) 
                    operation=Operation(commandRedo,commandUndo)
                    self._undoRedo.add(operation)
        except ValueError as ve:
            print(ve)
            
    def remove(self,command,undoable=False):
        #undoable=shows if the operation is undoable
        #True=shows that it is
        #False=shows that it is not, therefore it will not be added in the history
        v=command.split(" ")
        try:
            if v[1]=='assignment':
                command1=self._controllerAssignments.removeAssignment(command)
                self._assign.removeAssignment(command,self._removedAssignmentsAssignments)
                self._controllerGrades.removeAssignment(command,self._removedAssignments)
                #here you put the way to undo/redo the command in the list of operations
                if undoable==True:
                    commandUndo=FunctionCall(UI.add,self,command1)
                    commandRedo=FunctionCall(UI.remove,self,command) 
                    operation=Operation(commandRedo,commandUndo)
                    self._undoRedo.add(operation)
            else:
                ID=v[2]
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
            print(ve)
          
    
    def update(self,command,undoable=False):
        #undoable=shows if the operation is undoable
        #True=shows that it is
        #False=shows that it is not, therefore it will not be added in the history
        v=command.split()
        try:
            if len(v)==4:
                command1=self._controllerStudent.updateStudent(command,self._groups)
                #here you put the way to undo/redo the command in the list of operations
                if undoable==True:
                    commandUndo=FunctionCall(UI.update,self,command1)
                    commandRedo=FunctionCall(UI.update,self,command)
                    operation=Operation(commandRedo,commandUndo)
                    self._undoRedo.add(operation)
            else:
                command1=self._controllerAssignments.updateAssignment(command)
                print(command1)
                #here you put the way to undo/redo the command in the list of operations
                if undoable==True:
                    commandUndo=FunctionCall(UI.update,self,command1)
                    commandRedo=FunctionCall(UI.update,self,command)
                    operation=Operation(commandRedo,commandUndo)
                    self._undoRedo.add(operation)
        except ValueError as ve:
            print(ve)
        
    def listAssignment(self,undoable=True):
        '''
        THIS FUNCTION PRINTS ALL THE ASSIGNMENTS
        INPUT:ASSIGNMENTS=THE REPOSITORY OF THE ASSIGNMENTS
        OUTPUT:-
        '''
        listOfAssignments=self._repoAssignments.getAll()
        i=0
        print("The assignmnents are:")
        while i<len(listOfAssignments):
            print(str(i+1)+") "+str(listOfAssignments[i]))
            i+=1
        if i==0:
            print("There are no assignments.")
            
    def listStudent(self,undoable=True):
        '''
        THIS FUNCTION PRINTS ALL THE STUDENTS
        INPUT:STUDENTS=THE REPOSITORY OF THE STUDENTS
        OUTPUT:-
        '''
        listOfStudents=self._repoStudents.getAll()
        i=0
        print("The students are:")
        while i<len(listOfStudents):
            print(str(i+1)+") "+str(listOfStudents[i]))
            i+=1
        if i==0:
            print("There are no students.")
            
    def listGrades(self,undoable=True): 
        '''
        THIS FUNCTION PRINTS ALL THE GRADES EXISTING IN THE REPOSITORY
        ''' 
        listOfGrades=self._repoGrades.getAll()
        if len(listOfGrades)==0:
            print("There are no grades yet.")
        else:
            i=0
            while i<len(listOfGrades):
                print(str(i+1)+") "+str(listOfGrades[i])) 
                i+=1    
        
    def list(self,command,undoable=True):
        v=command.split()
        if v[1]=='assignments':
            self.listAssignment(undoable)
        elif v[1]=='students':
            self.listStudent(undoable)
        else:
            self.listGrades(undoable)
    
    def assignStudent(self,command,undoable=False):
        #undoable=shows if the operation is undoable
        #True=shows that it is
        #False=shows that it is not, therefore it will not be added in the history
        try:
            self._assign.assignToStudent(command)
        except ValueError as ve:
            print(ve)
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
        
    def deassignStudent(self,command,undoable=False):
        self._assign.deassignStudent(command)
        #here you put the way to undo/redo the command in the list of operations
        if undoable==True:
            v=command.split(" ")
            studentID=v[1]
            assignmentID=v[2]
            command1="student "+studentID+" assignment "+assignmentID
            commandUndo=FunctionCall(UI.assignStudent,self,command1)
            commandRedo=FunctionCall(UI.deassignStudent,self,command)
            operation=Operation(commandRedo,commandUndo)
            self._undoRedo.add(operation)
            
    def deassignGroup(self,command,undoable=False):
        self.__assign.deassignGroup(command)
        if undoable==True:
            v=command.split(" ")
            group=v[1]
            assignmentID=v[2]
            command1="group "+group+" assignment "+assignmentID
            commandUndo=FunctionCall(UI.assignGroup,self,command1)
            commandRedo=FunctionCall(UI.deassignStudent,self,command)
            operation=Operation(commandRedo,commandUndo)
            self._undoRedo.add(operation)
    
    def assignGroup(self,command,undoable=False):
        #undoable=shows if the operation is undoable
        #True=shows that it is
        #False=shows that it is not, therefore it will not be added in the history
        try:
            self.__assign.assignToGroup(command)
        except ValueError as ve:
            print(ve)
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
            
    def grade(self,command,undoable=False):
        #undoable=shows if the operation is undoable
        #True=shows that it is
        #False=shows that it is not, therefore it will not be added in the history
        v=command.split(" ")
        try:
            gradeValue=int(v[1])
            studentID=int(v[4])
            assignmentID=int(v[6]) 
            grade=Grade(assignmentID,studentID,gradeValue)
            self._controllerGrades.add(command)
        except ValueError as ve:
            print(ve)
        #here you put the way to undo/redo the command in the list of operations
        if undoable==True:
            command1='removeGrade '+str(grade.get_grade())+" from student "+str(grade.get_student_id())+" for "+str(grade.get_id())
            commandUndo=FunctionCall(UI.removeGrade,self,command1,True)
            commandRedo=FunctionCall(UI.grade,self,command) 
            operation=Operation(commandRedo,commandUndo)
            self._undoRedo.add(operation)

    
    '''
    THIS IS WHERE THE USER INPUT IS CHECKED
    '''
    def checkDate(self,x):
        '''
        x=the date from the add command
        '''
        v=x.split(".")
        month=[2,4,6,9,11]
        if len(v)==1:
            raise ValueError("Please insert the full date! The accepted format is DD/MM.")
        if v[0].isdigit()==False and v[1].isdigit()==False:
            raise ValueError("The date must contain only numbers!")
        if int(v[0])<0 or int(v[0])>31:
            raise ValueError("Invalid day!")
        if int(v[1])<0 or int(v[1])>12:
            raise ValueError("Invalid month!")
        if int(v[1]) in month:
            if int(v[0])==31:
                raise ValueError("This month doesn't have 31 days!")
            
    def checkAddAssignment(self,v):
        if len(v)<6:
            raise ValueError("Please insert the full command!")
        if v[1].isdigit()==False:
            raise ValueError("The ID must be a number!")
        if int(v[1])<=0:
            raise ValueError("The ID must be a positive number!")
        if v[2]!='description':
            raise ValueError("Please insert the description of the assignment!")
        if 'deadline' in v:
            self.checkDate(v[len(v)-1])
        else:
            raise ValueError("Please insert the deadline of the assignment!")
    
    def checkAddStudent(self,v):
        if v[1].isdigit()==False:
            raise ValueError("The ID must be a positive number!")
        if int(v[1])<=0:
            raise ValueError("The ID must be a positive number!")
        if v[2].isalpha()==False:
            raise ValueError("The name cannot contain numbers!")
        name=v[3].split("-")
        if len(name)==1:
            if v[3].isalpha()==False:
                raise ValueError("The name cannot contain numbers!")       
        else:
            if name[0].isalpha()==False and name[1].isalpha()==False:
                raise ValueError("The name cannot contain numbers!")
        if v[4].isdigit()==False:
            raise ValueError("The group number must be a number!")
        if int(v[4])<=0:
            raise ValueError("The group number must be a positive number!")
        
    def checkAdd(self,v):
        if len(v)==5:
            self.checkAddStudent(v)
            return
        self.checkAddAssignment(v)
       
    def checkRemove(self,v):
        if len(v)!=3:
            raise ValueError("Please insert the full command!")
        if v[1]!='student' and v[1]!='assignment':
            raise ValueError("Illegal command! You must specify if you want to remove a student ot an assignment.")
        if v[2].isdigit()==False:
            raise ValueError("The ID must be a positive number!")
        if int(v[2])<=0:
            raise ValueError("The ID must be a positive number!")  
      
    def checkUpdateAssignment(self,v):
        if len(v)<7:
            raise ValueError("Please insert the full command!")
        if v[2].isdigit()==False:
            raise ValueError("The ID must be a positive number!")
        if int(v[2])<=0:
            raise ValueError("The ID must be a positive number!")
        if v[3]!='description':
            raise ValueError("Please insert the description of the assignment!")
        if 'deadline' in v:
            if v[len(v)-1]=='None':
                pass
            else:
                self.checkDate(v[len(v)-1])
        else:
            raise ValueError("Please insert the deadline of the assignment!")
    
    def checkUpdateStudent(self,v):
        if v[2].isdigit()==False:
            raise ValueError("The ID must be a positive number!")
        if int(v[2])<=0:
            raise ValueError("The ID must be a positive number!")
        if v[3].isdigit()==False:
            raise ValueError("The group number must be a number!")
        if int(v[3])<=0:
            raise ValueError("The group number must be a positive number!")
        
    def checkUpdate(self,v):
        if len(v)==4:
            self.checkUpdateStudent(v)
            return
        self.checkUpdateAssignment(v)  
    
    def checkList(self,v):
        if len(v)!=2:
            raise ValueError("Please insert the full command!")
        if v[1]!='students' and v[1]!='assignments' and v[1]!='grades':
            raise ValueError("Illegal command! Please insert the correct one, as stated above. ")
    
    def checkAssignStudent(self,v):
        if len(v)!=4:
            raise ValueError("Please insert the full command!")
        if v[1].isdigit==False:
            raise ValueError("The student ID must be a positive number!")
        if int(v[1])<=0:
            raise ValueError("The student ID must be a positive number!")
        if v[2]!='assignment':
            raise ValueError("Please use the word 'assignment'!")
        if v[3].isdigit==False:
            raise ValueError("The assignment ID must be a positive number!")
        if int(v[3])<=0:
            raise ValueError("The assignment ID must be a positive number!")
        
    def checkAssignGroup(self,v):
        if len(v)!=4:
            raise ValueError("Please insert the full command!")
        if v[1].isdigit==False:
            raise ValueError("The group number must be a positive number!")
        if int(v[1])<=0:
            raise ValueError("The group number must be a positive number!")
        if v[2]!='assignment':
            raise ValueError("Please use the word 'assignment'!")
        if v[3].isdigit==False:
            raise ValueError("The assignment ID must be a positive number!")
        if int(v[3])<=0:
            raise ValueError("The assignment ID must be a positive number!")
    
    def checkGrade(self,v):
        if len(v)!=7:
            raise ValueError("Please input the full comand!")
        if v[1].isdigit()==False:
            raise ValueError("The grade must be a number!")
        if int(v[1])<=0:
            raise ValueError("The grade cannot be below 0!")
        if int(v[1])>10:
            raise ValueError("The grade cannot be higher than 10!")
        if v[2]!='to':
            raise ValueError("Please use the word 'to'!")
        if v[3]!='student':
            raise ValueError("Please use the word 'student'!")
        if v[4].isdigit()==False:
            raise ValueError("The student ID must be a positive number!")
        if int(v[4])<=0:
            raise ValueError("The student ID must be a postive number!")
        if v[5]!='for':
            raise ValueError("Please use the keyword 'for'!")
        if v[6].isdigit()==False:
            raise ValueError("The assignment ID must be a positive number!")
        if int(v[6])<=0:
            raise ValueError("The assignment ID must be a positive number!")
    
    def checkStat(self,v):
        #stat assignment <assignmentID> alpha 
        if len(v)!=4:
            raise ValueError("Please insert the full/correct command!")
        if v[1]!='assignment':
            raise ValueError("Please use the word 'assignment'!")
        if v[2].isdigit()==False:
            raise ValueError("The assignmnet ID must be a positive number!")
        if int(v[2])<=0:
            raise ValueError("The assignmnet ID must be a positive number!")
        if v[3]!='alpha' and v[3]!='avg':
            raise ValueError("Please use the keyword 'alpha'!")
           
    def checkCommand(self,command):
        '''
        THIS FUNCTION CHECKS WHETHER THE COMMANDS IS VALID, OR NOT 
        '''
        v=command.split()
        if len(v)==0:
            raise ValueError("Please input a command from the meniu!")
        if v[0]=='add':
            self.checkAdd(v)
        elif v[0]=='remove':
            self.checkRemove(v)
        elif v[0]=='update':
            self.checkUpdate(v)
        elif v[0]=='list':
            self.checkList(v)
        elif v[0]=='student':
            self.checkAssignStudent(v)
        elif v[0]=='group':
            self.checkAssignGroup(v)
        elif v[0]=='grade':
            self.checkGrade(v)
        elif v[0]=='stat':
            self.checkStat(v)
        elif v[0]=='late':
            if len(v)!=1:
                raise ValueError("Invalid command!")
        elif v[0]=='top':
            if len(v)!=1:
                raise ValueError("Invalid command!")
        elif v[0]=='all' or v[0]=='undo' or v[0]=='redo':
            if len(v)!=1:
                raise ValueError("Invalid command!")
        elif v[0]=='deassignStudent' or v[0]=='deassignGroup' or v[0]=='removeGrade':
            pass
        else:
            raise ValueError("Invalid command!")
    
    def populateStudents(self):
        '''
        THIS FUNCTION IS USED TO POPULATE THE STUDENTS REPOSITORY

        '''
        groups=[911,912,913,914,915,916,917,918,919,920]
        prenom=['Atanasoae','Niga','Dobrincu','Siret','Cazac','Volschi','Iacob','Oprea','Firea','Vancea']
        nom=[' Alexandru',' Ioana',' Cosmin',' Cristina',' Leonidas',' Greta',' Zalmoxis',' Elisabeta',' Escanor',' Nadia']
        for i in range(100):
            name=choice(prenom)+choice(nom)
            ID=i+1
            group=choice(groups)
            x="add "+str(ID)+" "+name+" "+str(group)
            self.add(x)
            
    def populateAssignments(self):
        '''
        THIS FUNCTION POPULATES THE ASSIGNMENTS REPOSITORY 
        '''
        x = 'add 1 description prime numbers deadline 1.10'
        self.add(x)
        x = 'add 2 description fibonacci sequence deadline 1.12'
        self.add(x)
        x = 'add 3 description palindrom deadline 13.11'
        self.add(x)
        x = "add 4 description lee's algorithm deadline 14.11"
        self.add(x)
        x = 'add 5 description snake game deadline 15.11'
        self.add(x)
        x = 'add 6 description common divisor deadline 5.12'
        self.add(x)
        x = 'add 7 description conversion in base 2 deadline 10.12'
        self.add(x)
        x = 'add 8 description conversion in base 16 deadline 15.12'
        self.add(x)
        x = 'add 9 description conversion from base 7 in base 3 deadline 21.12'
        self.add(x)
        x = 'add 10 description adition in a given base deadline 30.12'
        self.add(x)
     
     
     
        
'''
HERE WE HAVE THE TESTS FOR THE USER INPUT
'''
class TestCommands(unittest.TestCase):
    def setUp(self):
        students=Repository()
        assignments=Repository()
        grades=Repository()
        undoredo=UndoRedo
        self.__ui=UI(students,assignments,grades,undoredo)
        
    def tearDown(self):
        self.__ui=None
        students=None
        assignments=None
        grades=None
        undoredo=None
        
    def test_checkAdd(self):
        try:
            x="add"
            v=x.split()
            self.__ui.checkAdd(v)
            self.assertFalse(self.__ui.checkAdd(v))
        except ValueError as ve:
            pass   
        try:
            x="add r bla bla v"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add -2 bla bla v"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 11 13 bla v"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 11 bla1 bla v"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 11 bla / v"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 11 bla bla-bla 23"
            v=x.split()
            self.__ui.checkAdd(v)
        except ValueError as ve:
            assert False
        try:
            x="add 13 bla bla2 v"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 13 bla bla hh"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 13 bla bla -80"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 1 bla bla 123"
            v=x.split()
            self.__ui.checkAdd(v)
        except ValueError as ve:
            assert False
        
        try:
            x="add 23 descriptio exercise 1 deadline 12.09"
            v=x.split(" ")
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 23 description exercise 1 deadlin 12.09"
            v=x.split(" ")
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 23 description exercise 1 deadline dddd"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 23 description exercise 1 deadline 12"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 23 description exercise 1 deadline -9"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 23 description exercise 1 deadline 32.90"
            v=x.split()
            self.__ui.checkAdd(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="add 23 description exercise deadline 12.09"
            v=x.split()
            self.__ui.checkAdd(v)
        except ValueError as ve:
            assert False
     
    def test_checkRemove(self):
        try:
            x="remove"
            v=x.split()
            self.__ui.checkRemove(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="remove 13 345"
            v=x.split()
            self.__ui.checkRemove(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="remove student frd"
            v=x.split()
            self.__ui.checkRemove(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="remove assignment frd"
            v=x.split()
            self.__ui.checkRemove(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="remove student -23"
            v=x.split()
            self.__ui.checkRemove(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="remove assignment 234"
            v=x.split()
            self.__ui.checkRemove(v)
        except ValueError as ve:
            assert False
        
    def test_checkUpdate(self):
        try:
            x="update"
            v=x.split()
            self.__ui.checkUpdate(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="update 13 description 345 fff nn"
            v=x.split()
            self.__ui.checkUpdate(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="update student 23 nn"
            v=x.split()
            self.__ui.checkUpdate(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="update assignment 123 ddd frd nn"
            v=x.split()
            self.__ui.checkUpdate(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="update student -23 -23"
            v=x.split()
            self.__ui.checkUpdate(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="update assignment 234 description None deadline 9.5"
            v=x.split()
            self.__ui.checkUpdate(v)
        except ValueError as ve:
            assert False
        try:
            x="update student 12 123"
            v=x.split(" ")
            self.__ui.checkUpdate(v)
        except ValueError as ve:
            assert False
        
    def test_checkList(self):
        try:
            x="list"
            v=x.split()
            self.__ui.checkList(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="list st"
            v=x.split()
            self.__ui.checkList(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="list rgvw"
            v=x.split()
            self.__ui.checkList(v)
            assert False
        except ValueError as ve:
            pass
        try:
            x="list students"
            v=x.split()
            self.__ui.checkList(v)
        except ValueError as ve:
            assert False
        try:
            x="list assignments"
            v=x.split()
            self.__ui.checkList(v)
        except ValueError as ve:
            assert False
 
    def test_AssignStudent(self):
        try:
            x='student'
            v=x.split()
            self.__ui.checkAssignStudent(v)
            assert False
        except ValueError:
            pass
        try:
            x='student oo ff ff'
            v=x.split()
            self.__ui.checkAssignStudent(v)
            assert False
        except ValueError:
            pass
        try:
            x='student -12 ff ff'
            v=x.split()
            self.__ui.checkAssignStudent(v)
            assert False
        except ValueError:
            pass
        try:
            x='student 12 ff ff'
            v=x.split()
            self.__ui.checkAssignStudent(v)
            assert False
        except ValueError:
            pass
        try:
            x='student 12 assignment ff'
            v=x.split()
            self.__ui.checkAssignStudent(v)
            assert False
        except ValueError:
            pass
        try:
            x='student 12 assignment 0'
            v=x.split()
            self.__ui.checkAssignStudent(v)
            assert False
        except ValueError:
            pass
        try:
            x='student 12 assignment 10'
            v=x.split()
            self.__ui.checkAssignStudent(v)
        except ValueError:
            assert False
            
    def test_AssignGroup(self):
        try:
            x='group'
            v=x.split()
            self.__ui.checkAssignGroup(v)
            assert False
        except ValueError:
            pass
        try:
            x='group oo ff ff'
            v=x.split()
            self.__ui.checkAssignGroup(v)
            assert False
        except ValueError:
            pass
        try:
            x='group -12 ff ff'
            v=x.split()
            self.__ui.checkAssignGroup(v)
            assert False
        except ValueError:
            pass
        try:
            x='group 12 ff ff'
            v=x.split()
            self.__ui.checkAssignGroup(v)
            assert False
        except ValueError:
            pass
        try:
            x='group 12 assignment ff'
            v=x.split()
            self.__ui.checkAssignGroup(v)
            assert False
        except ValueError:
            pass
        try:
            x='group 12 assignment 0'
            v=x.split()
            self.__ui.checkAssignGroup(v)
            assert False
        except ValueError:
            pass
        try:
            x='student 12 assignment 10'
            v=x.split()
            self.__ui.checkAssignGroup(v)
        except ValueError:
            assert False