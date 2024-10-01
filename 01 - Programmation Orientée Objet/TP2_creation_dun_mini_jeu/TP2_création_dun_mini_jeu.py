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


perso1 = Personnage()
perso2 = Personnage()