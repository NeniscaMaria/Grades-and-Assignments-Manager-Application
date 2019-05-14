import unittest
class Grade():
    '''
    THIS CLASS IS USED FOR MODELLING THE CONCEPT OF GRADE
    EVERY GRADE HAS:
        AN ASSIGNMENT ID=A NATURAL NUMBER
        A STUDENT ID=A NATURAL NUMBER\
        A GRADE VALUE=A NUMBER BETWEEEN 1 AND 10
    A STUDENT CAND BE GRADED FOR AN ASSIGNMENT
    '''
    
    def __init__(self,assignmentID,studentID,grade):
        '''
        disciplineId, studentID=integer>0
        grade_value=integer between 1 and 10
        '''
        self.__assignmentID=assignmentID
        self.__studentID=studentID
        self.__grade=grade
        
    def get_id(self):
        return self.__assignmentID


    def get_student_id(self):
        return self.__studentID


    def get_grade(self):
        return self.__grade

    assignmentID = property(get_id, None, None, None)
    studentID = property(get_student_id, None, None, None)
    grade = property(get_grade,None, None, None)
    
    def __str__(self):
        return "For assignment, "+str(self.__assignmentID)+", to student, "+str(self.__studentID)+", grade, "+str(self.__grade)
    
    def validate(self):
        if self.__assignmentID<=0:
            raise ValueError("The asignment ID must be a positive integer!")
        if self.__studentID<=0:
            raise ValueError("The student ID must be a positive integer!")
        if self.__grade<=0 or self.__grade>10:
            raise ValueError("The grade must be between 1 and 10!")
    
    def __eq__(self,other):
        return self.get_id()==other.get_id() and self.get_student_id()==other.get_id() and self.get_grade()==other.get_grade()
        
'''
HERE IS THE CLASS FOR TESTING THE MODEL OF GRADE 
'''
class testModelGrade(unittest.TestCase):
    def setUp(self):
        self.__assignmentID=2
        self.__studentId=2
        self.__gradevalue=4
        self.__grade=Grade(self.__assignmentID,self.__studentId,self.__gradevalue)
        self.__assignmentID1=-3
        self.__grade1=Grade(self.__assignmentID1,self.__studentId,self.__gradevalue)
        self.__studentId1=-3
        self.__grade2=Grade(self.__assignmentID,self.__studentId1,self.__gradevalue)
        self.__gradevalue1=11
        self.__grade3=Grade(self.__assignmentID,self.__studentId,self.__gradevalue1)
        
    def tearDown(self):
        self.__assignmentID=None
        self.__studentId=None
        self.__gradevalue=None
        self.__grade=None
        self.__assignmentID1=None
        self.__grade1=None
        self.__studentId1=None
        self.__grade2=None
        self.__gradevalue1=None
        self.__grade3=None
        
    def test_getters(self):
        assert self.__assignmentID==self.__grade.get_id()
        assert self.__studentId==self.__grade.get_student_id()
        assert self.__gradevalue==self.__grade.get_grade()
        assert str(self.__grade)=='For assignment, 2, to student, 2, grade, 4'
        assert self.__grade==self.__grade
    
    def test_validate(self):
        with self.assertRaises(ValueError):
            self.__grade1.validate()
        with self.assertRaises(ValueError):
            self.__grade2.validate()
        with self.assertRaises(ValueError):
            self.__grade3.validate()