from shoot import *
from random import *
from tkinter import PhotoImage

class Alien():
    def __init__(self,posx:int,posy:int,_type:int,xmax:int,xmin:int,display):
        """Initialise un alien

        Args:
            posx (int): position sur l'axe des abcisse
            posy (int): position sur l'axe des ordonnee
            _type (int): type (3 : boss, 2 : bonus, 1 : shooter, 0 : normal)
            xmax (int): position maximale sur l'axe des abcisses
            xmin (int): position minimale sur l'axe des ordonnees
        """
        self.posx=posx
        self.posy=posy
        self.xmax=xmax
        self.xmin=xmin
        self.sens=1
        self.type=_type
        self.display=display
        if _type==3:
            self.img=PhotoImage(file="images/crane.png")
            self.score=1000
            self.bosslife=20
        if _type==2:
            self.img=PhotoImage(file="images/sombrero.png")
            self.score=100
        if _type==1:
            self.img=PhotoImage(file="images/cactus.png")
            self.score=25
        if _type==0:
            self.img=PhotoImage(file="images/maracas.png")
            self.score=10
        self.image=self.display.create_image(posx,posy,image=self.img)
    def get_score(self):
        return self.score
    def set_pos(self):
        """gère le mouvement de l'alien
        """
        if self.sens==-1:
            if self.xmax<550:
                self.posx+=10
            else:
                self.sens*=-1
                self.posy+=10
        elif self.sens==1:
            if self.xmin>50:
                self.posx-=10
            else:
                self.sens*=-1
                self.posy+=10
        self.display.coords(self.image,self.posx,self.posy)
    def __str__(self):
        return "Alien : x : "+str(self.posx)+";y : "+str(self.posy)
    def get_posx(self):
        return self.posx
    def get_posy(self):
        return self.posy
    def get_type(self):
        return self.type
    def getpos(self):
        return self.posx,self.posy
    def get_shot(self):
        if self.type==3:
            self.bosslife-=1
    def get_life(self):
        return self.bosslife
    def delete(self):
        """supprime l'alien du canvas
        """
        self.display.delete(self.image)
    def set_xmin(self,xmin:int):
        self.xmin=xmin
    def set_xmax(self,xmax:int):
        self.xmax=xmax
    def shot(self,shoot:list):
        """Génère un tir

        Args:
            shoot (list): liste des tirs à générer
        """
        if randint(0,int(19/self.type))==0:
            shoot.append(Shoot(self.posx,0,self.posy+15,self.display,PhotoImage(file="images/balle.png")))
