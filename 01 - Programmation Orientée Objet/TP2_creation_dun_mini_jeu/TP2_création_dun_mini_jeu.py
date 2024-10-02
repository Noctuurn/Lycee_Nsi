from random import randint
class Personnage: 
    """ 
    Personnage d'un jeu de type hack 'n slash 
 
    Attributs d’instance: 
        nom : chaine de caractères, nom du personnage 
        pv : entier positif ou nul, points de vie du personnage 
        degats : entier >0, dégat maximum du personnage  
    Méthodes: 
        init() constructeur de la classe Personnage 
        attaque() : renvoie les dégâts faits à l'adversaire  
        nombre aléatoire compris entre 1 et degats avec randint() 
    """
    def __init__(self,nom,pv,degats):
        self.nom = nom
        self.pv = pv
        self.degats = degats

    def attaque(self) : 
        if perso1.degats <= 0 :
            print(f"{perso1.nom} est pacifiste !")
        elif perso2.degats <= 0 :
            print(f"{perso2.nom} est pacifiste !")
        else :
                print("----------------- DEBUT DU COMBAT -------------------")
                while perso1.pv > 0 and perso2.pv > 0 :
                    # attaque du personnage 1
                    dmg = randint(1,perso1.degats)
                    perso2.pv -= dmg
                    print(f"{perso1.nom} inflige {dmg} points de dégats ! {perso2.nom} se retrouve à {perso2.pv} pv")
                    if perso2.pv <= 0 :
                         print(f"{perso1.nom} a mis une balle d'operator à {perso2.nom} !")
                    # attaque du personnage 2
                    dmg = randint(1,perso2.degats)
                    perso1.pv -= dmg
                    print(f"{perso2.nom} inflige {dmg} points de dégats ! {perso1.nom} se retrouve à {perso1.pv} pv")
                    if perso1.pv <= 0:
                         print(f"{perso2.nom} a one-tap {perso1.nom} !")

            
                    
                return "----------------- FIN DU COMBAT -------------------"
                              
                    
            


perso1 = Personnage("Jett",150,10)
perso2 = Personnage("Cypher",150,10)
print(Personnage.attaque(perso1))
