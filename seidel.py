import numpy as np # P193-6
ITERATION_LIMIT = 1000
def seidel2(A,b):
    print("System of equations:")
    for i in range(A.shape[0]):
        row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

    x = np.zeros_like(b)
    for it_count in range(1, ITERATION_LIMIT):
        x_new = np.zeros_like(x)
        print("Iteration {0}: {1}".format(it_count, x))
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new

    print("Solution: {0}".format(x))
    error = np.dot(A, x) - b
    print("Error: {0}".format(error))


def seidel(A,b,tol,x=None):
    if x is None:
        x=np.zeros(len(A[0]))
        prex=np.linspace(tol*10,tol*10,len(A[0]))
    B=np.eye(len(A[0]))-(A/np.diag(A))

    L=np.tril(B)
    U=np.triu(B)
    ILinv=np.linalg.inv(np.eye(len(A[0]))-L) #(I-L)^-1
    Dinv=np.linalg.inv(np.diagflat(np.diag(A)))

    K=np.dot(ILinv,U)
    C=np.dot(ILinv,Dinv)
    #print(C)
    es=np.linspace(tol,tol,len(A[0]))
    while np.all(np.fabs(prex-x)>es):
        prex=x
        x=np.dot(K,np.transpose(x))+np.dot(C,np.transpose(b))
        #x = np.dot(B, np.transpose(x)) + np.dot(U,np.transpose(x))+np.dot(Dinv,b)
        print(x)
    return x

A=np.array([[8.3,2.1,-1.2,0.5],[0.8,10.2,3.5,-1.8],
            [1.2,0.2,-4,-0.5],[-0.2,0.3,0.4,-2]])
b=np.array([-3.02,4.79,-6.72,8.89])
seidel2(A,b)