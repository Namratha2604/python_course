#move n disks from A to C using B as auxx
def hanoi(n,A,C,B):
    if n==0:
        return#nothing to move
        #recrusively move n-1 disks
        #from A to B using C as auxx
        haoi(n-1,A,B,C)

#atomatic move of single disk
    print("Move 1 disk from",A,"to",C)
#recrusively movie n-1 disks
#from B to C using A as auxx
    hanoi (n-1,B,C,A)
