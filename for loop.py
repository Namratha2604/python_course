r,a,n = 2,10,4
term = a
for i in range(1, n):
    term = term * r
print (term)


n= int(input('n? '))
u,v = 1,1
for i in range(n-2):   
    u, v = v, u + v
print (v)


n= int(input('n? '))
u,v = 1,1
for i in range(n-2):   
    u, v = v, u + v
print (v)


r,a,n = 2,10,4
term = a
for i in range(n):
    term = term * r
print (term)


r,a,n = 2,10,4
term = a
for i in range(1, 2, n):
    term = term * r 
print (term)
