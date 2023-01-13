#if a module had contained a function with the name for example
#fibonachi numbers are stoted in a module of fib.py
# then in other module u can import the same definitions by simply 
#import fib 
#which helps to import the def of fibonachi numbers
#so we dont need to write the fibonachi def again
def fib_rec(n):
    '''recrusive fibonacci'''
    if (n<=1):
        return n
    else:
        return fib_rec(n-1)+fib_rec(n-2)
    
def fib_iter(n):
    '''iterative fibonacchi'''
    cur,nxt=0,1
    for k in range(n):
        cur,nxt=nxt,cur+nxt
    return cur
