# Créé par perigueux, le 20/03/2017 en Python 3.2
pts = 0
nquestion=0
n1=0
n2=0
import random
import time

t=time.time()


while nquestion != 10 :
    n1=random.randint(0,100)
    n2=random.randint(0,100)
    n3=n1+n2
    resultat = int(input( str(n1) + '+' + str(n2) + "="))
    if resultat == n3 :
        pts = pts + 1
        nquestion = nquestion + 1
    else :
        pts = pts - 1
        nquestion = nquestion + 1
print("Vous avez " + str(pts) + " points")
print("Vous avez mis " + str(time.time()-t + 1) + " seconde" )