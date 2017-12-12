import numpy as np# P193-9
def sor(A,b,tol,w):
    x1=np.linspace(tol*10,tol*10,len(A[0]))
    prex1=np.zeros(len(A[0]))
    i=0
    while(np.linalg.norm(x1-prex1,ord=np.inf)>tol):
        i=i+1
        prex1=x1
        x1=(1-w)*prex1+w*((np.diagflat(np.diag(A))-A).dot(prex1)+b)/np.diag(A)
        print("iterate{0}:{1}".format(i,x1))


A=np.array([[5,2,1],[-1,4,1],[2,-3,-4]])
b=np.array([5.2,-6.2,-4.9])
sor(A,b,1e-8,1.25)
np.transpose(np.array([ 1.20227695, -2.10123957, 3.39750825]))