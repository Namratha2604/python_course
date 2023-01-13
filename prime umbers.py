def f(n):
    for i in range(2, n):
        if (n%i) == 0:
            return i
        return -1

print (f(49))

def f(n):
    i = 2
    while i*i < n :
        if (n%i) == 0:
            return i
        i = i + 1
    return n

print (f(47))

def f(n):
    i = 2
    while i*i < n :
        if (n%i) == 0:
            return i
        i = i + 1
    return i

print (f(47))

def f(n):
    for i in range(2, n):
        if (n%i) == 0:
            return i
        else:
            return -1

print (f(49))

def f(n):
    for i in range(2, n):
        if (n%i) == 0:
            return i
    return -1

print (f(49))
