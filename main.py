from tkinter import *
import game

fenetre=Tk()
fenetre.config(background="#EED")
fenetre.geometry("700x500")
fenetre.title("Trump VS Mexicans")
fenetre.iconphoto(True,PhotoImage(file="images/trump.png"))

Jeu = game.Game(fenetre)

fenetre.mainloop()