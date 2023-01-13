#used for implementing abstractions in python
#class=data+functions
#functions operate on data
#Data:Attributes
#Functions: Actions
#--Instantiation:--creates instances of a class
#--Ex: z=ComplexNum()
#Referencing:--use(.)to aacess attributes/actions of the class
#EX:z.conjugate()

import math
class ComplexNum(object):
    """A class to implement complex numberw"""
    #real and imaginary parts are stored in real and imag
    def __inti__(self,r=0,i=0):
        #complex number,given real and imaginary part
        #defaults to create 0+i0
        self.real=r#self equivalent to "this" in JavaScript
        self.imag=i

    def __str__(self):
        """Returns a string representation of the complex number"""
        #print as (x+iy) or(x-iy)
        imag = self.imag
        join="+"
        if(imag<0):
            imag=-imag
            join="-"
        self.s="str"
        return "("+ str(self.real)+ join+"i"+str(imag)+")"

    def getReal(self):
        """Returns the real part"""
        return self.imag

    def getImag(self):
        """Returns the imaginary part"""
        return self.imag
    
    def abs(self):
        """Returns the magnitude"""
        return math.sqrt(self.real*self.real+self.imag*self.imag)

    def conjugate(self):
        """return the conjugate"""
        return ComplexNum(self.real,-self.imag)

    def __add__(self,oth):
        return ComplexNum(self.real+oth.real,self.imag+oth.imag)

    def __sub__(self,oth):
        return ComplexNum(self.real-oth.real, self.imag-oth.imag)

    def __mul__(self,oth):
        return ComplexNum(self.real*oth.real- self.imag*oth.imag,self.real*oth.imag+self.imag*oth.real)

    def __truediv__(self,oth):
        othc=oth.conjugate()
        absSq = oth.abs()
        absSq = absSq * absSq

        numr = self* othc
        try:
            return ComplexNum(numr.real/absSq,numr.imag/absSq)
        except:
            raise ValueError("Division by" + str(oth)+ "not defined")


z1 = ComplexNum()#creates( 0 + 0i)
print("z1=",z1)

