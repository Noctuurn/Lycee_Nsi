class AdresseIP: 
 
    def __init__(self, adresse): 
        self.adresse = adresse
    
    def liste_octet(self): 
        """renvoie une liste de nombres entiers, 
           la liste des octets de l'adresse IP""" 
        return [int(i) for i in self.adresse.split(".")]  
         
    def est_reservee(self): 
        """renvoie True si l'adresse IP est une adresse 
           reservee, False sinon""" 
        return True or False
              
    def adresse_suivante(self): 
        """renvoie un objet de AdresseIP avec l'adresse  
           IP qui suit l'adresse self 
           si elle existe et False sinon""" 
        if self.adresse < 254: 
            octet_nouveau = octet_nouveau + 1 
            return AdresseIP('192.168.0.' + octet_nouveau) 
        else: 
            return False

adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')
print(
adresse1.est_reservee(),
adresse3.est_reservee(),
adresse2.adresse_suivante().adresse
)