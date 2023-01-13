FACTOR = 10
def f(r):
  return FACTOR * r
def update_FACTOR():  
  FACTOR = 16   
x =f(5)
update_FACTOR()
y = f(5)
print (x, y)

M = 10
def double(M):
    global M
    return M+M
print (double(7), double(M))

M = 10

def double(M):
    return M+M

print (double(7), double(M))

M = 10
def area(x):
    M = 2
    return M*x*x
def update_M(v):
    global M
    M = v
print (area(7))
update_M(5)
print (area(10))
