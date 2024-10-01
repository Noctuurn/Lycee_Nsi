class Eleve:
    '''
    La classe Eleve représente un élève.

    Création d'une instance :
    Eleve(pNom(str), pPrenom(str), pDate(list(int)), pNote1(int), pNote2(int), pNote3(int))
    
    Attributs de classe :
    matiere1
    matiere2
    matiere3

    Attributs d'instance : 
    nom
    prenom
    date
    note_mat1
    note_mat2
    note_mat3

    '''

    matiere1 = "Programmation"
    matiere2 = "Algorithmique"
    matiere3 = "Projet"
    # Méthodes
    def __init__(self, pNom, pPrenom, pDate, pNote1, pNote2, pNote3):
        self.nom = pNom
        self.prenom = pPrenom
        self.date = pDate
        self.note_mat1 = pNote1
        self.note_mat2 = pNote2
        self.note_mat3 = pNote3
    
    def __repr__(self):
        return f"Eleve(nom={self.nom}, prenom={self.prenom}, date={self.date}, notes=[{self.note_mat1}, {self.note_mat2}, {self.note_mat3}])"
    
    def __str__(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, Date de naissance: {self.date}, Notes: [{self.note_mat1}, {self.note_mat2}, {self.note_mat3}]"

    def moyenne(self):
        moy = (self.note_mat1 + self.note_mat2 + self.note_mat3) / 3
        return moy

def moy_matieres(liste_eleves: list) -> dict:
    
    somme_matiere1 = 0
    somme_matiere2 = 0
    somme_matiere3 = 0
    nb_eleves = len(liste_eleves)

    for eleve in liste_eleves:
        somme_matiere1 += eleve.note_mat1
        somme_matiere2 += eleve.note_mat2
        somme_matiere3 += eleve.note_mat3

    moyennes = {
        Eleve.matiere1: somme_matiere1 / nb_eleves,
        Eleve.matiere2: somme_matiere2 / nb_eleves,
        Eleve.matiere3: somme_matiere3 / nb_eleves
    }

    return moyennes

# Instances
dubois = Eleve("Dubois", "Camille", [1, 7, 2003], 7, 14, 11)
durand = Eleve("Durand", "Adrien", [1, 11, 2003], 13, 5, 17)
mazars = Eleve("Mazars", "Laurent", [25, 8, 2007], 2, 4, 14)

# Affichage des instances

print(moy_matieres([mazars,durand,dubois]))