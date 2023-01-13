t="intro to python","namratha gunda",101 #tuple assigned to a variable t
print(t[0])
print(t[2])
print(t)
print(type(t))
#Empty and singleton tuples
#empty=()
#singleton=1 , #Note that comma at end..otherwise it is treated as normal word
#---tuples can be nested aswell---
course="python","amey",101
student="namratha","34",course
print(student)
#course tuploe is copied in student tuple
#even if I change anything in course tuple later the student tuple doesnt change 
print(len(course))
#tuples aalso suppoet concatente and repeat and indexing
print(course+student)
#slicing
print(t[0:3])
#indexing
print((t+course)[4])
#repeatetion
print(2*course)
# print(len(1,2,3,4,5))
print(len(1))
print(len(("Hello", "World")))
