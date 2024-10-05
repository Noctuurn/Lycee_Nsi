class Heure1:
    '''
    La clase Heure1 représente une horloge

    Création d'une instance :
    Heure1(HeureInit(int),MinuteInit(int))

    Attributs de classe :
    heureInit,
    minuteInit

    Attributs d'instance :
    
    __heure,
    __minute,
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
print("Pré-Incrémentation")
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


class Heure2:
    '''
    La clase Heure2 représente une horloge

    Création d'une instance :
    Heure1(HeureInit(int),MinuteInit(int))

    Attributs de classe :
    Aucun

    Attributs d'instance :
    
    __heure,
    __minute,
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