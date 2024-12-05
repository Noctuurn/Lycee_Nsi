class Cellule:
    """Classe représentant une cellule dans une liste chaînée."""
    def __init__(self, valeur, suivant=None):
        """
        Initialise une cellule.
        :param valeur : La valeur contenue dans la cellule.
        :param suivant : La cellule suivante dans la liste (par défaut None).
        """
        self.valeur = valeur
        self.suivant = suivant


class ListeChainee:
    """Classe représentant une liste chaînée."""
    def __init__(self):
        """Initialise une liste chaînée vide."""
        self.tete = None

    def creer_liste(self):
        """Réinitialise la liste en une liste vide."""
        self.tete = None

    def liste_vide(self):
        """Vérifie si la liste est vide.
        :return : True si la liste est vide, False sinon.
        """
        return self.tete is None

    def inserer(self, valeur):
        """Insère une valeur au début de la liste.
        :param valeur : La valeur à insérer.
        """
        nouvelle_cellule = Cellule(valeur, self.tete)
        self.tete = nouvelle_cellule

    def supprimer(self):
        """Supprime l'élément en tête de la liste."""
        if not self.liste_vide():
            self.tete = self.tete.suivant

    def tete_valeur(self):
        """Retourne la valeur de la tête de la liste."""
        return self.tete.valeur if self.tete else None

    def queue_valeur(self):
        """Retourne la valeur de la queue de la liste."""
        if self.liste_vide():
            return None
        courant = self.tete
        while courant.suivant:
            courant = courant.suivant
        return courant.valeur

    def compter(self):
        """Compte le nombre de cellules dans la liste."""
        compteur = 0
        courant = self.tete
        while courant:
            compteur += 1
            courant = courant.suivant
        return compteur

    def afficher(self):
        """Affiche les éléments de la liste chaînée."""
        elements = []
        courant = self.tete
        while courant:
            elements.append(courant.valeur)
            courant = courant.suivant
        print(" -> ".join(map(str, elements)))
