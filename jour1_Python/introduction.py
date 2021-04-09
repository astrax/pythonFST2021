from math import sqrt
import random as r

def somme_pairs(n):
    
    s2 = 0 # somme des i pairs
    j = 1
    while j <= n:
        if j % 2 == 0:
            s2 += j
        j+=1
    return s2

def somme(n):
    s1 = 0
    for i in range(1, n+1):
        s1 += i
    return s1
# Méthode classique : (sur 4 lignes)
L = []
for i in range(1, 101):
    L.append(sqrt(i))
#print(L)

# Méthode avancée (compréhension de liste) : sur une ligne
M = [sqrt(i) for i in range(1, 101) if i%2 ==0]

# Créer une liste de valeurs alléatoires

R = [r.randint(1, 6) for i in range(20)]
for el in R:
    print(el*"*")