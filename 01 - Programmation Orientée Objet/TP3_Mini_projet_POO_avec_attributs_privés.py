class Heure1:
    def __init__(self,heureInit=0,minuteInit=0) :
        self.__heure = heureInit
        self.__minute = minuteInit
    def getHeure(self):
        return self.__heure
    def getMinute(self):
        return self.__minute
    def setHeure(nouvelleHeure):
        ...