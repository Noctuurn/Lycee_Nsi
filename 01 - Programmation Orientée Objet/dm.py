def note(cop, corr):
    # Initialiser la note à 0
    score = 0
    
    # Parcourir les deux listes avec un index
    for i in range(len(cop)):
        # Si la réponse est correcte, on incrémente la note
        if cop[i] == corr[i]:
            score += 1
    
    return score

def notes_paquet(p, corr):
    # Initialiser un dictionnaire pour stocker les notes des candidats
    resultat = {}
    
    # Parcourir chaque candidat et sa copie dans le paquet
    for candidat, copie in p.items():
        # Calculer la note pour chaque candidat en utilisant la fonction note
        resultat[candidat] = note(copie, corr)
    
    return resultat

# Exemple d'utilisation
p1 = {
    ('Tom', 'Matt'): [4, 1, 5, 4, 3, 3, 1, 4, 5, 3, 5, 1, 5, 5, 5, 1, 3, 3, 3, 3],
    ('Lambert', 'Ginne'): [2, 4, 2, 2, 1, 2, 4, 2, 2, 5, 1, 2, 5, 5, 3, 1, 1, 1, 4, 4],
    ('Carl', 'Roth'): [5, 4, 4, 2, 1, 4, 5, 1, 2, 2, 3, 2, 3, 3, 5, 2, 2, 3, 4, 4],
    ('Kurt', 'Jett'): [2, 5, 5, 3, 4, 1, 5, 3, 2, 3, 1, 3, 4, 1, 3, 1, 3, 2, 4, 4],
    ('Ayet', 'Finzerb'): [4, 3, 5, 3, 2, 1, 2, 1, 2, 4, 5, 5, 1, 4, 1, 5, 4, 2, 3, 4]
}

corr0 = [4, 2, 1, 4, 3, 5, 3, 3, 2, 1, 1, 3, 3, 5, 4, 4, 5, 1, 3, 3]

# Appel de la fonction pour obtenir les notes du paquet
notes = notes_paquet(p1, corr0)
print(notes)