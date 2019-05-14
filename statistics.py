from controllerGrades import *
from assigning import *


class Statistics():
    def __init__(self,__idlist,__repoGrades,__assignmentDict,__repoStudents):
        self.__repoGrades=__repoGrades
        self.__idlist=__idlist
        self.__assignmentDict=__assignmentDict
        self.__repoStudents=__repoStudents
    
    def findTheGrades(self):
        '''
        HERE WE WANT TO COMPUTE A DICTIONARY WHERE:
            THE KEYS ARE THE STUDENTS' ID'S
            THE VALUES=LISTS OF THIS FORM:[sumOfGrades,numberOfGrades]. WE DO THIS IN ORDER TO BE ABLE TO FIND THE AVERAGE GRADE
            OF EACH STUDENT
        OUPTUT:dictOfStudentsGrades=the kind of dict explained above
        '''
        dictOfStudentsGrades={}
        lstGrades=self.__repoGrades.getAll()
        if len(lstGrades)==0:
            raise ValueError("There are no grades!")
        for i in range(len(lstGrades)):
            grade=lstGrades[i]
            studentID=grade.get_student_id()
            if studentID not in dictOfStudentsGrades.keys():
                gradeValue=grade.get_grade()
                dictOfStudentsGrades.update({studentID:[gradeValue,1]})
            else:
                gradeValue=grade.get_grade()
                dictOfStudentsGrades[studentID][0]+=gradeValue
                dictOfStudentsGrades[studentID][1]+=1      
        return dictOfStudentsGrades     
    
    def findAverage(self,dictOfStudentsGrades):
        '''
        THIS FUNCTION WILL COMPUTE THE AVERAGE GRADE FOR EVERY STUDENT
        INPUT:dictOfStudentsGrades=DICT
        PRECODNTION:dictOfStudentsGrades has the fllowing meaning:
            THE KEYS ARE THE STUDENTS' ID'S
            THE VALUES=LISTS OF THIS FORM:[sumOfGrades,numberOfGrades]. WE DO THIS IN ORDER TO BE ABLE TO FIND THE AVERAGE GRADE
            OF EACH STUDENT
        OUTPUT:listOfAverageGrade=list
        POSTCONDITION: THIS LIST WILL HAVE THE FOLLOWING MEANING:
            [[studentID,averageGrade],[studentID1,averageGrade1],...]
        '''
        listOfAverageGrade=[]
        for i in self.__idlist:
            if i in dictOfStudentsGrades.keys():
                sumOfGrades=dictOfStudentsGrades[i][0]
                numberOfGrades=dictOfStudentsGrades[i][1]
                averageGrade=sumOfGrades/numberOfGrades
                listOfAverageGrade.append([i,averageGrade])

        return listOfAverageGrade
    
    def sortList(self,listOfAverageGrades):
        '''
        THIS FUNCTION SORTS A LIST OF LISTS BY THE SECOND ELEMENT
        INPUT:listOfAverageGrades=list
        PRECONDITION:THIS LIST HAS THE FOLLOWING MEANING:
            [[studentID(or assignmnetID),averageGrade],[studentID1(or assignmnetID1),averageGrade1],...]
        OUTPUT:the sorted list
        
        THIS WILL ALSO WORK EHNE WE WANT TO SORT THE LIST OF AVERAGE GRADES OF ASSIGNMENTS
        '''
        listOfAverageGrades.sort(key=lambda x:x[1],reverse=True)
        return listOfAverageGrades
        
            
    def top(self):
        '''
        THIS FUNCTION COMPUTES THE LIST OF TOP STUDENTS
        OUTPUT:listTop=the list with the id's of the best students, in descending order of their average grade
        '''
        dictOfStudentsGrades=self.findTheGrades()
        listOfAverageGrades=self.findAverage(dictOfStudentsGrades)
        listTop=self.sortList(listOfAverageGrades)
        return listTop
    
    def findAssignmnetsWithGrades(self):
        '''
        THIS FUNCTION WILL FIND ALL THE ASSIGNMENT THAT HAVE BEEN GRADED
        OUTPUT:dictOfAssignmentWithGrades=dict
        POSTCONDITION: THIS DICT WILL BE OF THE FOLLOWING FORM:
        {assignmnetID1:[sumOfGrades,numberOfGrades],assignmentID2:[sumOfGrades2,numberOfGrades2],...}
        '''
        dictOfAssignmentsWithGrades={}
        listGrades=self.__repoGrades.getAll()
        if len(listGrades)==0:
            raise ValueError("There are no grades!")
        for i in range(len(listGrades)):
            grade=listGrades[i]
            assignmentID=grade.get_id()
            if assignmentID not in dictOfAssignmentsWithGrades:
                gradeValue=grade.get_grade()
                dictOfAssignmentsWithGrades.update({assignmentID:[gradeValue,1]})
            else:
                gradeValue=grade.get_grade()
                dictOfAssignmentsWithGrades[assignmentID][0]+=gradeValue
                dictOfAssignmentsWithGrades[assignmentID][1]+=1
        return dictOfAssignmentsWithGrades
    
    def findAverageAssignments(self,dictOfAssignmnetsWithGrades):
        '''
        THIS FUNCTION WILL COMPUTE THE AVERAGE GRADE FOR EVERY ASSIGNMENT
        INPUT:dictOfAssignmentsWithGrades=dict
        POSTCONDITION:THIS DICT IS OF OF THE FOLLOWING FORM:
        {assignmnetID1:[sumOfGrades,numberOfGrades],assignmentID2:[sumOfGrades2,numberOfGrades2],...}
        OUTPUT:listOfAvgGrades=list
        POSTCONDITION: THE LIST WILL BE OF THE FORM:
        [[assignmnetID1,avgGrade1],[assignmentID2,avgGrade2],....]
        '''  
        listOfAvgGrades=[]
        for i in dictOfAssignmnetsWithGrades.keys():
            assignmentID=i
            sumOfGrades=dictOfAssignmnetsWithGrades[i][0]
            numberOfGrades=dictOfAssignmnetsWithGrades[i][1]
            avg_grade=sumOfGrades/numberOfGrades
            listOfAvgGrades.append([assignmentID,avg_grade])
        return listOfAvgGrades
            
    def all(self):
        '''
        THIS FUNCTION WILL COMPUTE A LIST OF THE FOLLOWING:
        [[assignmnetID,average_grade_at_that_assignment],[assignmnetID1,average_grade_at_that_assignment],....]
        AND THIS LIST WILL BE SORTED IN DESCENDING ORDER BY THE AVG GRADE
        OUTPUT:listAll=the list explained above
        '''
        dictOfAssignmentsWithGrades=self.findAssignmnetsWithGrades()
        listOfAverageGrades=self.findAverageAssignments(dictOfAssignmentsWithGrades)
        listAll=self.sortList(listOfAverageGrades)
        return listAll
    
    def getStudents(self,assignmentID):
        '''
        THIS FUNCTION WILL FIND ALL THE STUDENTS THAT HAVE RECIEVED A GIVEN ASSIGNMENT
        INPUT:ASSIGNMNETid=integer>0
        OUTPUT:listOfStudents=THE LIST OF STUDENTS 
        WE WILL USE THE self.__assignmentDict:
        ->the assignment dict will have as keys the students' id and as value the
        list of assignments that were assigned to the student with that id. The list of assignments
        also represents the list of ungraded assignments.
        '''
        listOfStudents=[]
        for studentID in self.__assignmentDict.keys():
            if assignmentID in self.__assignmentDict[studentID]:
                listOfStudents.append(studentID)
        if listOfStudents==[]:
            raise ValueError("No student received this assignment!")
        return listOfStudents
    
    def swap(self,i,j,lstStd):
        '''
        THIS FUNCTION SWAPS 2 ELEMENTS
        INPUT:I,J,INTEGERS>=0, REPRESENTED THE POSITIONS
            LSTSTD=THE LIST IN WHICH WE WANT TO SWAP
        '''
        student1=lstStd[i]
        student2=lstStd[j]
        lstStd[i]=student2
        lstStd[j]=student1
        
    def sortAlpha(self,listOfStudents):
        '''
        THIS FUNCTION WILL SORT THE STUDENTS BY NAME 
        INPUT:listOfStudents=list// it contains only the id's of the students
        OUTPUT:the sorted list will be returned(it will contain the students)
        '''
        
        repoStud=Repository()
        for studentID in listOfStudents:
            student=self.__repoStudents.search(studentID)
            repoStud.add(student)
        lstStd=repoStud.getAll()
        lstStd.sort()
        return lstStd
    
    def stat(self,command):
        '''
        THIS FUNCTION WILL COMPUTE THE LIST OF STUDENTS THAT WHERE ASSIGNED A GIVEN ASSIGNMENT,ORDERED ALPHABETICALLY
        INPUT:command=string=the command input by the user//stat assignment <assignmentID> alpha
        OUTPUT:listStat=list
        '''
        v=command.split(" ")
        assignmentId=int(v[2])
        listOfStudents=self.getStudents(assignmentId)
        if v[len(v)-1]=='alpha':
            listStat=self.sortAlpha(listOfStudents)
        return listStat
        
'''
HERE IS THE CLASS FOR TESTING THE STATISTTICS CLASS
'''
from undo_redo import UndoRedo
class testStatistics(unittest.TestCase):
    def setUp(self):
        self.__repoGrades=Repository()
        self.__idlist=[]
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
        x="add 2 Doc Emil 911"
        self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        
        self.__repoAssignments=Repository()
        self.__control2=controllerAssignmnet(self.__repoAssignments,self.__undoRedo)
        #here we populate the assignment repo
        x="add 2 description prime numbers deadline 12.09"
        self.__control2.addAssignment(x)
        x="add 1 description fibonacci sequence deadline 13.10"
        self.__control2.addAssignment(x)
        self.__controllerGrades=ControllerGrades(self.__repoGrades,self.__repoStudents,self.__repoAssignments,self.__idlist,self.__assignmentDict,self.__undoRedo)
        self.__statistics=Statistics(self.__idlist,self.__repoGrades,self.__assignmentDict,self.__repoStudents)  
        self.__assign=Assign(self.__idlist,self.__assignmentDict,self.__repoStudents,self.__repoAssignments,self.__groups,self.__undoRedo) 
        
    def tearDown(self):
        self.__undoRedo=None
        self.__repoGrades=None
        self.__statistics=None
        self.__assign=None
        self.__idlist=None
        self.__assignmentDict=None
        self.__repoStudents=None
        self.__repoAssignments=None
        self.__groups=None
        self.__control=None
        self.__control2=None
        self.__assign=None
    
    def test_Top_by_pieces(self):
        with self.assertRaises(ValueError):
            dictt=self.__statistics.findTheGrades()
        
        x='group 911 assignment 2'
        self.__assign.assignToGroup(x)
        x='grade 10 to student 1 for 2'
        self.__controllerGrades.add(x)
        x='group 915 assignment 2'
        self.__assign.assignToGroup(x)
        x='grade 5 to student 23 for 2'
        self.__controllerGrades.add(x)
        x='group 911 assignment 1'
        self.__assign.assignToGroup(x)
        x='grade 8 to student 1 for 1'
        self.__controllerGrades.add(x)
        x='group 915 assignment 1'
        self.__assign.assignToGroup(x)
        x='grade 6 to student 23 for 1'
        self.__controllerGrades.add(x)
        dictt=self.__statistics.findTheGrades()
        assert dictt=={1: [18, 2], 23: [11, 2]}
        lst_avg=self.__statistics.findAverage(dictt)
        assert lst_avg==[[23, 5.5], [1, 9.0]]
        sorted1=self.__statistics.sortList(lst_avg)
        assert sorted1==[[1, 9.0], [23, 5.5]]
        listTop=self.__statistics.top()
        assert listTop==sorted1
            
    def test_All_by_piece(self):
        with self.assertRaises(ValueError):
            dictt=self.__statistics.findAssignmnetsWithGrades() 
        x='group 911 assignment 2'
        self.__assign.assignToGroup(x)
        x='grade 10 to student 1 for 2'
        self.__controllerGrades.add(x)
        x='group 915 assignment 2'
        self.__assign.assignToGroup(x)
        x='grade 5 to student 23 for 2'
        self.__controllerGrades.add(x)
        x='group 911 assignment 1'
        self.__assign.assignToGroup(x)
        x='grade 8 to student 1 for 1'
        self.__controllerGrades.add(x)
        x='student 23 assignment 1'
        self.__assign.assignToStudent(x)
        x='grade 6 to student 23 for 1'
        self.__controllerGrades.add(x)
        dictt=self.__statistics.findAssignmnetsWithGrades()
        assert dictt=={2: [15, 2], 1: [14, 2]}
        listt=self.__statistics.findAverageAssignments(dictt)
        assert listt==[[2, 7.5], [1, 7.0]]
        sortedd=self.__statistics.sortList(listt)
        assert sortedd==[[2, 7.5], [1, 7.0]]
        sorteddd=self.__statistics.all()
        assert sorteddd==sortedd
        
    def test_stat_by_pieces(self):
        with self.assertRaises(ValueError):
            listt=self.__statistics.getStudents(1)
        x='group 911 assignment 2'
        self.__assign.assignToGroup(x)
        x='group 915 assignment 2'
        self.__assign.assignToGroup(x)
        x='group 911 assignment 1'
        self.__assign.assignToGroup(x)
        x='student 23 assignment 1'
        self.__assign.assignToStudent(x)
        listt=self.__statistics.getStudents(1)
        assert listt==[23,1,2]
        sortedd=self.__statistics.sortAlpha(listt)
        assert str(sortedd[0])=='1, Boc Emil, 911'
        assert str(sortedd[1])=='2, Doc Emil, 911'
        assert str(sortedd[2])=='23, Popescu Marin, 915'
        soorted=self.__statistics.stat('stat assignment 1 alpha')
        assert soorted==sortedd
        
        