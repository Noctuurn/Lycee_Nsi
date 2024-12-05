liste_chainee = ("n",("s",("i",None)))
liste_v = (None,None)

def creer_liste() -> tuple :
    lis = (None,None)
    return lis

def liste_vide(lis:tuple) -> bool:
    if lis == (None,None):
        return True
    else : 
        return False

def inserer(lis:tuple,elt)-> tuple :
    lis = (elt,lis)
    return lis 

def suppr(lis:tuple)-> tuple :
    sup,lis = lis[0],lis[1]
    return sup

def tete(lis:tuple)-> tuple :
    return lis[0]

def queue(lis:tuple)-> tuple :
    return lis[1]

def compte(lis:tuple)-> int :
    longueur = 0
    for _ in range(len(lis)):
        longueur += 1
    return longueur
        


if __name__ == "__main__":
    print(liste_chainee)
    creer_liste()
    print(liste_vide(liste_v))

    inserer(liste_chainee,"TG6")
    suppr(liste_chainee)
    tete(liste_chainee)
    queue(liste_chainee)
    compte(liste_chainee)
    print("Tous les tests unitaires marchent !")



