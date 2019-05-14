import datetime
from repository import Repository
from repository import FileRepository
from undo_redo import UndoRedo,Operation,FunctionCall
import unittest

class Assign:
    def __init__(self,idlist,assignmentDict,students,assignments,groups,undoRedo):
        '''
        ->the assignment dict will have as keys the students' id and as value the
        list of assignments that were assigned to the student with that id
        
        ->groups will be a dict which will have the group number is the key and
        as value the list on the id's of students in that group
        input:-idlist-list
            assignmentDict-dictionary
            students,assignments-repository
            groups-dictionary
        '''
        self.__idlist=idlist
        self.__assignmentDict=assignmentDict
        self.__repoStudents=students
        self.__repoAssignments=assignments
        self.__groups=groups
        self.__undoRedo=undoRedo
    
    def assignToStudent(self,command):
        '''
        this function assigns to a student an assignment
        '''
        v=command.split()
        studentID=int(v[1])
        assignmentID=int(v[3])
        if studentID in self.__assignmentDict.keys():
            if assignmentID in self.__assignmentDict[studentID]:
                raise ValueError("You already gave to this student this assignment!") 
            else:
                self.__assignmentDict[studentID].append(assignmentID)
        
    def deassignStudent(self,command):
        v=command.split(" ")
        studentID=int(v[1])
        assignmentID=int(v[2])
        self.__assignmentDict[studentID]=list(filter(lambda x: x!=assignmentID,self.__assignmentDict[studentID]))
             
    def assignToGroup(self,command):
        '''
        this function assigns to an entire group the same assignment
        '''
        v=command.split()
        group=int(v[1])
        assignmentID=int(v[3])
        if group in self.__groups:
            listOfStudentIDs=self.__groups[group]
            #we will count how many students in this group have this assignment
            #we must not give a student an assignment if he already has it assigned to him
            number=0
            for i in range(len(listOfStudentIDs)):
                if listOfStudentIDs[i] in self.__assignmentDict.keys():
                    if assignmentID in self.__assignmentDict[listOfStudentIDs[i]]:
                        number=number+1 
                    else:
                        self.__assignmentDict[listOfStudentIDs[i]].append(assignmentID)
            if number==len(listOfStudentIDs):
                raise ValueError("You already gave this assignment to this group!")
        else:
            raise ValueError("This group does not exist!")
        
    def deassignGroup(self,command):
        v=command.split(" ")
        group=int(v[1])
        assignmentID=int(v[2])
        for i in range (len(self.__groups[group])):
            studentID=self.__groups[group][i]
            for j in range(len(self.__assignmentDict[studentID])):
                if self.__assignmentDict[studentID][j]==assignmentID:
                    del self.__assignmentDict[studentID][j]
            if self.__assignmentDict[studentID]==[]:
                del self.__assignmentDict[studentID]
            
    def restoreStudents(self,removedStudentsAssignment,ID):
        if len(removedStudentsAssignment)==0 or ID not in removedStudentsAssignment.keys():
            return
        for i in range(len(removedStudentsAssignment[ID])):
            if ID not in self.__assignmentDict.keys():
                self.__assignmentDict.update({ID:[removedStudentsAssignment[ID][i]]})
            else:
                self.__assignmentDict[ID].append(removedStudentsAssignment[ID][i])
        del removedStudentsAssignment[ID]
    
    def removeStudent(self,x,removedStudentsAssignment):
        '''
        When removing a student, we also need to remove him from the assignmentDict
        He will be here, only if he was given an assignment
        INPUT:X-COMMAND(STRING)//remove student <studentID>
            removedStudentsAssignment-dict
            ^^ this has the form:
        {studentID:[list of assignments of student],...}
            
        '''
        v=x.split(" ")
        studentID=int(v[2])
        if studentID in removedStudentsAssignment.keys():
            del removedStudentsAssignment[studentID]
        if studentID in self.__assignmentDict.keys():
            removedStudentsAssignment.update({studentID:self.__assignmentDict[studentID]})
            del self.__assignmentDict[studentID]
    
    def restoreAssignments(self,removedAssignments,assignmentID):
        '''
        removedAssignments={assignmentID:[studentsID],....}
                                             ^students who had this assignment
        '''       
        if len(removedAssignments)==0 or assignmentID not in removedAssignments.keys():
            return
        for assignmentID in removedAssignments.keys():
            for i in range (len(removedAssignments[assignmentID])):
                studentID=removedAssignments[assignmentID][i]
                if studentID not in self.__assignmentDict.keys():
                    self.__assignmentDict.update({studentID:[assignmentID]})
                else:
                    self.__assignmentDict[studentID].append(assignmentID)
        del removedAssignments[assignmentID]
            
        
    def removeAssignment(self,x,removedAssignments):    
        '''
        When removing an assignment, we also need to remove it from the assignmentDict
        It will be here only if it was assigned to any student
        INPUT:x-command(string)//remove assignment <assignmentID>
            removedAssignments-dict
        '''
        v=x.split(" ")
        assignmentID=int(v[2])
        if assignmentID in removedAssignments.keys():
            del removedAssignments[assignmentID]
        removedAssignments.update({assignmentID:[]})
        for i in range(len(self.__idlist)):
            if self.__idlist[i] in self.__assignmentDict.keys():
                if self.__assignmentDict[self.__idlist[i]]!=[]:
                    self.__assignmentDict[self.__idlist[i]]=list(filter(lambda x: x!=assignmentID,self.__assignmentDict[self.__idlist[i]]))
                    removedAssignments[assignmentID].append(self.__idlist[i])
                    
    
    def checkLateDeadline(self,day,month):
        now = datetime.datetime.now()
        currentDay=now.day
        currentMonth=now.month 
        if currentMonth>month:
            return True
        else:
            if currentMonth==month:
                if currentDay>day:
                    return True
        return False
                      
    def getLate(self):
        repoOfLateStudents=Repository()
        for i in range(len(self.__idlist)):
            studentID=self.__idlist[i]
            assignmentsOfStudent=self.__assignmentDict[studentID]
            #we look into the assignments of the student w/ studentID
            for j in range(len(assignmentsOfStudent)):
                assignmentFound=self.__repoAssignments.search(assignmentsOfStudent[j])
                deadline=assignmentFound.get_deadline()
                date=deadline.split(".")
                day=int(date[0])
                month=int(date[1])
                if self.checkLateDeadline(day,month)==True:
                    student=self.__repoStudents.search(studentID)
                    try:
                        repoOfLateStudents.add(student)
                    except ValueError:
                        pass
        return repoOfLateStudents
 
from controllerAssignment import *
from controllerStudent import *
from undo_redo import UndoRedo
                       
class TestAssign(unittest.TestCase): 
    def setUp(self):
        self.__idlist=[1,23]
        self.__assignmentDict={}
        self.__repoStudents=Repository()
        self.__undoRedo=UndoRedo()
        #here we populate the students repository
        self.__groups={}
        self.__control=controllerStudent(self.__repoStudents,self.__undoRedo)
        x="add 23 Popescu Marin 915"
        self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        x="add 1 Boc Emil 911"
        self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        self.__repoAssignments=Repository()
        
        self.__control2=controllerAssignmnet(self.__repoAssignments,self.__undoRedo)
        #here we populate the assignment repo
        x="add 2 description prime numbers deadline 12.09"
        self.__control2.addAssignment(x)
        x="add 1 description fibonacci sequence deadline 13.10"
        self.__control2.addAssignment(x)
        
        self.__assign=Assign(self.__idlist,self.__assignmentDict,self.__repoStudents,self.__repoAssignments,self.__groups,self.__undoRedo) 
        
    def tearDown(self):
        self.__assign=None
        self.__idlist=None
        self.__assignmentDict=None
        self.__repoStudents=None
        self.__repoAssignments=None
        self.__groups=None
        self.__control=None
        self.__control2=None
        self.__assign=None
       
    def test_assignToStudent(self):
        x='student 1 assignment 2'
        self.__assign.assignToStudent(x)  
        with self.assertRaises(ValueError):
            x='student 1 assignment 2'
            self.__assign.assignToStudent(x)
        x='deassignStudent 1 2'
        self.__assign.deassignStudent(x)
        x='student 1 assignment 3'
        self.__assign.assignToStudent(x) 
        
    def test_assignToGroup(self):
        x='group 911 assignment 2'
        self.__assign.assignToGroup(x)
        with self.assertRaises(ValueError):
            x='group 911 assignment 2'
            self.__assign.assignToGroup(x)
        with self.assertRaises(ValueError):
            x='group 9 assignment 2'
            self.__assign.assignToGroup(x)
        x='deassignGroup 911 2'
        self.__assign.deassignGroup(x)
        x='group 911 assignment 2'
        self.__assign.assignToGroup(x)
            
    def test_removeStudent(self):
        x='remove student 1'
        dictt={}
        self.__assign.removeStudent(x,dictt)
        assert len(self.__assignmentDict)==1
        assert 1 not in self.__assignmentDict.keys()
        
    def test_removeAssignment(self):
        x='remove assignment 1'
        self.__assign.removeAssignment(x,{})
        assert self.__assignmentDict[1]==[]
        
    def test_checkLateDeadline(self):
        assert self.__assign.checkLateDeadline(31,12)==False
        assert self.__assign.checkLateDeadline(1, 9)==True
        assert self.__assign.checkLateDeadline(30, 11)==True
        assert self.__assign.checkLateDeadline(2,11)==True
    
    def test_late(self):
        x='group 911 assignment 2'
        self.__assign.assignToGroup(x)
        lst=self.__assign.getLate()
        assert len(lst)==1
        
    def test_restoreStudents(self):
        removedStudents={23:[2,3],3:[2]}
        self.__assign.restoreStudents(removedStudents, 23)
        assert len(self.__assignmentDict[23])==2
        self.__assign.restoreStudents(removedStudents, 23)
        assert len(self.__assignmentDict[23])==2
    
    def test_restoreAssignments(self):
        removedAssignments={2:[23,45],3:[23]}
        self.__assign.restoreAssignments(removedAssignments, 2)
        assert len(self.__assignmentDict[23])==2
        self.__assign.restoreAssignments(removedAssignments, 3)
        assert len(self.__assignmentDict[23])==2
                