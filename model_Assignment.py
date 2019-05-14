import unittest

class Assignment:
    '''
    THIS CLASS IS USED TO MODEL THE CONCEPT OF ASSIGNMENT
    EVERY ASSIGNMENT HAS:
        AN ID=A UNIQUE NATURAL NUMBER
        A DESCRIPTION=A STRING
        A DEADLINE=A STRING IN DATE FORMAT: DD/MM
    '''
    
    def __init__(self,ID,description,deadline):
        '''
        ID=integer>0
        description,deadline=string// deadline is in date format
        '''
        self.__ID=ID
        self.__description=description
        self.__deadline=deadline

    def set_description(self, value):
        self.__description = value
        
    def set_deadline(self, value):
        self.__deadline = value
        
    def get_id(self):
        return self.__ID


    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline

    def __str__(self):
        return str(self.__ID)+", description, "+str(self.__description)+", deadline,"+str(self.__deadline)
    
    def __eq__(self,other):
        return self.get_id()==other.get_id()
    
    ID = property(get_id, None, None, None)
    description = property(get_description,set_description, None, None)
    deadline = property(get_deadline, set_deadline, None, None)
    
    def validate(self):
        if self.__ID<=0:
            raise ValueError("The ID must be a positive number!")
        if len(self.__deadline.split("."))!=2:
            raise ValueError("Incomplete deadline!")
        x=self.__deadline.split(".")
        if x[0].isdigit()==False or x[1].isdigit()==False:
            raise ValueError("The deadline must contain numbers!")
    
'''
HERE IS THE CLASS USED TO VARIFY THE MODEL OF ASSIGNMENT
'''
class TestModelAssignment(unittest.TestCase):
    def setUp(self):
        self.__id=23
        self.__id1=-7
        self.__description="prime numbers"
        self.__deadline='1.2'
        self.__deadline2='2.martie'
        self.__assignment=Assignment(self.__id,self.__description,self.__deadline)
        self.__assignment1=Assignment(self.__id1,self.__description,self.__deadline)
        self.__assignment2=Assignment(self.__id,self.__description,self.__deadline2)
        
    def tearDown(self):
        self.__id=None
        self.__id1=None
        self.__description=None
        self.__deadline=None
        self.__deadline2=None
        self.__assignment1=None
        self.__assignment1=None
        self.__assignment=None
    
    def test_getters_and_setter(self):
        assert self.__id==self.__assignment.get_id()
        assert self.__description==self.__assignment.get_description()
        assert self.__deadline==self.__assignment.get_deadline()
        assert str(self.__assignment)=='23, description, prime numbers, deadline,1.2'
        self.__assignment.set_description('fibonacci')
        assert self.__assignment.get_description()=='fibonacci'
        self.__assignment.set_deadline('3.2')
        assert self.__assignment.get_deadline()=='3.2'
        self.assertTrue(self.__assignment==self.__assignment)
        
    def test_validate(self):
        with self.assertRaises(ValueError):
            self.__assignment1.validate()
        with self.assertRaises(ValueError):
            self.__assignment2.validate()
        with self.assertRaises(ValueError):
            assignment3=Assignment(2,'sss','23')
            assignment3.validate()
            
        