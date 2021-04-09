from projet_pi import piLeibniz, piEuler
from math import pi
f = open("pi.csv", "w")
f.write(" "*6+"n" + ","+" Leibniz" + ","+" "*7 +" Euler"+"\n")
for n in range(1, 101):
    EL = abs(pi -piLeibniz(n))
    EE = abs(pi -piEuler(n))
    f.write("{:7d},{:.7f},{:.7f}\n".format(n, EL, EE))
f.close()
