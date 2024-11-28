def creer_pile()-> list:
    return []

def pile_vide(pile)-> bool :
    if len(pile) == 0 :
        return True
    else : False

def empiler(pile,elt):
    pile.append(elt)

def depiler(pile)-> list :
     if not pile_vide(pile) :  
        return pile.pop() 
     
def taille(pile)-> int :
    return len(pile)

def sommet(pile)-> str :
    return pile[0]



class Pile :
    def __init__(self):
        self.items = []

    def empiler(self, elt):
        self.items.append(elt)

    def pop(self):
        return self.items.pop()

    def sommet(self):
        if self.est_vide():
            return None
        return self.items[-1]

    def est_vide(self):
        return len(self.items) == 0

    def taille(self):
        return len(self.items)


    def __str__(self):
        return f"Pile({self.items})"
