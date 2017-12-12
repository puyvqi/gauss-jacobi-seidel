#P228 -6.1
import math
def der1(a):
    re=(2*a-math.exp(a)-3)/3.0
    return re

def fun1(a):
    re=(2-math.exp(a)+a**2-3*a)/3.0
    return re

def fun2(a):
    re=a**2+10*math.cos(a)
    return re

def der2(a):
    re=2*a-10*math.sin(a)
    return re

def newton(fun,der):
    x=10
    prex=0
    i=0
    while(math.fabs(prex-x)>1e-8):
        i=i+1
        prex=x
        x=prex-fun(x)/der(x)
        print("iterate{0}:{1}".format(i,x))

newton(fun1,der1)