import operator, math
class Vector:
    def __init__(self, first, second):
        self.f = first
        self.s = second
        self.mag = self.getMag()
    def add(self, vec):
        return self.Combine(vec, operator.add)
    def sub (self, vec):
        return self.Combine(vec, operator.sub)
    def Combine(self, vec, f):
        if not type(vec) is Vector: #eventually change this so it checks the dimension states
            print ("Size of Matrices do not match")
            return
        else: 
            newf = f(self.f, vec.f)
            news = f(self.s, vec.s)
            return Vector (newf, news)
    def getUnit(self):
        newf= self.f / self.mag
        news = self.s / self.mag
        return Vector (newf, news)
    def getMag(self):
        dist= math.sqrt(math.pow (self.f, 2) + math.pow (self.s, 2))
        return dist
    def showCo(self):
        return  "[%f , %f]" % (self.f, self.s)
    def showUn(self):
        return "Magnitude %d @ Unit Vector %s" % (self.mag, self.getUnit().showCo())
        
#Test Stuff
x= Vector(1,2)
y= Vector(2,1)
z =x.add(y)
 
