class Block():
    def __init__(self,color:str,posx:int,posy:int,display):
        """Initialise un bloc

        Args:
            color (str): Code RGB de la couleur
            posx (int): abcisse du coin superieur gauche du bloc
            posy (int): ordonnee du coin superieur gauche du bloc
        """
        self.__posx__=posx
        self.__posy__=posy
        self.__color__=color
        self.display=display
        self.__wall__=self.display.create_rectangle(posx,posy,posx+10,posy+10,fill=color,width=0)
    def __str__(self):
        return "Block : x = " + str(self.__posx__) + ", y = " + str(self.__posy__) + ",couleur = " + self.__color__
    def get_posx(self):
        return self.__posx__
    def get_posy(self):
        return self.__posy__
    def get_color(self):
        return self.__color__
    def get_wall(self):
        return self.__wall__
    def del_wall(self,x:int,y:int):
        """Verifie si les coordonnees entrees appartiennent au bloc

        Args:
            x (int): abcisse
            y (int): ordonnee

        Returns:
            Bool: True si trouve (et supprime) False sinon
        """
        if x >= self.__posx__ and x <= self.__posx__ + 10 and y >= self.__posy__ and y <= self.__posy__ + 10:
            self.display.delete(self.__wall__)
            return True
        return False