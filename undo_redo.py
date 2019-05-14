from repository import *        
 
class UndoRedo():
    def __init__(self):
        self._history=[]
        self._index=-1 
    
    def add(self,operation):
        '''
        operation=Operation (class)
        '''
        self._history.append(operation)  
        self._index+=1

    def undo(self):
        if self._index==-1:
            return False
        operation=self._history[self._index]
        self._index-=1
        operation.undo()
        return True
    
    def redo(self):
        if self._index==len(self._history)-1:
            return False
        self._index+=1
        operation=self._history[self._index]
        operation.redo()
        return True
    
    def update_history(self):
        if len(self._history)>0:
            for i in range(self._index,len(self._history)-1):
                self._history.pop(i)
                
class FunctionCall():
    def __init__(self,functionRef,*parameters):
        self._functionRef=functionRef
        self._parameters=parameters
        
    def call(self):
        self._functionRef(*self._parameters)
    
class Operation():
    def __init__(self,functionDo,functionUndo):
        '''
        functionDo,functionUndo= FunctionCall(class)
        '''
        self._functionDo=functionDo
        self._functionUndo=functionUndo
        
    def undo(self):
        self._functionUndo.call()
    
    def redo(self):
        self._functionDo.call()
'''    
class CascadedOperation():
    def __init__(self,op=None):
        self._operations=[]
        if op!=None:
            self.add(op)
    
    def add(self,op):
        self._operations.append(op)
    
    def undo(self):
        for i in range(len(self._operations)-1,-1,-1):
            self._operations[i].undo()
            
    def redo(self):
        for i in range(len(self._operations)-2,-1,-1):
            self._operations[i].redo()
        self._operations[len(self._operations)-1].redo()
'''                         

import unittest
#from UI import UI
from repository import Repository
class TestUndoRedo(unittest.TestCase):
    def setUp(self):
        self.__undoRedo=UndoRedo()
        self.__students=Repository()
        self.__assignments=Repository()
        self.__grades=Repository()
        self.__ui=UI(self.__students,self.__assignments,self.__grades,self.__undoRedo)
        
    def tearDown(self):
        self.__undoRedo=None
        self.__ui=None
        self.__students=None
        self.__assignments=None
        self.__grades=None
    
    def test_undoRedo(self):
        command='add 1 Cozma Marin 908'
        self.__ui.add(command,True)
        assert len(self.__students)==1
        self.__ui.undo('undo')
        self.__ui.undo('undo')
        lst=self.__students.getAll()
        assert len(self.__students)==0
        self.__ui.redo('redo')
        self.__ui.redo('redo')
        
        
        
  
