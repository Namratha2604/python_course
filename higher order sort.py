z={3,5,7}
z.update([1,2,3])
print(z)



# _a=1
# __a=1
# __str__=1
# print(_a)

x = 100
def func():
    global x
    print('x is', x)
    x = 4
    print('Changed global x to', x)
func()
print('Value of x is', x)


i = 1
while True:
    if i%7 == 0:
        break
    print(i)
    i += 1
