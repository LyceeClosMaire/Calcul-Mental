import random
import time

def adfacile():
    n1=random.randint(0,10)
    n2=random.randint(0,10)
    op= str(n1) + '+' + str(n2) + "="
    res=n1+n2
    return (op, res)

def play_adfacile() :
    pts = 0
    nquestion=0
    t=time.time()
    while nquestion != 10 :
                (op, res) = adfacile()
                resultat = int(input(op))
                if resultat == res :
                    pts = pts + 1
                    nquestion = nquestion + 1
                else :
                    pts = pts - 1
                    nquestion = nquestion + 1
    print("Vous avez " + str(pts) + " points")
    print("Vous avez mis " + str(time.time()-t) + " seconde" )

play_adfacile()
