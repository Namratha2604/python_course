class X:
    def __init__(self):
         self.a = 10
         self._b = 20
    def getB(self):
         return self._b

x = X()
x._b = 60
print(x.getB())

class Roll:
    def __init__(self, id):
        self.id = id
        id = 231

val = Roll(321)
print (val.id)
