# Grades-and-Assignments-Manager-Application
--created during the first semester
What I learned:
-python basics
-working with files
-multiple ways to store data: in text/binary/json files and swl database
-lambda expressions
-creating iterable classes
-CRUD operations
-inheritance in python
-using TKInter
-undo/redo
-creating statistics
-layered architecture
-user input verification
-unit tests and coverage
-throwing exceptions, creating new exceptions

This is an application that helps with the management of a number of students. You are able to manage the assignmnets the students have or will be given and their grades. It offers a console interface, as well as a GUI (created with TKInter). 

Multiple ways to store your data:
1)permanently:-this will save the data in files
2)temporary:-this will save the data in memory
3)binary:-this will save the data in binary files
4)json:-this will save the data in json files
5)sql:-this will save the data in a sql database

No matter what data storage you opted for, the repositories will be already populated with some data.

You can add,remove and update students and assignmnets. You can assign to the students/to a whole group an assignment and grade them.

There are also options for statistics:
	->STAT:if you want all students who received a given assignment, ordered alphabetically. This is the only one that requires an assignmentID.
	->LATE:if you want all students who are late in handing in at least one assignment. These are all the students who have an ungraded assignment for which the deadline has passed.
	->TOP:if you want the students with the best school situation, sorted in descending order of the average grade received for all assignments.
	->ALL:if you want all assignments for which there is at least one grade, sorted in descending order of the average grade received by all students who received that assignment.

There is the option for undo/redo, as well.

In order to run the program, click on the 'main' file (considering you have Python installed).

