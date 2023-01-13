# Helps us to eliminate duplicate entries
basket=["apple","banana","guvava","pear","orange","apple","banana"]
fruits=set(basket)
print(fruits)
print(type(fruits))
print("apple" in fruits)
print("mango" in fruits)
A=set("acads")
B=set("institute")
print(A)
#set opertators
print(A-B)#set difference
print(A|B)#set union
print(A&B)#set intersection
print(A^B)#symmetric difference[(a-b)|(b-a)]
