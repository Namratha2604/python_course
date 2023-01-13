breaking of loop
sum=0
for i in range(100):
    value= int(input())
    if(value<0):
        sum=sum+value
print("sum=",sum)

# Using continue
# in continue the loop is not broken it is just skipping certain iteration for a certain number.
# u justneed to write the condition and continue under it to cancel that particular iteration

sum=0
for i in range(100):
    value= int(input())
    if(value<0):
        #-ve number: skip to the next number
        #iteration of the loop
        continue
    sum=sum+value
print("sum=",sum)

i=1
while i<=10:
    if i%2==0:
        print(i,end="")

i = 1
while i <= 10:       
    if i%2==0: # even
        i= i+1  
        continue   
    print (i, end=' ')   
    i= i+1

i = 1
while i <= 10:       
    if i%2==0: # even        
        continue   
    print (i, end=' ')   
    i= i+1

r,a,n = 2,10,20
term = a
for i in range(n):
    term = term * r
    if (i > 3):
        break
print (term)

i = 1
while i <= 10:       
    if i%2==0: # even
        i= i+1  
        continue   
    print (i, end=' ')

i = 1
while i <= 10:       
    i= i+1  
    if i%2==0: # even        
        continue   
    print (i, end=' ')
