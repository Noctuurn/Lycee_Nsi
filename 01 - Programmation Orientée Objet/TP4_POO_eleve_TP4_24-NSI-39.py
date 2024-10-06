class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères 
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = ["192.168.0.0","192.168.0.255" ] 
        return self.adresse == reservees[0] or self.adresse == reservees[1]

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = self.liste_octets()[-1]
        if octets == 254: 
            return None
        octet_nouveau = int(octets) + 1 
        return AdresseIP('192.168.0.' + str(octet_nouveau)) 
    
adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')

print(
adresse1.liste_octets(),
adresse3.est_reservee(),
adresse2.adresse_suivante().adresse
)
