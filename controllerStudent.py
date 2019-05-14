from model_Student import *
from undo_redo import UndoRedo,Operation,FunctionCall
from repository import Repository,FileRepository,BinaryRepository
from repoIterable import filterList

class controllerStudent():
    def __init__(self,__repo,__undoRedo):
        self.__repo=__repo
        self.__undoRedo=__undoRedo
    
    def addStudent(self,x,groups,idlist,assignmentDict):
        '''
        THIS FUNCTION ADDS A NEW STUDENT TO THE LIST OF STUDENTS:
        INPUT_X-STRING
            STUDENTS=CLASS REPOSITORY
        PRECOND:X=THE COMMAND(STRING)=ADD <STUDENTID> <STUDENTNAME>
        OUTPUT-
        POSTCOND:-
        '''
        v=x.split()
        ID=int(v[1])
        name=v[2]+" "+v[3]
        group=int(v[4])
        newStudent=Student(ID,name,group)
        try:
            self.__repo.add(newStudent)
            idlist.append(ID)
            assignmentDict.update({ID:[]})
        except ValueError:
            raise ValueError("There already exists a student with this ID!")
        if group not in groups.keys():
            groups.update({group:[ID]})
        else:
            groups[group].append(ID)
        
        
    def removeStudent(self,x,groups):
        '''
        THIS FUNCTION REMOVES A STUDENT FROM THE LIST
        INPUT:X=COMMAND(STRING)=remove student <studentID>
            groups=dict with keys=ne group number, values=[the students id]
            assignmentDict=the keys=student ID, the values=the assignments of each student
        OUTPUT:-
        '''
        v=x.split(" ")
        ID=int(v[2])
        try:
            studentToDelete=self.__repo.search(ID)
        except ValueError:
            raise ValueError("This student does not exist!")
        self.__repo.remove(studentToDelete)
        group=studentToDelete.get_group()
        #here we remove the ID from the group
        groups[group]=list(filterList(lambda x: x!=ID,groups[group])) 
        return 'add '+str(ID)+" "+studentToDelete.get_name()+" "+str(group)
        
    def updateStudent(self,x,groups):
        '''
        THIS FUNCTION UPDATES A STUDENT'S GROUP FROM THE LIST
        INPUT:X-COMMAND(STRING)=update student <studentID> <studentGroup>
            groups-dict as follows:{groupNo:[studentIDs],..}
        OUTPUT:-
        '''
        v=x.split()
        ID=int(v[2])
        group=int(v[3])
        if group not in groups:
            raise ValueError("This group does not exist!")
        studentFound=self.__repo.search(ID)
        if group==studentFound.get_group():
            raise ValueError("This student is already in this group!")
        name=studentFound.get_name()
        newStudent=Student(ID,name,group)
        self.__repo.update(newStudent)
        command='update student '+str(ID)+" "+str(studentFound.get_group())
        return command
        
        
class TestControllerStudents(unittest.TestCase):
    def setUp(self):
        self.__repo=Repository()
        self.__groups={}
        self.__idlist=[]
        self.__assignmentDict={}
        self.__undoRedo=UndoRedo()
        self.__control=controllerStudent(self.__repo,self.__undoRedo)
        

    def tearDown(self):
        self.__repo=None
        self.__groups=None
        self.__idlist=None
        self.__assignmentDict=None
        self.__control=None
        self.__undoRedo=None
        
    def test_addStudent(self):
        x="add 23 Popescu Marin 915"
        self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        with self.assertRaises(ValueError):
            self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        lst=self.__repo.getAll()
        x="add 2 Popescu Maria 915"
        self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        assert str(lst[0])=="23, Popescu Marin, 915"
        
    def test_removeStudent(self):
        x="add 23 Popescu Marin 915"
        self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        x="add 45 Boc Emil 911"
        self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        x="remove student 23"
        self.__control.removeStudent(x,self.__groups)
        with self.assertRaises(ValueError):
            x='remove student 1000'
            self.__control.removeStudent(x,self.__groups)
        lst=self.__repo.getAll()
        assert str(lst[0])=='45, Boc Emil, 911'  
        
    def test_updateStudent(self):
        x="add 45 Boc Emil 911"
        self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        x='add 48 Dorin Mihai 912'
        self.__control.addStudent(x,self.__groups,self.__idlist,self.__assignmentDict)
        x='update student 45 912'
        dictt={911:[45],912:[48]}
        self.__control.updateStudent(x,dictt)
        lst=self.__repo.getAll()
        assert str(lst[0])=='45, Boc Emil, 912'
        with self.assertRaises(ValueError):
            x='update student 100 912'
            self.__control.updateStudent(x,self.__groups)
        with self.assertRaises(ValueError):
            x='update student 100 789'
            self.__control.updateStudent(x, self.__groups)
        with self.assertRaises(ValueError):
            x='update student 45 912'
            self.__control.updateStudent(x, self.__groups)
            