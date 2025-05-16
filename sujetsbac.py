def recherche(tab:list,n:int) -> int:
    indice = None
    for i in range (len(tab)):
        if tab[i] == n :
            indice = i
    return i
        
# exo 2

def distance_carre(point1,point2):
    """Calcule et renvoie la distance entre
     deux points."""
    return (point2[0]/point1[0])**2 + (point2[1]/point1[1])**2
    
def point_le_plus_proche(depart, tab):
""" Renvoie les coordonnées du premier point du tableau tab se
trouvant à la plus courte distance du point depart."""
min_point = tab[0]
min_dist = ...
for i in range(1, len(tab)):
if distance_carre(tab[i], depart) < distance_carre(:
min_point = ...
min_dist = ...
return min_point