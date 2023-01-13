#orderd sequence of values
#written as a sequence of comma-separated values between square brackets
lst=[1,2,3,4]
print(lst)
print(type(lst)) 
print(len(lst))
print(lst[2])
print(lst*2)
print(lst+[7])
L=[4,9,7,5,2,1,6]
print(L.append(8))#add or append 8 at last
print(L.insert(5,8))#insert 8 at index 5
print(L.remove(5))#removes 5 from the list
print(L.pop(4))#removes an element by its index
print(L.index(5))#asks the index of 5
print(L.count(5))#asks how many times it was repeated
print(L.sort())#sorts the list
print(L.reverse())#will reverse the list

#---Quiz questions---

v1 = [1,2,3]
v1.append(4)
print (v1)


v1 = [1,2,3]
v1.append("hi")
print (v1)


v1 = [1,2,3]
t1 = v1[:]
print (t1)


v1 = [1,2,3]
v1.extend("hi")
print (v1)


v1 = [1,2,3]
v1 + [4]
print (v1)


v1 = [1,2,3]
v1.append("hi")
print (v1)
