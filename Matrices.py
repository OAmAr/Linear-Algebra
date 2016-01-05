import operator, math
class Matrix(object):
    def __new__(cls, lst):
        mat = lst[-1]
        wid = lst[1]
        hi = lst[0]
        if len(mat) == hi:
            for col in mat:
                if len(col) != wid:
                    print("Error: Width of array does not match")
                    return
            return super(Matrix, cls).__new__(cls)
        else:
            print("Error: Height of array does not match")
            return
    def __init__(self, lst): #Takes list of format (Height, Width, [ (row 1) (row 2..) ] )
        self.mat = lst[-1]
        self.wid = lst[1]
        self.hi = lst[0]
    def sameSize(self, matrix):
        if self.wid == matrix.wid and self.hi == matrix.hi:
            return True
        else:
            return False
    def Combine(self, matrix, op): #Mason is mad that this is more functional than OOP
        #print("checking")
        if not self.sameSize(matrix):
            print ("Error, Invalid Dimensions")
            return
        #print("init")
        newmat= []
        for i in range(len(self.mat)):
            newrow=[]
            for x, y in zip(self.mat[i],matrix.mat[i]):
                newrow.append (op (x,y))
            newmat.append (newrow)
        newMat= Matrix ( [self.hi, self.wid, newmat])
        newMat.show()
        print('\n')
        return newMat 
    def add(self, matrix):
        #print("adding")
        #disp
        self.show()
        print ('+')
        matrix.show()
        print ('=')
        #/disp
        return self.Combine(matrix, operator.add)
    def scale(self, scalar):
        #display
        #print('multiplying')
        print('%d \n*' % scalar)
        self.show()
        print ('=')
        #/display
        scalerow = [scalar]*self.wid
        #print (scalerow)
        mat= []
        for i in range(self.hi):
            mat.append(scalerow)
        tempMat = Matrix([self.hi, self.wid, mat])
        return self.Combine (tempMat, operator.mul)       
    def sub(self, matrix):
        #disp
        self.show()
        print ('-')
        matrix.show()
        print ('=')
        #/disp
        return self.Combine(matrix, operator.sub)
    def show(self):
        for i in enumerate(self.mat):
            print (i[1])
    
    
    
def comb(lol1, lol2):
    newlist= []
    for i in range(len(lol1)):
        newcol=[]
        for x, y in zip(lol1[i],lol2[i]):
            newcol.append(x+y)
        newlist.append(newcol)
    newlist
    return newlist
#Test Stuff
y = [2, 1, 4]
x= [1, 2, 3]
z= [x, x, x]
m = [y,y,y]
t= [x,x]
one = [1]
v1 = [one, one]
M = Matrix([3,3,m])
Ma2 = M.add(M)
M.scale(2)
