from repository import Repository
import unittest
#this is the filter function
def filterList(function, lst):
    # lst=iterable
    if function==None:
        function=bool
    for i in lst:
        if not function(i):
            yield i
#this is the shell sort method
def shellSort(lst):
    gap = len(lst)//2
    while gap > 0:
        for startposition in range(gap):
            gapInsertionSort(lst,startposition,gap)
        gap = gap // 2
    return lst

def gapInsertionSort(lst,start,gap):
    for i in range(start+gap,len(lst),gap):
        currentvalue = lst[i]
        position = i
        while position>=gap and lst[position-gap]>currentvalue:
            lst[position]=lst[position-gap]
            position = position-gap
        lst[position]=currentvalue
        
#this is the iterable repository
class RepositoryIterable(Repository):
    def __init__(self):
        Repository.__init__(self)
        self.index=-1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index+=1
        if self.index==len(self._elems):
            raise StopIteration
        return self._elems[self.index]

    def __setitem__(self, position, value):
        for i in range(len(self._elems)):
            if i==position:
                self._elems[i]=value
                return
        raise KeyError(position)
                

    def __delitem__(self, position):
        for i in range(len(self._elems)):
            if i==position:
                del self._elems[i]
                return
        raise KeyError(position)
    
    def sort(self):
        #here we implement the shell sort method
        sublistcount = len(self._elems)//2
        while sublistcount > 0:
            for startposition in range(sublistcount):
                self.gapInsertionSort(startposition,sublistcount)
            sublistcount = sublistcount // 2
    
    def gapInsertionSort(self,start,gap):
        for i in range(start+gap,len(self._elems),gap):
            currentvalue = self._elems[i]
            position = i
            while position>=gap and self._elems[position-gap]>currentvalue:
                self._elems[position]=self._elems[position-gap]
                position = position-gap
            self._elems[position]=currentvalue
    
     
from model_Assignment import Assignment
from model_Grade import Grade
from model_Student import Student
    
class TestRepoIterable(unittest.TestCase):
    def setUp(self):
        self.__repo=RepositoryIterable()
        self.__student=Student(23,'Popescu Ion',915)
        self.__student2=Student(2,'Cozma Ana',901)
        self.__repo2=RepositoryIterable()
        self.__grade=Grade(1,23,4)
        self.__grade1=Grade(2,45,4)
        self.lst=[2,3,4,5,6,7] 
        
    def tearDown(self):
        
        self.__repo=None
        self.__student=None
        self.__student2=None
        self.__repo2=None
        self.__grade=None
        self.__grade1=None
        self.lst=None
        
    def test_filter(self):         
        filtered=filterList(lambda x:x%2,self.lst)
        ok=0
        for i in filtered:
            if i%2!=0:
                ok=1
        assert ok==0        
 
    def test_sort(self):
        self.__repo.add(self.__student)
        self.__repo.add(self.__student2)
        lst=self.__repo.getAll()
        newlist=shellSort(lst)
        self.__repo.sort()
        lst1=self.__repo.getAll()
        assert str(lst1[0])=='2, Cozma Ana, 901'
        assert str(lst1[1])=='23, Popescu Ion, 915'
        assert lst==newlist
    
    def test_delete(self):
        self.__repo.add(self.__student)
        self.__repo.add(self.__student2)
        del self.__repo[1]
        assert len(self.__repo)==1
        with self.assertRaises(KeyError):
            del self.__repo[1]
            
    def test_set(self):
        self.__repo.add(self.__student)
        self.__repo.add(self.__student2)
        self.__repo[1]=Student(890,'Radu Bucalaie',908)
        for i in self.__repo:
            if i==Student(890,'Radu Bucalaie',908):
                ok=1
        assert ok==1
        with self.assertRaises(KeyError):
            self.__repo[3]='k'   
    def test_addRepository(self):
        self.__repo.add(self.__student)
        with self.assertRaises(ValueError):
            self.__repo.add(self.__student)
        lst=self.__repo.getAll()
        assert str(lst[0])=='23, Popescu Ion, 915'
        repoGrades=RepositoryIterable()
        grade=Grade(24,56,8)
        repoGrades.addForGrades(grade)
        assert len(repoGrades)==1
        
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
        with self.assertRaises(ValueError):
            student=Student(456,'Popa Vlad',90)
            self.__repo.update(student)
        repo=RepositoryIterable()
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
   
    
        