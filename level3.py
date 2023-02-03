from alien import *

class line_bonus():
    def __init__(self,display):
        """Classe générant une ligne d'alien boss
        """
        self.__aliens__=[]
        self.display=display
        self.__aliens__.append(Alien(100,50,3,100,500,self.display))
    def delete_alien(self,alien:Alien):
        """Verifie si l'alien est dans la liste et le supprime si oui

        Args:
            alien (Alien): alien a supprimer

        Returns:
            Bool: True si trouve (et supprime) False sinon
        """
        if alien in self.__aliens__:
            self.__aliens__.remove(alien)
            alien.delete()
            return True
        return False
    def get_bonus(self):
        return self.__aliens__
    def setminmax(self):
        for alien in self.__aliens__:
            alien.set_xmin(self.get_min())
            alien.set_xmax(self.get_max())
    def get_min(self):
        return self.__aliens__[0].get_posx()
    def get_max(self):
        return self.__aliens__[-1].get_posx()

class line_shooter():
    def __init__(self,display):
        """initialise un ligne d'alien shooter
        """
        self.__aliens__=[]
        self.display=display
        for i in range(100,550,50):
            self.__aliens__.append(Alien(i,150,1,100,500,self.display))
    def delete_alien(self,alien:Alien):
        """Cherche et supprime un alien

        Args:
            alien (Alien): alien a supprimer

        Returns:
            Bool: True si trouve (et supprime) False sinon
        """
        if alien in self.__aliens__:
            self.__aliens__.remove(alien)
            alien.delete()
            return True
        return False
    def get_bonus(self):
        return self.__aliens__
    def setminmax(self):
        for alien in self.__aliens__:
            alien.set_xmin(self.get_min())
            alien.set_xmax(self.get_max())
    def get_min(self):
        return self.__aliens__[0].get_posx()
    def get_max(self):
        return self.__aliens__[-1].get_posx()

class line_normal():
    def __init__(self,display):
        """Initialise un ligne d'alien normaux
        """
        self.__aliens__=[]
        self.display=display
        for i in range(100,550,50):
            self.__aliens__.append(Alien(i,200,0,100,500,self.display))
    def delete_alien(self,alien:Alien):
        """Cherche et supprime un alien

        Args:
            alien (Alien): alien a supprimer

        Returns:
            Bool: True si trouve (et supprime) False sinon
        """
        if alien in self.__aliens__:
            self.__aliens__.remove(alien)
            alien.delete()
            return True
        return False
    def get_bonus(self):
        return self.__aliens__
    def setminmax(self):
        for alien in self.__aliens__:
            alien.set_xmin(self.get_min())
            alien.set_xmax(self.get_max())
    def get_min(self):
        return self.__aliens__[0].get_posx()
    def get_max(self):
        return self.__aliens__[-1].get_posx()