from model_Assignment import *
from undo_redo import UndoRedo,Operation,FunctionCall
from repository import *


class controllerAssignmnet():
    def __init__(self,__repo,__undoRedo):
        self.__repo=__repo
        self.__undoRedo=__undoRedo
        
    def addAssignment(self,x):
        '''
        THIS FUNCTION ADDS AN ASSIGNMENT
        INPUT: X-THE COMMAND(STRING)// add <assignmentID> description <assignmentDescription> deadline <assignmentDeadline>
        '''
        v=x.split()
        ID=int(v[1])
        description=""
        i=3
        while v[i]!='deadline':
            description+=v[i]+" "
            i+=1
        deadline=v[len(v)-1]
        newAssignment=Assignment(ID,description,deadline)
        try:
            self.__repo.add(newAssignment)
        except ValueError:
            raise ValueError("An element with this ID already exists!")
            
    def removeAssignment(self,x):
        '''
        THIS FUNCTION REMOVES AN ASSIGNMENT
        INPUT: X-THE COMMAND(STRING)//remove assignment <assignmentID>
        '''
        v=x.split(" ")
        ID=int(v[2])
        assignmentToDelete=self.__repo.search(ID)
        self.__repo.remove(assignmentToDelete)
        command="add "+str(ID)+" description "+str(assignmentToDelete.get_description())+"deadline "+str(assignmentToDelete.get_deadline())
        return command

    def updateAssignment(self,x):
        '''
        THIS FUNCTION UPDATES AN ASSIGNMENT
        INPUT:X-THE COMMAND(STRING)//update assignment <assignmentID> description <assignmentDescription> deadline <assignmnetDeadline>
        '''
        v=x.split(" ")
        ID=int(v[2])
        assignment=self.__repo.search(ID)
        command="update assignment "+str(assignment.get_id())+" description "+str(assignment.get_description())+" deadline "+str(assignment.get_deadline())
        description=""
        i=4
        while v[i]!='deadline':
            description+=v[i]+" "
            i+=1
        deadline=v[len(v)-1]
        assignmentToUpdate=Assignment(ID,description,deadline)
        self.__repo.update(assignmentToUpdate)
        return command

class TestControllerAssignments(unittest.TestCase):
    def setUp(self):
        self.__repo2=Repository()
        self.__undoRedo=UndoRedo()
        self.__control2=controllerAssignmnet(self.__repo2,self.__undoRedo)
        
        
    def tearDown(self):
        self.__control2=None
        self.__undoRedo=None 
        
    def test_addAssignment(self):
        x="add 234 description prime numbers deadline 12.09"
        self.__control2.addAssignment(x)
        with self.assertRaises(ValueError):
            self.__control2.addAssignment(x)
        lst=self.__repo2.getAll()
        assert str(lst[0])=="234, description, prime numbers , deadline,12.09"
        
    def test_removeAssignment(self):
        x="add 234 description prime numbers deadline 12.09"
        self.__control2.addAssignment(x)
        x="add 345 description fibonacci sequence deadline 13.10"
        self.__control2.addAssignment(x)
        x="remove assignment 345"
        self.__control2.removeAssignment(x)
        with self.assertRaises(ValueError):
            x="remove assignment 1000"
            self.__control2.removeAssignment(x)
        lst=self.__repo2.getAll()
        assert str(lst[0])=='234, description, prime numbers , deadline,12.09'
        
    def test_updateAssignment(self):

        x="add 123 description numbers deadline 1.10"
        self.__control2.addAssignment(x)
        x="update assignment 123 description prime numbers deadline 12.3"
        self.__control2.updateAssignment(x)
        lst=self.__repo2.getAll()
        assert str(lst[0])=='123, description, prime numbers , deadline,12.3'
    
    
    
    
     