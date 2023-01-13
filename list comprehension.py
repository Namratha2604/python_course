#set builder notation in python
print([x*x for x in range(1,11)])
#consists of a bracket ontaing an expressin followed bt a for clause, then zero or more for or if clauses
# nums=[-1,6,8,-5,-3]
# pos=[x for x in nums if x>0]
# print(pos)

# print([ (x ,abs(x)) for x in nums])

z = [x*y for x in range(1,4) for y in range(3, 1)]
print(z)

z = [x*y for y in range(3, 1, -1) for x in range(1,4) ]
print(z)

z = [x*y for x in range(1,4) for y in range(3, 1, -1)]
print(z)

x = 'acads'
y = []
y.extend(x)
y.extend([x])
print(len(y))

z = [x*x for x in range(1,5) if (x%2 == 0)]
print(z)
