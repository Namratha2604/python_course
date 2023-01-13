#to write the complex functions in python like higher order functions
def summation(n,f):
    '''compute f(1)+f(2)+....f(n)'''
    sum=0
    for i in range(1,n+1):
        sum = sum+f(i)
    return sum
print(sum)

def identity(x):
    return x
print(summation(10,identity))

def square(x):
    return x*x
print(summation(10,square))

print(summation(10,lambda x:x**3))#we can use lambda if we sont have the function name


def printapp(f, xs):
    for i in xs:
        print(f(i), end='')

printapp(lambda x: x+x, [(1,2), (3,4)])

def printapp(f, xs):
    for i in xs:
        print(f(i), end='%')

def double(x):
    return x+x

printapp(double, {1:1, 2:4, 3:9})
