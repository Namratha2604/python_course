for i in range(1,9):
    for j in range(1,6):
        print(i*j, end=" ")
    print()
    # here the end="" charecter says that instead  of printing in the same line print in the another row with some space  

for i in range(1,7):
    for j in range(i,i*2):
        print(j,end=" ")
    print()

for i in range(1,5):   
    for j in range(1, i, 2*i):     
        print (j,end='.')

for i in range(1,5):   
    for j in range(i, i+1):     
        print (j,end='#') 
    print(end='#')

for i in range(1,4):   
    for j in range(i,2*i):     
        print (j,end='.')

for i in range(1,3):   
    for j in range(2*i):     
        print (j,end='.')

n = 13
while (n > 1):   
    n = n//2   
    print(n, end='+')
