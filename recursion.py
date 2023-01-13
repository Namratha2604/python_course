#A function calling itself,directly or indirectly, is called a recursive function.
#--the phenomenon itself is called recursion 
#examples: for factorial
#0!=1
#n!=n*(n-1)!
#even or odd function:
#even(n)=(n==0) or odd(n-1)
#odd(n)=(n!=0) and even(n-1)

#recursive functions:properties
#the arguments change between the recursive calls
#5!=5*4!...
#change is toward a case for which solutions is known(base case)
#0! id 1
#odd(0) is false
#even(0) is true 
u = 1
v = 2
u = v
v = u
print(u)
print(v)

u, v = 1, 2
u, v = v, u
print(u)
print(v)
