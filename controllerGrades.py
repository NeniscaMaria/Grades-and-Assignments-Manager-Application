from model_Grade import *
from controllerStudent import *
from assigning import *
from undo_redo import UndoRedo,Operation,FunctionCall
from repository import *
from repoIterable import filterList

class ControllerGrades:
    def __init__(self,__repo,__students,__assignments,__idlist,__assignmentDict,__undoRedo):
        self.__repoGrades=__repo
        self.__repoStudents=__students
        self.__repoAssignments=__assignments
        self.__idlist=__idlist
        self.__assignmentDict=__assignmentDict
        self.__undoRedo=__undoRedo
        
        
    def createStudentWithGrades(self):
        '''
        THIS FUNCTION CREATES A DICTIONARY WITH THE FOLLOWING:
        KEY-THE STUDENT ID
        VALUE:LIST WITH ASIGNMENTS AT WHICH THE STUDENT HAS A GRADE
        OUTPUT:-THIS DICTIONARY(studentsWithGrades)
        '''
        studentsWithGrades={}
        grades=self.__repoGrades.getAll()
        for i in range(len(grades)):
            studentID1=grades[i].get_student_id()
            assignmentID1=grades[i].get_id()
            if studentID1 not in studentsWithGrades:
                studentsWithGrades.update({studentID1:[assignmentID1]})
            else:
                studentsWithGrades[studentID1].append(assignmentID1)
        return studentsWithGrades   
        
    def add(self,x):   
        '''
        THIS FUNCTION ADDS A GRADE
        INPUT:x-THE COMMAND(STRING)//grade <grade> to student <studentID> for <assignmentID>
        After we grade a student for an assignment, we will delete the assignment from the assignmentDict from this student.
        '''
        studentsWithGrades=self.createStudentWithGrades()
        v=x.split(" ")
        gradeValue=int(v[1])
        studentID=int(v[4])
        assignmentID=int(v[6])   
        if studentID in self.__idlist:
            try:
                assignment=self.__repoAssignments.search(assignmentID)
                #now we look to see whether this students was given this assignment or not
                if studentID in studentsWithGrades.keys():
                    if assignmentID in studentsWithGrades[studentID]:
                        raise ValueError("You already graded this student for this assignment! The grades cannot be changed!")
                if assignmentID not in self.__assignmentDict[studentID]:
                    raise ValueError("You did not give to this student this assignment!")
                else:
                    grade=Grade(assignmentID,studentID,gradeValue)
                    self.__repoGrades.addForGrades(grade)
                    #here we filter the list from the studentID key by the assignmentID
                    #in other words, we remove the assignment from the student 
                    self.__assignmentDict[studentID]=list(filterList(lambda x: x!=assignmentID,self.__assignmentDict[studentID]))
            except ValueError as ve:
                raise ValueError(ve)
        else:
            raise ValueError("This student does not exist!")
        
    def restoreGradesAssignment(self,assignmentID,removedAssignments):
        '''
        this function restores the grades from a given assignment. useful for undo
        input: assignmentID=integer positive
            removedAssignments is of the form:
        {assignmentID:[all the grades of this assignment],assignmentID1:[the same],...}
        this will come in handy when we will undo the removing of an assignment
        '''
        if assignmentID in removedAssignments.keys():
            for i in range(len(removedAssignments[assignmentID])):
                grade=removedAssignments[assignmentID][i]
                self.__repoGrades.addForGrades(grade)
            del removedAssignments[assignmentID]
            
    def removeGrade(self,x):
        '''
        THIS IS A HELPING FUNCTION WHEN IT COMES TO UNDOING/REDOING THE ADDITION OF A GRADE
        INPUT X=THE COMMAND/removeGrade <grade> from student <studentID> for <assignmentID>
        '''
        v=x.split(" ")
        gradeValue=v[1]
        studentID=v[4]
        assignmentID=v[6]
        gradeToDelete=Grade(assignmentID,studentID,gradeValue)
        self.__repoGrades.removeForGrades(gradeToDelete)
        #we add the assignment back to the student.Useful when it comes to undo/redo
        if studentID not in self.__assignmentDict.keys():
            self.__assignmentDict.update({int(studentID):[int(assignmentID)]})
        else:
            self.__assignmentDict[studentID].append(int(assignmentID))
        
        
    def removeAssignment(self,x,removedAssignments):
        '''
        When removing an assignment,we also need to remove the grades at that assignment, if they exist
        INPUT:x-command(string)//remove assignment <assignmentID>
            removedAssignments - dict\'''
        removedAssignments is of the form:
        {assignmentID:[all the grades of this assignment],assignmentID1:[the same],...}
        this will come in handy when we will undo the removing of an assignment
        '''
        v=x.split(" ")
        assignmentID=int(v[2])
        if assignmentID in removedAssignments.keys():
            '''
            if an assignment with this id exists in the dict of removed assignments, it means that an assignment with 
            this id was removed and, afterwards, an assignment with the same id was added
            '''
            del removedAssignments[assignmentID]
        removedAssignments.update({assignmentID:[]})
        for i in range(len(self.__repoGrades)):
            lst=self.__repoGrades.getAll()
            if i<len(lst):
                if lst[i].get_id()==assignmentID:
                    grade=lst[i]
                    self.__repoGrades.removeForGrades(grade)
                    removedAssignments[assignmentID].append(grade)
                    
    def restoreStudentGrades(self,studentID,removedStudents):
        '''
        THIS FUNCTION RESTORES ALL THE GRADES THAT A STUDENT
        COMES IN HANDY WHEN WE WANT TO UNDO THE REMOVING OF A STUDENT
        INPUT:STUDENTID=INTEGER POSTIVE
            removedStudents is of the form:
        {studentID:[all the grades that this student had],studentID1:[the same],...}
        this will come in handy when we will undo the removing of a student
        '''
        if studentID in removedStudents.keys():
            for i in range(len(removedStudents[studentID])):
                grade=removedStudents[studentID][i]
                self.__repoGrades.addForGrades(grade)    
            del removedStudents[studentID]     
                
    def removeStudent(self,x,removedStudents):
        '''
        When removing a student, we need to remove his grades, too
        INPUT:x-command(string)//remove student <studentID>
            removedStudents is of the form:
        {studentID:[all the grades that this student had],studentID1:[the same],...}
        this will come in handy when we will undo the removing of a student
        '''
        v=x.split(" ")
        studentID=int(v[2])
        if studentID in removedStudents.keys():
            '''
            if this id is already in the dict of removed students, it means that a student with this id 
            was removed and afterwards a new student with the same id was added
            '''
            del removedStudents[studentID]
        removedStudents.update({studentID:[]})
        if len(self.__repoGrades)==0:
            return
        for i in range(len(self.__repoGrades)):
            lst=self.__repoGrades.getAll()
            if lst[i].get_student_id()==studentID:
                self.__repoGrades.removeForGrades(lst[i])
                removedStudents[studentID].append(lst[i])

'''
HERE IS THE CLASS FOR TESTING THE CONTROLLERGRADES
'''
class testControllerGrades(unittest.TestCase):
    def setUp(self):
        self.__idlist=[1,23]
        self.__assignmentDict={}
        self.__repoGrades=Repository()
        self.__undoRedo=UndoRedo()
        
        self.__repoStudents=Repository()
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
        
        self.__controllerGrades=ControllerGrades(self.__repoGrades,self.__repoStudents,self.__repoAssignments,self.__idlist,self.__assignmentDict,self.__undoRedo)
        self.__assign=Assign(self.__idlist,self.__assignmentDict,self.__repoStudents,self.__repoAssignments,self.__groups,self.__undoRedo)
        
    def tearDown(self):
        self.__idlist=None
        self.__assignmentDict=None
        self.__repoGrades=None
        self.__repoStudents=None
        self.__groups=None
        self.__repoAssignments=None
        self.__control2=None
        self.__controllerGrades=None
        self.__control=None
        self.__control2=None
        self.__assign=None
        self.__undoRedo=None 
    
    def testcontrollerUpToRemoveAssignment(self):
        x='group 911 assignment 2'
        self.__assign.assignToGroup(x)
        x='grade 5 to student 1 for 2'
        self.__controllerGrades.add(x)
        with self.assertRaises(ValueError):
            self.__controllerGrades.add(x)
        with self.assertRaises(ValueError):
            x='grade 5 to student 1 for 1'
            self.__controllerGrades.add(x)
        with self.assertRaises(ValueError):
            x='grade 5 to student 45 for 1'
            self.__controllerGrades.add(x)
        lst=self.__repoGrades.getAll()
        assert(len(lst))==1
        x='group 911 assignment 1'
        self.__assign.assignToGroup(x)
        x='grade 5 to student 1 for 1'
        self.__controllerGrades.add(x)
        lst2=self.__controllerGrades.createStudentWithGrades()
        assert len(lst2)==1
        x='remove assignment 2'
        dictt={}
        self.__controllerGrades.removeAssignment(x,dictt)
        lst=self.__repoGrades.getAll()
        #assert len(lst)==1
        
    def testremoveStudent(self):
        x='group 911 assignment 2'
        self.__assign.assignToGroup(x)
        x='grade 5 to student 1 for 2'
        self.__controllerGrades.add(x)
        x='remove student 1'
        dictt={}
        self.__controllerGrades.removeStudent(x,dictt)
        lst=self.__repoGrades.getAll()
        print(lst)
        
    def test_restore_assignments(self):
        removedAssignments={23:[Grade(23,2,4)],2:[Grade(2,3,4)]}
        assignmentID=23
        self.__controllerGrades.restoreGradesAssignment(assignmentID, removedAssignments)
        assert len(self.__repoGrades)==1
        self.__controllerGrades.removeGrade("removegrade 4 from student 2 for 23")
        assert len(self.__repoGrades)==0
        
    def test_restore_studentsgrades(self):
        studentID=2
        removedStudents={2:[Grade(2,2,2)]}
        self.__controllerGrades.restoreStudentGrades(studentID, removedStudents)
        assert len(self.__repoGrades)==1