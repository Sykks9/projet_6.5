from tkinter import PhotoImage

class Shoot():
    def __init__(self,posx:int,_type:int,posy:int,display,image):
        """Initialise un tir

        Args:
            posx (int): abcisse du tir
            _type (int): type du tir (1 : joueur, 0 : alien)
            posy (int): ordonnee du tir
        """
        self.posy=posy
        self.posx=posx
        self.display=display
        self.img=image
        self.image=self.display.create_image(self.posx,self.posy,image=self.img)
        self.type=_type
        if _type==1:
            self.sens=-1
        if _type==0:
            self.sens=1
    def get_posy(self):
        return self.posy
    def set_posy(self, value:int):
        self.posy=value
    def get_posx(self):
        return self.posx
    def set_posx(self, value:int):
        self.posx=value
    def getpos(self):
        return self.posx,self.posy
    def rise_pos(self):
        """fait varier l'ordonnee du tir
        """
        self.set_posy(self.posy+self.sens*10)
        self.display.coords(self.image,self.posx,self.posy)
    def delete(self):
        self.display.delete(self.image)