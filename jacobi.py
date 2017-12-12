import numpy as np #P193-6
def jacobi(A,b,tol,x=None):
    if x is None:
        x=np.zeros(len(A[0]))
        prex=np.linspace(tol*10,tol*10,len(A[0]))

    D=np.diag(A)
    R=A-np.diagflat(D)
    es=np.linspace(tol,tol,len(A[0]))
    i=0
    while np.all(np.fabs(prex-x)>es):
        i=i+1
        prex=x
        x=(b-np.dot(R,x))/D
        print("iterate{0}:{1}".format(i, x))
    return x

A=np.array([[8.3,2.1,-1.2,0.5],[0.8,10.2,3.5,-1.8],
            [1.2,0.2,-4,-0.5],[-0.2,0.3,0.4,-2]])
b=np.array([-3.02,4.79,-6.72,8.89])
jacobi(A,b,1e-8)