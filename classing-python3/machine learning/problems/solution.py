#! /usr/bin/env python3


#In [13]
#%matplotlib inline
from matplotlib.pyplot import *
from numpy import *
from scipy import *
from scipy.linalg import *
from scipy.sparse import *
from scipy.sparse.linalg import *

#In [14] 
'''Question (a)'''
m=100
#Matrice K avec I et DTD
I = diag(ones(m))
DTD = diags([-1,2,-1],[-1,0,1], shape=(m,m))
K = kron(I,DTD)+kron(DTD,I)
K=csr_matrix(K)

#In [4] Question (b) 

#v0 : vecteur de taille m
#k : nombre d'iterations de l'algo
#Membre de droite f avec e1 et en
e1=zeros(m)
e1[0]=1
e1=csr_matrix(e1)
en=zeros(m)
en[m-1]=1
en=csr_matrix(en)
#Potentiels haut, bas, droite et gauche
h=b=d=g=zeros(m)
for i in range(m):
    h[i], b[i], d[i], g[i] = 1,1,1,1
h=csr_matrix(h)
b=csr_matrix(b)
d=csr_matrix(d)
g=csr_matrix(g)
f=kron(e1,h)+kron(g,e1)+kron(en,b)+kron(d,en)
f=f.transpose()

v0=ones((m*m,1))
v0[2,0]=2
v0[3,0]=5
v0=csr_matrix(v0)
def resolution(K, f, v0, k):
    r=[f-K*v0]
    Vk=r[0]
    Mk=K*Vk
    #On fait la décompostion QR :
    norme=linalg.norm(Mk[1,0])
    Q=Mk[:,0]/norme
    #On a donc M1 et Q1
    R=[norme]
    R=csr_matrix(R)
    #Maintenant qu'on a M1, Q1 et R1, trouvons alpha :
    alpha=R*transpose(Q)*f
    qk=transpose(Q)*K*r[0]
    qk=Q*qk
    qk=K*r[0]-qk
    S=norm(qk)
    qk=qk/S
    #On augmente maintenant le sev en calculant le residu :
    for i in range(1,k):
        r.append(r[i-1]-(qk*(transpose(qk)*r[0])))
        r[i]=csr_matrix(r[i])
        #On crée Vk+1
        Vk=hstack([Vk,r[i]])
        #Et le nouveau Q
        qk=transpose(Q)*K*r[i]
        qk=Q*qk
        qk=K*r[i]-qk
        S=norm(qk)
        qk=qk/S
        transQ=transpose(Q)
        Q=hstack([Q,qk])
        #Ainsi que le nouveau R
        R=hstack([R,transQ*K*r[i]])
        ligne=zeros((1,i+1))
        ligne=csr_matrix(ligne)
        R=vstack([R,ligne], format="csr")
        R[i,i]=S
    #On resoud le systeme :
    alpha=solve_triangular(R.todense(),(transpose(Q)*f).todense())
    vs=v0+Vk*alpha
    return r, vs, Vk, Q, R
r,vs,Vk,Q,R=resolution(K, f, v0, 50)

print('Liste des résidus successifs:\n {}'.format(r))

print('Approximation vk:\n {}'.format(vs))

print('Matrice Vk :\n {}'.format(Vk))

print('Matrice Qk :\n {}'.format(Q))

print('Matrice Rk :\n {}'.format(R))


#In [22] 
#Question (c)
def restarting(K, f, v0, k1, k2):
    r, vs, V, Q, R=resolution(K, f, v0, k2)
    for i in range(k1):
        r, vs, V, Q, R=resolution(K, f, r[0], k2)
    return r, vs, V, Q, R
r, vs, V, Q, R=restarting(K, f, v0, 50, 25)
print(vs)

#In [23] 
#Question (d)
vs=vs.reshape(m,m)
#In [24]
contour(vs)
#In [ ]
#Avec la fonction contourf :
contourf(vs)
#In [ ]
#Question (e)
print('Solutions obtenues :\n {}'.format(vs))

print('Solutions "exactes" (avec spsolve) :\n {}'.format(spsolve(K,f)))
