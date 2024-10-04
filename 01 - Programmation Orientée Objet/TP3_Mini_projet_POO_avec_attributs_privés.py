class Heure1:
    def __init__(self,heureInit=0,minuteInit=0) -> str :
        self.__heure = heureInit
        self.__minute = minuteInit

    def getHeure(self):
        return self.__heure
    
    def getMinute(self):
        return self.__minute
    
    def setHeure(self,nouvelleHeure):
        set.__heure = nouvelleHeure

    def setMinute(self,nouvelleMinute):
        set.__minute = nouvelleMinute

    def incrementer(self):
        set.__minute = self.__minute + 1
        if self.__minute > 60 :
            set.__minute = 0
            set.__heure = self.__heure + 1
        if self.__heure > 23 :
            set.__minute = 0
            set.__heure = 0
    def __str__(self):
        return f"{self.__heure}:{self.__minute}"
horloge = Heure1()