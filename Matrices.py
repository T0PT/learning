import numpy as np

class matrix():
    def __init__(self, x=[[1,2],[3,4]]):
        self.matr=np.array(x)
        #self.determinant=self.determinant()
    def determinant(self):
        if len(self.matr) == len(self.matr[0]):
            out=0
            for i in range(len(self.matr)):
                if len(self.matr) ==2:
                    return self.matr[0][0]*self.matr[1][1]-self.matr[0][1]*self.matr[1][0]
                else:
                    out+= ((i%2)*-1)*self.matr[i][0]*matrix.determinant(self.matr[:i-1]+self.matr[i+1:])
            return out
    def __add__(self, other):
        return matrix(self.matr+other.matr)
    def __(self, *args, **kwargs):
        return self.matr
    def __sub__(self, other):
        return matrix(self.matr-other.matr)
    def __mul__(self, other):
        return matrix(self.matr*other.matr)
    def __truediv__(self, other):
        return matrix(self.matr/other.matr)
    def __str__(self):
        return self.matr
    def dot(self,other):
        return matrix(self.matr.dot(other.matr))
a=matrix()
b=matrix()