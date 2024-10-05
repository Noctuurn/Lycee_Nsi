# Exercice 1
class Heure1:
    '''
    La clase Heure1 représente une horloge

    Création d'une instance :
    Heure1(HeureInit(int),MinuteInit(int))

    Attributs de classe :
    __heure,
    __minute,

    Attributs d'instance :
    nouvelleHeure,
    nouvelleMinute

    '''
    def __init__(self,heureInit=0,minuteInit=0) -> str :
        self.__heure = heureInit
        self.__minute = minuteInit

    def getHeure(self):
        return self.__heure
    
    def getMinute(self):
        return self.__minute
    
    def setHeure(self,nouvelleHeure):
        self.__heure = nouvelleHeure

    def setMinute(self,nouvelleMinute):
        self.__minute = nouvelleMinute

    def incrementer(self):
        self.__minute +=  1
        if self.__minute >= 60 :
            self.__minute = 0
            self.__heure += 1
        if self.__heure >= 24 :
            self.__minute = 0
            self.__heure = 0
    def __str__(self):
        return f"{self.__heure}:{self.__minute}"
    
# Exercice 2
print("Exercice 2 Pré-Incrémentation")
h1 = Heure1(22,12)
print(h1.getHeure()) 
print(h1.getMinute())
print(h1)
print("Incrémentation et post-incrémentation")
h1.setHeure(23)
h1.setMinute(59)
print(h1)
h1.incrementer()
print(h1)

# Exercice 3
class Heure2:
    '''
    La clase Heure2 représente une horloge

    Création d'une instance :
    Heure1(HeureInit(int),MinuteInit(int))

    Attributs de classe :
    __minute

    Attributs d'instance :
    nouvelleHeure,
    nouvelleMinute

    '''
    def __init__(self,heureInit=0,minuteInit=0) -> str :
        self.__minute = minuteInit + heureInit*60

    def getHeure(self):
        return self.__minute // 60
    
    def getMinute(self):
        return self.__minute % 60
    
    def setHeure(self,nouvelleHeure):
        self.__minute = nouvelleHeure*60


    def setMinute(self,nouvelleMinute):
        self.__minute += nouvelleMinute

    def incrementer(self):
        self.__minute +=  1

        if self.__minute//60 >= 24 :
            self.__minute = 0

    def __str__(self):
        return f"{self.__minute//60}:{self.__minute%60}"

# Exercice 4

print("Exercice 4 Pré-Incrémentation")
h2 = Heure2(22,12)
print(h2.getHeure()) 
print(h2.getMinute())
print(h2)
print("Incrémentation et post-incrémentation")
h2.setHeure(23)
h2.setMinute(59)
print(h2)
h2.incrementer()
print(h2)


class Heure3:
    '''
    La clase Heure3 représente une horloge

    Création d'une instance :
    Heure3(hh(int),mm(int),ss(int))

    Attributs de classe :
    heure,
    minute,
    seconde,

    Attributs d'instance :
    h
    '''
    def __init__(self,hh=0,mm=0,ss=0) -> str :
        self.heure = hh
        self.minute = mm
        self.seconde = ss

    def afficheHeure(self):
        return f"{self.heure}:{self.minute}:{self.seconde}"
    
    def setHeure(self,h):
        self.heure = h

# Exercice 6 
h3 = Heure3()
print("Exercice 6",h3.afficheHeure())
h3.setHeure(13) , print(h3.afficheHeure())
recreation = Heure3(9,50,18)
print(recreation.afficheHeure())