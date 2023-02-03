from tkinter import PhotoImage
from shoot import *

class Trump():
    def __init__(self,display,window):
        self.posx=300
        self.posy=425
        self.display=display
        self.trump=PhotoImage(file="images/trump.png")
        self.image=display.create_image(self.posx,self.posy,image=self.trump)
        self.img_shoot=PhotoImage(file="images/twitter.png")
        self.window=window
        self.life=3
    def move_right(self,event):
        if self.posx+10 < 585:
            self.posx+=10
        self.replace()
    def move_left(self,event):
        if self.posx-10>15:
            self.posx-=10
        self.replace()
    def replace(self):
        self.display.coords(self.image,self.posx,self.posy)
    def get_shot(self):
        self.life-=1
    def get_life(self):
        return self.life
    def get_pos(self):
        return self.posx,self.posy
    def set_life(self,life:int):
        self.life=life
    def shoot(self,event,liste:list):
        liste.append(Shoot(self.posx,1,self.posy-15,self.display,self.img_shoot))