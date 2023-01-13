def sieve(n):
    '''Find all primes <=n.Updates global primes list that prime indices have value True, composite indices False'''
    global primes
    primes=[True]*(n+1)#primes[0...n]

    primes[0],primes[1]=False,False

    for j in range(2,n+1):
        if primes[j]==False:#composite
            continue
        for i in range(j*j,n+1,j):
            primes[i]= False

#main function to call sieve
global primes
n=int(input('n= '))
sieve(n)#set primes
for i in range(2,n+1):
    if primes[i]:
        print(i, end=' ')


def f(n):
    for i in range(2, n):
        if (n%i) == 0:
            return i
        return -1

print (f(49))
