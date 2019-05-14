from model_Assignment import *
from model_Grade import *
from model_Assignment import *
from model_Student import *


class Repository():
    
    
    def __init__(self):
        self._elems =[]
        self._idlist=[]
    
    def __len__(self):
        return len(self._elems)
    
    def add(self,elem):
        if elem in self._elems:
            raise ValueError("This is an existing element!\n")
        if elem.get_id() in self._idlist:
            raise ValueError("This is an existing element!\n")
        self._elems.append(elem)
        self._idlist.append(elem.get_id())
    
    def addForGrades(self,elem):
        self._elems.append(elem)
          
    def search(self,ID):
        for x in self._elems:
            if x.get_id() == ID:
                return x
        raise ValueError("There is no such element!\n")
    
    def update(self,elem):
        
        if elem.get_id() not in self._idlist:
            raise ValueError("This element does not exist!\n")
        for i in range(len(self._elems)):
            if type(elem)==Assignment:
                if self._elems[i].get_id()==elem.get_id():
                    if str(elem.get_description()).strip()=="None":
                        self._elems[i].set_deadline(elem.get_deadline())
                    elif str(elem.get_deadline()).strip()=="None":
                        self._elems[i].set_description(elem.get_description())
                    else:
                        self._elems[i]=elem
                    return
            else:
                if self._elems[i].get_id()==elem.get_id():
                    self._elems[i]=elem
                    return           
    
    def remove(self,elem):
        
        if elem not in self._elems:
            raise ValueError("This element does not exist!\n")
        i=0
        while self._idlist[i]!=elem.get_id():
            i+=1
        del self._idlist[i]
        for i in range(len(self._elems)):
            if self._elems[i]==elem:
                del self._elems[i]
                return
    
    def removeForGrades(self,elem):
        for i in range(len(self._elems)):
            if str(self._elems[i])==str(elem):
                del self._elems[i]
                return
        raise ValueError("There exists no such grade!")
        
    def getAll(self):
        return self._elems[:]

class FileRepository(Repository):
    def __init__(self,filename):
        Repository.__init__(self)
        self.__filename=filename
        self.readFromFile()
    
    def readFromFile(self):
        try:
            with open(self.__filename,'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        if self.__filename=='assignment05_07_students.txt':
                            ID = int(words[0].strip())
                            name = words[1].strip()
                            group = int(words[2])
                            student = Student(ID,name,group)
                            self._elems.append(student)
                            self._idlist.append(ID)
                        elif self.__filename=='assignment05_07_assignments.txt':
                            ID = int(words[0].strip())
                            description=words[2].strip()+" "
                            deadline = words[4].strip()
                            assignment=Assignment(ID,description,deadline)
                            self._elems.append(assignment)
                            self._idlist.append(ID)
                        elif self.__filename=='assignment05_07_grades.txt':
                            assignmentID=int(words[1].strip())
                            studentID=int(words[3].strip())
                            gradeValue=int(words[5].strip())
                            grade=Grade(assignmentID,studentID,gradeValue)
                            self._elems.append(grade)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
    
    def __writeAllToFile(self):
        try:
            with open(self.__filename,"w") as f:
                for elem in self._elems:
                    f.write(str(elem)+"\n")
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
        

    def add(self,other):
        Repository.add(self,other)
        self.__writeAllToFile()
    
    def addForGrades(self, elem):
        Repository.addForGrades(self, elem)
        self.__writeAllToFile()

    def remove(self,elem):
        Repository.remove(self, elem)
        self.__writeAllToFile()
    
    def removeForGrades(self, elem):
        Repository.removeForGrades(self, elem)
        self.__writeAllToFile()
        
    def update(self,elem):
        Repository.update(self, elem)
        self.__writeAllToFile()
        
import pickle
   
class BinaryRepository(Repository):
    def __init__(self,filename):
        Repository.__init__(self)
        self.__filename=filename
        self.__readFile()
    
    def __readFile(self):
        if self.__filename=='assignment05_07_studentsBinary':
            for p in self.pickleRead():
                words=str(p).strip().split(",")
                ID = int(words[0].strip())
                name = words[1].strip()
                group = int(words[2])
                student = Student(ID,name,group)
                self._elems.append(student)
                self._idlist.append(ID)
        elif self.__filename=='assignment05_07_assignmentsBinary':
            for p in self.pickleRead():
                words=str(p).strip().split(",")
                ID = int(words[0].strip())
                description=words[2].strip()+" "
                deadline = words[4].strip()
                assignment=Assignment(ID,description,deadline)
                self._elems.append(assignment)
                self._idlist.append(ID)
        elif self.__filename=='assignment05_07_gradesBinary':
            for p in self.pickleRead():
                words=str(p).strip().split(",")
                assignmentID=int(words[1].strip())
                studentID=int(words[3].strip())
                gradeValue=int(words[5].strip())
                grade=Grade(assignmentID,studentID,gradeValue)
                self._elems.append(grade)

    def pickleRead(self):
        try:
            with open(self.__filename,"rb") as f:
                return pickle.load(f)
        except EOFError:
            return []
        except IOError as e:
            raise ValueError("An error occured - " + str(e))
               
    def __writeFile(self):
        try:
            with open(self.__filename,'wb') as f:
                pickle.dump(self._elems,f)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
    
    def add(self,elem):
        Repository.add(self, elem)
        self.__writeFile()
        
    def addForGrades(self, elem):
        Repository.addForGrades(self, elem)
        self.__writeFile()

    def remove(self,elem):
        Repository.remove(self, elem)
        self.__writeFile()
    
    def removeForGrades(self, elem):
        Repository.removeForGrades(self, elem)
        self.__writeFile()
        
    def update(self,elem):
        Repository.update(self, elem)
        self.__writeFile()
 
import json       
class JsonRepository(Repository):
    def __init__(self,filename):
        Repository.__init__(self)
        self.__filename=filename
        self.__readFromFile()
    
    def __readFromFile(self):
        try:
            with open(self.__filename) as f:
                data = json.load(f)
                if self.__filename=='jsonStudents':
                    for student in data['students']:
                        ID=int(student['id'])
                        name=student['name']
                        group=int(student['group'])
                        newStudent=Student(ID,name,group)
                        self._elems.append(newStudent)
                        self._idlist.append(ID)
                elif self.__filename=='jsonAssignments':
                    for assignment in data['assignments']:
                        ID=int(assignment['id'])
                        description=assignment['description']
                        deadline=assignment['deadline']
                        newassignment=Assignment(ID,description,deadline)
                        self._elems.append(newassignment)
                        self._idlist.append(ID)
                elif self.__filename=='jsonGrades':
                    for grade in data['grades']:
                        assignmentID=int(grade['assignmentID'])
                        studentID=int(grade['studentID'])
                        gradeValue=int(grade['grade'])
                        newgrade=Grade(assignmentID,studentID,gradeValue)
                        self._elems.append(newgrade)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
    
    def __writeToFile(self):
        lst=self._elems[:]
        try:
            with open(self.__filename,'w') as f:
                if self.__filename=='jsonStudents':
                    f.write('{\n\t"students":[\n')
                    for j in range(len(lst)):
                        i=lst[j]
                        ID=i.get_id()
                        name=i.get_name()
                        group=i.get_group()
                        f.write('{\n\t\t"name": "'+name+'",\n\t\t "id": "'+str(ID)+'",\n\t\t"group" :"'+str(group)+'"')
                        if j!=len(lst)-1:
                            f.write('\n},')
                        else:
                            f.write('\n}\n\t]\n}')
                elif self.__filename=='jsonAssignments':
                        f.write('{\n\t"assignments":[\n')
                        for j in range(len(lst)):
                            i=lst[j]
                            ID=i.get_id()
                            description=i.get_description()
                            deadline=i.get_deadline()
                            f.write('{\n\t\t"id": "'+str(ID)+'",\n\t\t "description": "'+description+'",\n\t\t"deadline" :"'+deadline+'"')
                            if j!=len(lst)-1:
                                f.write('\n},')
                            else:
                                f.write('\n}\n\t]\n}')
                elif self.__filename=='jsonGrades':
                        f.write('{\n\t"grades":[\n')
                        for j in range(len(lst)):
                            i=lst[j]
                            assignmentID=i.get_id()
                            studentID=i.get_student_id()
                            gradeValue=i.get_grade()
                            f.write('{\n\t\t"assignmentID": "'+str(assignmentID)+'",\n\t\t "studentID": "'+str(studentID)+'",\n\t\t"grade" :"'+str(gradeValue)+'"')
                            if j!=len(lst)-1:
                                f.write('\n},')
                            else:
                                f.write('\n}\n\t]\n}')

                
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
    
    def add(self,elem):
        Repository.add(self, elem)
        self.__writeToFile()
        
    def addForGrades(self, elem):
        Repository.addForGrades(self, elem)
        self.__writeToFile()

    def remove(self,elem):
        Repository.remove(self, elem)
        self.__writeToFile()
    
    def removeForGrades(self, elem):
        Repository.removeForGrades(self, elem)
        self.__writeToFile()
        
    def update(self,elem):
        Repository.update(self, elem)
        self.__writeToFile()

import sqlite3
class SQLRepository(Repository):
    def __init__(self,filename):
        Repository.__init__(self)
        self.__filename=filename
        self.__readFile()
    
    def __readFile(self):
        try:
            conn=sqlite3.connect(self.__filename)
            c=conn.cursor()
            with open(self.__filename,'r') as f:
                if self.__filename=='students.db':
                    c.execute("SELECT * FROM students")
                    lst=c.fetchall()
                    conn.commit()
                    for i in lst:
                        ID=i[0]
                        name=i[1]
                        group=i[2]
                        newStudent=Student(ID,name,group)
                        self._elems.append(newStudent)
                        self._idlist.append(ID)
                if self.__filename=='assignments.db':
                    c.execute("SELECT * FROM assignments")
                    lst=c.fetchall()
                    conn.commit()
                    for i in lst:
                        assignmentID=i[0]
                        description=i[1]
                        deadline=i[2]
                        newAssignment=Assignment(assignmentID,description,deadline)
                        self._elems.append(newAssignment)
                        self._idlist.append(assignmentID)
                if self.__filename=='grades.db':
                    c.execute("SELECT * FROM grades")
                    lst=c.fetchall()
                    conn.commit()
                    for i in lst:
                        assignmentID=i[0]
                        studentID=i[1]
                        gradeValue=i[2]
                        newGrade=Grade(assignmentID,studentID,gradeValue)
                        self._elems.append(newGrade)
            conn.close()
        except FileNotFoundError:
            print("Inexistent file : "+self.__filename) 
            
    def add(self,elem):
        Repository.add(self, elem)
        conn=sqlite3.connect(self.__filename)
        c=conn.cursor()
        if type(elem)==Student:
            c.execute("INSERT INTO students VALUES (:ID, :name, :groupStudent)",
                       {'ID': elem.get_id(), 'name': elem.get_name(), 'groupStudent': elem.get_group()})
        elif type(elem)==Assignment:
            c.execute("INSERT INTO assignments VALUES (:assignmentID, :description, :deadline)",
                       {'assignmentID': elem.get_id(), 'description': elem.get_description(), 'deadline': elem.get_deadline()})
        conn.commit()
        conn.close()
        
    def addForGrades(self, elem):
        Repository.addForGrades(self, elem)
        conn=sqlite3.connect(self.__filename)
        c=conn.cursor()
        c.execute("INSERT INTO grades VALUES (:assignmentID, :studentID, :gradeValue)",
                       {'assignmentID': elem.get_id(), 'studentID': elem.get_student_id(), 'gradeValue': elem.get_grade()})
        conn.commit()
        conn.close()
        
    def remove(self,elem):
        Repository.remove(self, elem)
        conn=sqlite3.connect(self.__filename)
        c=conn.cursor()
        if type(elem)==Student:
            c.execute("DELETE FROM students where ID="+str(elem.get_id()))
        elif type(elem)==Assignment:
            c.execute("DELETE FROM assignments where assignmentID="+str(elem.get_id()))        
        conn.commit()
        conn.close()
    
    def removeForGrades(self, elem):
        Repository.removeForGrades(self, elem)
        conn=sqlite3.connect(self.__filename)
        c=conn.cursor()
        c.execute("DELETE FROM grades WHERE assignmentID=:assignmentID AND studentID=:studentID AND gradeValue=:gradeValue",
          {'assignmentID':elem.get_id(),'studentID':elem.get_student_id(),'gradeValue':elem.get_grade()})
        conn.commit()
        conn.close()
        
    def update(self,elem):
        Repository.update(self, elem)
        conn=sqlite3.connect(self.__filename)
        c=conn.cursor()
        if type(elem)==Student:
            c.execute("""UPDATE students SET groupStudent = :groupStudent
                    WHERE ID = :ID AND name = :name""",
                  {'groupStudent': elem.get_group(), 'name': elem.get_name(), 'ID': elem.get_id()})
        elif type(elem)==Assignment:
            if elem.get_description()=="None":
                    c.execute("""UPDATE assignments SET deadline = :deadline WHERE assignmentID = :assignmentID""",
                              {'deadline': elem.get_deadline(), 'assignmentID': elem.get_id()})
            elif elem.get_deadline()=="None":
                    c.execute("""UPDATE assignments SET description = :description WHERE assignmentID = :assignmentID""",
                              {'description': elem.get_description(), 'assignmentID': elem.get_id()})
            else:
                    c.execute("""UPDATE assignments SET deadline = :deadline WHERE assignmentID = :assignmentID""",
                              {'deadline': elem.get_deadline(), 'assignmentID': elem.get_id()})
                    c.execute("""UPDATE assignments SET description = :description WHERE assignmentID = :assignmentID""",
                              {'description': elem.get_description(), 'assignmentID': elem.get_id()})
        conn.commit()
        conn.close()
        
    def search(self,ID):
        conn=sqlite3.connect(self.__filename)
        c=conn.cursor()
        if self.__filename=='students.db':
            c.execute("SELECT * FROM students WHERE ID=:ID", {'ID': ID})
            student = c.fetchall()
            if student!=[]:
                newStudent=Student(student[0][0],student[0][1],student[0][2])
                return newStudent
            else:
                raise ValueError("This student does not exist!")
        elif self.__filename=='assignments.db':
            c.execute("SELECT * FROM assignments WHERE assignmentID=:ID", {'ID': ID})
            assignment = c.fetchall()
            if assignment!=[]:
                newAssignment=Assignment(assignment[0][0],assignment[0][1],assignment[0][2])
                return newAssignment
            else:
                raise ValueError("This assignment does not exist!")
        conn.commit()
        conn.close()
        
class TestSQLRepository(unittest.TestCase):
    def setUp(self):
        self.__repoStudents=SQLRepository("students.db") 
        self.__repoAssignments=SQLRepository("assignments.db")
        self.__repoGrades=SQLRepository("grades.db")
        
    def tearDown(self):
        self.__repoStudents=None
        self.__repoAssignments=None
        self.__repoGrades=None
        
    def test_build(self):
        assert(len(self.__repoStudents))==99
        assert(len(self.__repoAssignments))==10
        assert(len(self.__repoGrades))==1
    
    def test_add_remove(self):
        self.__repoStudents.add(Student(101,'nn nn',908))
        assert(len(self.__repoStudents))==100
        self.__repoStudents.remove(Student(101,'nn nn',908))
        assert(len(self.__repoStudents))==99
        self.__repoAssignments.add(Assignment(12,'sss','1.12'))
        assert(len(self.__repoAssignments))==11
        self.__repoAssignments.remove(Assignment(12,'sss','1.12'))
        assert(len(self.__repoAssignments))==10
        self.__repoGrades.addForGrades(Grade(3,4,5))
        assert(len(self.__repoGrades))==2
        self.__repoGrades.removeForGrades(Grade(3,4,5))
        assert(len(self.__repoGrades))==1
    
    def test_update(self):
        student=Student(1,'Firea Nadia',910)
        self.__repoStudents.update(student)
        lst=self.__repoStudents.getAll()
        assert lst[0]==student
        student=Student(1,'Firea Nadia',908)
        self.__repoStudents.update(student)
        
        assignment=Assignment(4,'None','1.10')
        self.__repoAssignments.update(assignment)
        lst=self.__repoAssignments.getAll()
        assert lst[0]==assignment
        assignment1=Assignment(4,'concave','1.10')
        self.__repoAssignments.update(assignment1)
        lst=self.__repoAssignments.getAll()
        assert lst[0]==assignment1
        assignment=Assignment(4,'lee s algorithm','14.11')
        self.__repoAssignments.update(assignment)
        
        with self.assertRaises(ValueError):
            self.__repoStudents.update(Student(10000,'ccc',908))
    
    def test_search(self):
        student=self.__repoStudents.search(1)
        assert student==Student(1,'Firea Nadia',908)
        with self.assertRaises(ValueError):
            student1=self.__repoStudents.search(900000)
            
        assignment=self.__repoAssignments.search(1)
        assert assignment==Assignment(1,'prime numbers','1.10')
        with self.assertRaises(ValueError):
            self.__repoAssignments.search(654)
'''
here is the test class for the json repository
'''       
class TestJson(unittest.TestCase):
    def setUp(self):
        self.__repoStudents=JsonRepository("jsonStudents")
        self.__student=Student(101,'Johnny Bravo',908)
        self.__repoAssignments=JsonRepository("jsonAssignments")
        self.__assignment=Assignment(34,"dddd","12.10")
        self.__repoGrades=JsonRepository("jsonGrades")
        self.__grade=Grade(3,2,10)
        
    def tearDown(self):
        self.__repoStudents=None
        self.__student=None
        self.__repoAssignments=None
        self.__assignment=None
        self.__repoGrades=None
        self.__grade=None
        
    def test_build(self):
        lst=self.__repoStudents.getAll()
        assert len(lst)==100 
        assert len(self.__repoAssignments)==10    
        assert len(self.__repoGrades)==1
        
    def test__add__remove_students(self):
        self.__repoStudents.add(self.__student)
        assert len(self.__repoStudents)==101
        self.__repoStudents.remove(self.__student)
        assert len(self.__repoStudents)==100
        self.__repoAssignments.add(self.__assignment)
        assert len(self.__repoAssignments)==11
        self.__repoAssignments.remove(self.__assignment)
        assert len(self.__repoAssignments)==10
        self.__repoGrades.addForGrades(self.__grade)
        assert len(self.__repoGrades)==2
        self.__repoGrades.removeForGrades(self.__grade)
        assert len(self.__repoGrades)==1
        
'''
this is the test class for the binary repository
'''
        
class Test_BinaryRepo(unittest.TestCase):
    
    def setUp(self):
        self.__studentRepo=BinaryRepository("assignment05_07_studentsBinary")
        self.__assignmentRepo=BinaryRepository('assignment05_07_assignmentsBinary')
        self.__gradesRepo=BinaryRepository('assignment05_07_gradesBinary')
    
    def tearDown(self):
        self.__studentRepo=None
        self.__assignmentRepo=None
        self.__gradesRepo=None
    
    def test_binaryRepo(self):
        lst=self.__studentRepo.getAll()
        assert str(lst[45])=='46, Volschi Elisabeta, 915'
        lst=self.__assignmentRepo.getAll()
        assert str(lst[5])=='6, description, common divisor , deadline,5.12'
        self.__studentRepo.add(Student(107,'Cozma Marin',908))
        lst=self.__studentRepo.getAll()
        assert str(lst[100])=='107, Cozma Marin, 908'
        self.__studentRepo.remove(Student(107, 'Cozma Marin', 908))
        lst=self.__studentRepo.getAll()
        assert len(lst)==100
        grade=Grade(1,2,3)
        self.__gradesRepo.addForGrades(grade)
        lst=self.__gradesRepo.getAll()
        assert len(lst)==1
        self.__gradesRepo.removeForGrades(grade)
        lst=self.__gradesRepo.getAll()
        assert len(lst)==0
        self.__assignmentRepo.update(Assignment(6,'common divisor','5.12'))
        lst1=self.__assignmentRepo.getAll()
        assert str(lst1[5])=='6, description, common divisor, deadline,5.12'
        
''' 
 this is the test class for the repository
'''
   
class TestRepository(unittest.TestCase):
    def setUp(self):
        self.__repo=Repository()
        self.__student=Student(23,'Popescu Ion',915)
        self.__student2=Student(2,'Cozma Ana',901)
        self.__repo2=Repository()
        self.__grade=Grade(1,23,4)
        self.__grade1=Grade(2,45,4)
        
    def tearDown(self):
        self.__repo=None
        self.__student=None
        self.__student2=None
        self.__repo2=None
        self.__grade=None
        self.__grade1=None
        
    def test_addRepository(self):
        self.__repo.add(self.__student)
        with self.assertRaises(ValueError):
            self.__repo.add(self.__student)
        lst=self.__repo.getAll()
        assert str(lst[0])=='23, Popescu Ion, 915'
        repoGrades=Repository()
        grade=Grade(24,56,8)
        repoGrades.addForGrades(grade)
        
    def test__removeRepository(self):
        self.__repo.add(self.__student)
        self.__repo.add(self.__student2)
        self.__repo.remove(self.__student2)
        lst=self.__repo.getAll()
        assert len(self.__repo)==1
        assert str(lst[0])=='23, Popescu Ion, 915'
        with self.assertRaises(ValueError):
            student=Student(234,None,None)
            self.__repo.remove(student)
        
    def test_updateRepository(self):
        self.__repo.add(self.__student)
        student3=Student(23,'Popescu Ion',910)
        self.__repo.update(student3)
        lst=self.__repo.getAll()
        assert str(lst[0])=='23, Popescu Ion, 910'
        repo=Repository()
        assignment1=Assignment(23,'prime numbers','12.01')
        repo.add(assignment1)
        x=Assignment(23,'dd dd',None)
        repo.update(x)
        lst=repo.getAll()
        assert str(lst[0])=='23, description, dd dd, deadline,12.01'
        x=Assignment(23,None,'31.10')
        repo.update(x)
        lst=repo.getAll()
        assert str(lst[0])=='23, description, dd dd, deadline,31.10'
        x=Assignment(23,'cioco bono','15.09')
        repo.update(x)
        lst=repo.getAll()
        assert str(lst[0])=='23, description, cioco bono, deadline,15.09'
        
    def test_searchRepository(self):
        self.__repo.add(self.__student)
        self.__repo.add(self.__student2)
        x=self.__repo.search(23)
        assert x.get_name()=='Popescu Ion'
        with self.assertRaises(ValueError):
            x=self.__repo.search(12589)
    
    def test_removeForGrades(self):
        self.__repo2.addForGrades(self.__grade)
        self.__repo2.addForGrades(self.__grade1)
        self.__repo2.removeForGrades(self.__grade1)
        with self.assertRaises(ValueError):
            self.__repo2.removeForGrades(self.__grade1)
        assert len(self.__repo2)==1
        
'''
this is the test class for the FileRepository
'''
class TestFileRepository(unittest.TestCase):
    def setUp(self):
        self.__repo=FileRepository('assignment05_07_students.txt')
        self.__student=Student(236,'Popescu Ion',915)
        self.__student2=Student(278,'Cozma Ana',901)
        self.__repo2=FileRepository('assignment05_07_grades.txt')
        self.__grade=Grade(1,23,4)
        self.__grade1=Grade(2,45,4)
        self.__repo3=FileRepository('assignment05_07_assignments.txt')
        
    def tearDown(self):
        try:
            self.__repo.remove(self.__student)
            self.__repo.remove(self.__student2)
        except ValueError:
            pass
        self.__repo=None
        self.__student=None
        self.__student2=None
        self.__repo2=None
        self.__grade=None
        self.__grade1=None
        self.__repo3=None
        
    def test_addRepository(self):
        self.__repo.add(self.__student)
        with self.assertRaises(ValueError):
            self.__repo.add(self.__student)
        lst=self.__repo.getAll()
        assert str(lst[100])=='236, Popescu Ion, 915'
        repoGrades=Repository()
        grade=Grade(24,56,8)
        repoGrades.addForGrades(grade)
        
    def test__removeRepository(self):
        self.__repo.add(self.__student2)
        self.__repo.remove(self.__student2)
        lst=self.__repo.getAll()
        assert len(self.__repo)==100
        with self.assertRaises(ValueError):
            student=Student(234,None,None)
            self.__repo.remove(student)
        
    def test_updateRepository(self):
        self.__repo.add(self.__student)
        student3=Student(236,'Popescu Ion',910)
        self.__repo.update(student3)
        lst=self.__repo.getAll()
        assert str(lst[100])=='236, Popescu Ion, 910'
        repo=Repository()
        assignment1=Assignment(23,'prime numbers','12.01')
        repo.add(assignment1)
        x=Assignment(23,'dd dd',None)
        repo.update(x)
        lst=repo.getAll()
        assert str(lst[0])=='23, description, dd dd, deadline,12.01'
        x=Assignment(23,None,'31.10')
        repo.update(x)
        lst=repo.getAll()
        assert str(lst[0])=='23, description, dd dd, deadline,31.10'
        x=Assignment(23,'cioco bono','15.09')
        repo.update(x)
        lst=repo.getAll()
        assert str(lst[0])=='23, description, cioco bono, deadline,15.09'
        
    def test_searchRepository(self):
        self.__repo.add(self.__student)
        x=self.__repo.search(236)
        assert x.get_name()=='Popescu Ion'
        with self.assertRaises(ValueError):
            x=self.__repo.search(12589)
    def test_removeForGrades(self):
        self.__repo2.addForGrades(self.__grade)
        self.__repo2.addForGrades(self.__grade1)
        self.__repo2.removeForGrades(self.__grade1)
        self.__repo2.removeForGrades(self.__grade)
        with self.assertRaises(ValueError):
            self.__repo2.removeForGrades(self.__grade1)
        assert len(self.__repo2)==1
        
           


