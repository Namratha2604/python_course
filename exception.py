try:
    5/0
except:
    print("Something Bad Happened")
except ZeroDivisionError:
    print("Division by Zero")
except ArithmeticError:
    print("Bad Arithmetic")


try:
    print('Hello', end='#')
except:   
    print('Bye', end='#')
else:
    print('PK', end='#')
finally:
    print('AK', end='#')
 

try:
    print('Hello', end='#')
except:   
    print('Bye', end='#')
else:
    print('PK', end='#')
finally:
    print('AK', end='#')
