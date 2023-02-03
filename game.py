import importlib
from trump import *
from tkinter import *
from ilot import *

class Game():
    def __init__(self,window):
        """ Prend en entrée une fenêtre tkinter et 

        Args:
            window (tkinter): fenetre tkinter
        """
        self.window=window
        self.menubar = Menu(self.window,tearoff=0)
        self.game=Menu(self.menubar,tearoff=0)
        self.game.add_command(label="Play",command=self.play)
        self.game.add_command(label="Quit",command=self.window.quit)
        self.menubar.add_cascade(label="Game",menu=self.game)
        self.level_choice=Menu(self.menubar,tearoff=0)
        self.level1=self.level_choice.add_command(label="Level 1", command=lambda:self.set_level(1))
        self.level2=self.level_choice.add_command(label="Level 2", command=lambda:self.set_level(2))
        self.level3=self.level_choice.add_command(label="Level 3", command=lambda:self.set_level(3))
        self.level_choice.add_separator()
        self.about=self.level_choice.add_command(label="About", command=lambda:self.set_level(0))
        self.menubar.add_cascade(label="Level select",menu=self.level_choice)
        self.window.config(menu=self.menubar)
        self.score=Label(self.window,text="",font="Helvetic 14", foreground="Black", background="#EED")
        self.score.place(x=300,y=15)
        self.display=Canvas(self.window,width=600,height=450,bg="#114",bd=0)
        self.display.place(y=50)
        self.background=PhotoImage(file="images/background12.png")
        self.background_boss=PhotoImage(file="images/background3.png")
        self.heart=PhotoImage(file="images/heart.png")
        self.tweet_img=PhotoImage(file="images/twitter.png")
        self.trump_img=PhotoImage(file="images/trump.png")
        self.sombrero_img=PhotoImage(file="images/sombrero.png")
        self.cactus_img=PhotoImage(file="images/cactus.png")
        self.maracas_img=PhotoImage(file="images/maracas.png")
        self.crane_img=PhotoImage(file="images/crane.png")
        self.balle_img=PhotoImage(file="images/balle.png")
        self.bg=self.display.create_image(300,225,image=self.background)
        self.numero=1
        self.niveau=Label(self.window,text="",font="Helvetic 14", foreground="Black", background="#EED")
        self.niveau.place(x=625,y=15)
        self.start=Button(self.window,text="START",command=self.play)
        self.start.place(x=625,y=350)
        self.lifes=Canvas(self.window,width=50,height=150,background="#EED")
        self.lifes.place(x=625,y=150)
        self.stop=Button(self.window,text="PAUSE",command=self.pause_on_off)
        self.stop.place(x=625,y=400)
        self.quit=Button(self.window,text="QUIT",command=self.window.quit)
        self.quit.place(x=625,y=450)
        self.lines=[]
        self.ilots=[]
        self.shoots=[[],[]]
        self.pause=0
    def about_page(self):
        """page about
        """
        self.display.delete("all")
        self.niveau['text']="About"
        self.bg=self.display.create_image(300,225,image=self.background)
        self.display.create_text(10,10,anchor=NW,text="This game is a space invaders game like.",font="Helvetic 12 bold", fill="black")
        self.display.create_text(10,60,anchor=NW,text="There are several enemies :",font="Helvetic 12 bold", fill="black")
        self.display.create_text(50,110,anchor=NW,text="- Normal aliens (they can only kill you by touching you):",font="Helvetic 10 bold", fill="black")
        self.display.create_image(400,100,anchor=NW,image=self.maracas_img)
        self.display.create_text(450,100,anchor=NW,text="+10 pts ",font="Helvetic 12 bold", fill="red")
        self.display.create_text(50,160,anchor=NW,text="- Shooter aliens (like normal aliens but can shoot you):",font="Helvetic 10 bold", fill="black")
        self.display.create_image(400,150,anchor=NW,image=self.cactus_img)
        self.display.create_text(450,150,anchor=NW,text="+25 pts ",font="Helvetic 12 bold", fill="red")
        self.display.create_text(50,210,anchor=NW,text="- Bonus aliens :",font="Helvetic 10 bold", fill="black")
        self.display.create_image(150,200,anchor=NW,image=self.sombrero_img)
        self.display.create_text(220,200,anchor=NW,text="+100 pts ",font="Helvetic 12 bold", fill="red")
        self.display.create_text(50,260,anchor=NW,text="- Boss aliens :",font="Helvetic 10 bold", fill="black")
        self.display.create_image(150,220,anchor=NW,image=self.crane_img)
        self.display.create_text(250,250,anchor=NW,text="+1000 pts ",font="Helvetic 12 bold", fill="red")
        self.display.create_text(10,310,anchor=NW,text="You control Trump president using left and right key :",font="Helvetic 12 bold", fill="black")
        self.display.create_image(420,300,anchor=NW,image=self.trump_img)
        self.display.create_text(10,360,anchor=NW,text="You can send tweets to hurt the aliens using space bar :",font="Helvetic 12 bold", fill="black")
        self.display.create_image(450,360,anchor=NW,image=self.tweet_img)
        self.display.create_text(10,410,anchor=NW,text="Shooter aliens and Boss aliens can both shoot :",font="Helvetic 12 bold", fill="black")
        self.display.create_image(400,410,anchor=NW,image=self.balle_img)
    def set_level(self,level:int):
        if level==0:
            self.about_page()
        else:
            self.numero=level
        if level==3:
            self.bg=self.display.create_image(300,225,image=self.background_boss)
        elif level != 0:
            self.bg=self.display.create_image(300,225,image=self.background)
    def displifes(self):
        self.lifes.delete("all")
        for i in range(3-min([3,self.trump.get_life()]),3):
            self.lifes.create_image(25,25+i*50,image=self.heart)
    def play(self):
        self.pause=0
        self.lifes.delete("all")
        for i in range(1,4):
            self.level_choice.entryconfig("Level "+str(i),state=DISABLED)
        self.level_choice.entryconfig("About",state=DISABLED)
        self.game.entryconfig("Play",state=DISABLED)
        self.lines=[]
        self.ilots=[]
        self.shoots=[[],[]]
        self.display.delete("all")
        self.score['text']="Score : 0"
        self.niveau['text']="Level "+str(self.numero)
        if self.numero==3:
            self.bg=self.display.create_image(300,225,image=self.background_boss)
        else:
            self.bg=self.display.create_image(300,225,image=self.background)
        self.level=importlib.import_module("level"+str(self.numero))
        self.lines.append(self.level.line_bonus(self.display))
        self.lines.append(self.level.line_shooter(self.display))
        self.lines.append(self.level.line_normal(self.display))
        self.ilots.append(Ilot(75,300,10,7,self.display))
        self.ilots.append(Ilot(250,300,10,7,self.display))
        self.ilots.append(Ilot(425,300,10,7,self.display))
        self.start['state']=DISABLED
        self.trump=Trump(self.display,self.window)
        self.displifes()
        self.window.bind("<Right>",self.trump.move_right)
        self.window.bind("<Left>",self.trump.move_left)
        self.window.bind("<space>",lambda event,tirs=self.shoots[1]:self.trump.shoot(event,tirs))
        self.refresh()
    def pause_on_off(self):
        if self.pause==0:
            self.pause=1
        else:
            self.pause=0
            self.window.after(100,self.refresh)
    def refresh(self):
        # Aliens bougent, tirent
        for line in self.lines:
            line.setminmax()
            for alien in line.get_bonus():
                alien.set_pos()
                if alien.get_type()==1 or alien.get_type()==3:
                    alien.shot(self.shoots[0])
                for ilot in self.ilots:
                    ilot.delete(alien.get_posx(),alien.get_posy())
                if abs(alien.get_posx()-self.trump.get_pos()[0])<=10 and abs(alien.get_posy()-self.trump.get_pos()[1])<=10:
                    self.trump.get_shot()
        for tir in self.shoots[0]:
            tir.rise_pos()
            if abs(tir.get_posx()-self.trump.get_pos()[0])<=10 and abs(tir.get_posy()-self.trump.get_pos()[1])<=10:
                self.trump.get_shot()
                if tir in self.shoots[0]:
                    self.shoots[0].remove(tir)
                    tir.delete()
            for ilot in self.ilots:
                if ilot.delete(tir.get_posx(),tir.get_posy()) and tir in self.shoots[0]:
                    self.shoots[0].remove(tir)
                    tir.delete()
            if tir.get_posy()>450:
                self.shoots[0].remove(tir)
                tir.delete()
        for tir in self.shoots[1]:
            tir.rise_pos()
            for ilot in self.ilots:
                if ilot.delete(tir.get_posx(),tir.get_posy()) and tir in self.shoots[1]:
                    self.shoots[1].remove(tir)                
                    tir.delete()
            for line in self.lines:
                for alien in line.get_bonus():
                    if line==self.lines[0] and self.numero==3 and abs(tir.getpos()[0]-alien.getpos()[0])<=25 and abs(tir.getpos()[1]-alien.getpos()[1])<=25:
                        alien.get_shot()
                        if alien.get_life()<=0:
                            line.delete_alien(alien)
                            self.score["text"]="Score : "+str(int(self.score["text"].split(" : ")[1])+alien.get_score())
                        self.shoots[1].remove(tir)
                        tir.delete()
                    elif abs(tir.getpos()[0]-alien.getpos()[0])<=10 and abs(tir.getpos()[1]-alien.getpos()[1])<=10:
                        self.score["text"]="Score : "+str(int(self.score["text"].split(" : ")[1])+alien.get_score())
                        line.delete_alien(alien)
                        self.shoots[1].remove(tir)
                        tir.delete()
            if tir.get_posy()<0:
                self.shoots[1].remove(tir)
                tir.delete()
        self.displifes()
        if self.numero==3:
            if self.lines[0].get_bonus()!=[]:
                self.boss_cadre=self.display.create_rectangle(198,5,402,15,fill="black")
                self.boss_death=self.display.create_rectangle(200+10*self.lines[0].get_bonus()[0].get_life(),7,400,13,fill="white")
                self.boss_life=self.display.create_rectangle(200,7,200+10*self.lines[0].get_bonus()[0].get_life(),13,fill="red")
            else:
                self.boss_cadre=self.display.create_rectangle(198,5,402,15,fill="black")
                self.boss_death=self.display.create_rectangle(200,7,400,13,fill="white")
        if self.pause==1:
            return
        elif (self.lines[0].get_bonus() or self.lines[1].get_bonus() or self.lines[2].get_bonus()) and self.trump.get_life()!= 0:
           self.window.after(100,self.refresh)
        else:
            self.window.after(100,self.end_game)
    def end_game(self):
        """Finit la partie et affiche le score
        """
        for i in range(1,4):
            self.level_choice.entryconfig("Level "+str(i),state=NORMAL)
        self.level_choice.entryconfig("About",state=NORMAL)
        self.game.entryconfig("Play",state=NORMAL)
        self.display.create_rectangle(150,125,450,325,fill="#EED",width=5,outline="black")
        self.texte_2="Your score is "+str(self.score['text'])
        if self.trump.get_life()==0:
            self.texte_1="You lose\n"
        else:
            self.texte_1="You win\n"
        self.display.create_text(300,200,text=self.texte_1,font="Helvetic 18")
        self.display.create_text(300,250,text=self.texte_2,font="Helvetic 18")
        self.trump.set_life(0)
        self.start["state"]=NORMAL