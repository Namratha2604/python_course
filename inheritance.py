class Person:
    def getInfo(self):
        return "Person's getInfo is called"
  
    def printPerson(self):
        print(self.getInfo())

class Staff(Person):
    def getInfo(self):
        return "Staff's getInfo is called"

def main():
    Person().printPerson()
    Staff().printPerson()

print(main())

####################
class A:
    def __init__(self, i = 0, j = 0):
        self.i = i
        self.j = j

    def __str__(self):
        return "some string"

    def __eq__(self, other):
        return self.i * self.j == other.i * other.j

def main():
    x = A(4, 3)
    y = A(6, 2)
    print(x == y)

main()
