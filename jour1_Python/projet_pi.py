from math import sqrt
def piLeibniz(n):
    s = 0
    for i in range(n+1):
        s+=1/((4*i + 1)*(4*i +3))
    s*=8
    return s
def piEuler(n):
    s = 0
    for i in range(1, n+1):
        s+= 1/i**2
    s = sqrt(6*s)
    return s
