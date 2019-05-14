import unittest
import json
class Student:
    '''
    THIS CLASS IS USED FOR MODELLING A STUDENT
    A STUDENT HAS :
        AN ID=A NATURAL NUMBER
        A NAME=A STRING. A STUDENT CAN HAVE 2 OR 3 NAMES. THE PRENOMS ARE SEPPARTED BY '-'
        A GROUP=A NATURAL NUMBER. EACH STUDENT BELONGS TO A GROUP
    '''
    def __init__(self,ID,name,group):
        '''
        ID=integer>0
        name=string
        group=integer>0
        '''
        self.__ID=ID
        self.__name=name
        self.__group=group
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)   
        
    def get_id(self):
        return self.__ID
    
    def get_name(self):
        return self.__name
    
    def get_group(self):
        return self.__group
    
    def __str__(self):
        return str(self.__ID)+", "+str(self.__name)+", "+str(self.__group)

    ID = property(get_id, None, None)
    name = property(get_name, None, None)
    group = property(get_group, None, None)

    def validateStudent(self):
        if self.get_id()<=0:
            raise ValueError("ID cannot be a negative number or equal to 0!")
        if self.get_group()<=0:
            raise ValueError("The group number cannot be negative or 0!")
        if len(self.get_name().split(" "))!=2:
            raise ValueError("The name is incomplete!")  
         
    def __lt__(self,other):
        return self.get_name()[0]<other.get_name()[0]
    
    def __eq__(self,other):
        return self.get_id()==other.get_id()
    
    
'''
HERE IS THE CLASS USED TO TEST THE MODEL
'''
class TestModelStudent(unittest.TestCase):
    def setUp(self):
        self.__id=23
        self.__name='Popa Ion'
        self.__group=915
        self.__id2=-4
        self.__student2=Student(self.__id2,self.__name,self.__group)
    
    def tearDown(self):
        self.__id=None
        self.__id2=None
        self.__group=None
        self.__name=None
        self.__student2=None
    
    def test_getters(self):
        student1=Student(self.__id,self.__name,self.__group)
        self.assertEqual(self.__id,student1.get_id())
        assert self.__name==student1.get_name()
        assert self.__group==student1.get_group()
        assert str(student1)=='23, Popa Ion, 915'
        student2=Student(34,'Alecu Ion',915)
        self.assertFalse(student1<student2) 
        self.assertFalse(student1==student2)
        
    def test_validate(self):
        with self.assertRaises(ValueError):
            self.__student2.validateStudent()
        with self.assertRaises(ValueError):
            student3=Student(self.__id,'Ion',self.__group)
            student3.validateStudent()
        with self.assertRaises(ValueError):
            student3=Student(self.__id,self.__name,-97)
            student3.validateStudent()
            
        
        
        


