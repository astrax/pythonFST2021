from integral import milieu, trapeze
from math import exp
import matplotlib.pyplot as plt
def X(t):
    return exp(t**3) - 1
def f(t):
    return 3*t**2 * exp(t**3)

exact = X(1) - X(0)

liste_n,Err_milieu, Err_trapeze= [],[],[]
for n in range(1, 50):
    X_milieu = milieu(f, 0, 1, n)
    X_trapeze = trapeze(f, 0, 1,n)
    Err_milieu.append(abs(exact - X_milieu))
    Err_trapeze.append(abs(exact - X_trapeze))
    liste_n.append(n)
    
plt.plot(liste_n, Err_milieu, "--ro", label = "Point milieu")
plt.plot(liste_n, Err_trapeze, "--bo", label = "Trapèze")
plt.legend()
plt.xlabel("n")
plt.ylabel("E(n)")