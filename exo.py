def ajoute_dictionnaires(d1:dict[int], d2:dict[int]) -> dict[int] :

    d = {}
    dmix = set(d1.keys()).union(set(d2.keys()))

    for clé in dmix :

        if clé in d1 and clé in d2:
            d[clé] = d1[clé] + d2[clé]

        elif clé in d1 :
            d[clé] = d1[clé]

        elif clé in d2 :
            d[clé] = d2[clé]

    return d

print("Exo 7 :",ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))



resultats = {'Dupont': {
                           'DS1': [15.5, 4],
                           'DM1': [14.5, 1],
                           'DS2': [13, 4],
                           'PROJET1': [16, 3],
                           'DS3': [14, 4]
                       },
             'Durand': {
                           'DS1': [6 , 4],
                           'DM1': [14.5, 1],
                           'DS2': [8, 4],
                           'PROJET1': [9, 3],
                           'IE1': [7, 2],
                           'DS3': [8, 4],
                           'DS4':[15, 4]
                       }
            }

def moyenne(nom:str, dico_result:dict) -> int :
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round( total_points / total_coefficients, 1 )
    else:
        return -1
print("Exo 8 :",moyenne("Durand",{'Dupont': {
                           'DS1': [15.5, 4],
                           'DM1': [14.5, 1],
                           'DS2': [13, 4],
                           'PROJET1': [16, 3],
                           'DS3': [14, 4]
                       },
             'Durand': {
                           'DS1': [6 , 4],
                           'DM1': [14.5, 1],
                           'DS2': [8, 4],
                           'PROJET1': [9, 3],
                           'IE1': [7, 2],
                           'DS3': [8, 4],
                           'DS4':[15, 4]
                       }
            }))