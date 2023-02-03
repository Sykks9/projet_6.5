from block import *
from random import *

class Ilot():
    def __init__(self,posx:int,posy:int,sizex:int,sizey:int,display):
        """Initialise un ilot

        Args:
            posx (int): position en abcisse du coin en haut a gauche de l'ilot
            posy (int): position en ordonnée du coin en haut a gauche de l'ilot
            sizex (int): taille sur l'axe des abcisses
            sizey (int): taille sur l'axe des ordonnées
        """
        self.__posx__=posx
        self.__posy__=posy
        self.__sizex__=sizex
        self.__sizey__=sizey
        self.__blocks__=list()
        self.display=display
        for i in range(self.__posx__,self.__posx__ + 10 * (self.__sizex__ + 1), 10):
            for j in range(self.__posy__,self.__posy__ + 10 * (self.__sizey__ + 1),10):
                self.__blocks__.append(Block(choice(["#AAA","#999","#888","#777","#666","#555"]),i,j,display))
    def delete(self,x:int,y:int):
        """Verifie si les coordonnees appartiennent a un bloc de l'ilot et dans ce cas le retire de l'ilot

        Args:
            x (int): abcisse
            y (int): ordonnee

        Returns:
            Bool: True si trouve (donc retire) False sinon
        """
        for block in self.__blocks__:
            if block.del_wall(x,y):
                self.__blocks__.remove(block)
                return True
        return False