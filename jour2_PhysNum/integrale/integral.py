
def milieu(f,a, b, n):
    h = (b-a)/n
    s = 0
    for i in range(n):
        xi = (a+h/2)+i*h
        s+= f(xi)
    s*=h
    return s
def trapeze(f, a, b, n):
    h = (b-a)/n
    s = (f(a)+f(b))/2
    for i in range(1, n):
        xi = a + h*i
        s+= f(xi)
    s*=h
    return s
