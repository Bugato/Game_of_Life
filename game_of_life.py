from tkinter import *
from random import *

def damier(): #grid plotting function
    ligne_vert()
    ligne_hor()

def ligne_vert():  #vertical lines plotting function
    c_x = 0
    while c_x != width:
        can1.create_line(c_x,0,c_x,height,width=1,fill='black')
        c_x+=c

def ligne_hor(): #horizontal lines plotting function
    c_y = 0
    while c_y != height:
        can1.create_line(0,c_y,width,c_y,width=1,fill='black')
        c_y+=c

def click_gauche(event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='red')
    dico_case[x,y]=1


def click_droit(event): #function making the clicked cell alive so sets the value 1 for the clicked cell to dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='white')
    dico_case[x,y]=0

def change_vit(event): #function to change the speed (waiting between each step)
    global vitesse
    vitesse = int(eval(entree.get()))

def go():       #function to start the animation
    "démarrage de l'animation"
    global flag
    if flag ==0:
        flag =1
        play()

def stop():      #function to stop the animation
    "arrêt de l'animation"
    global flag
    flag =0

def play(): #function counting the number of living cells around each cell
    global flag, vitesse
    v=0
    vitesse=510-(b7.get()*5)   #speed of the animation (in reality it is the wait between each step in ms)
    while v!= width/c:
        w=0
        while w!= height/c:
            x=v*c
            y=w*c
            # special cases:
            # the corners
            if x==0 and y==0: #top left corner
                compt_viv=0
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==0 and y==int(height-c): #bottom left corner
                compt_viv=0
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(width-c) and y==0: #top right corner
                compt_viv=0
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(width-c) and y==int(height-c): #bottom right corner
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv

            # special cases:
            # the edges of the painting (without the corners)
            elif x==0 and 0<y<int(height-c): # left edge
                compt_viv=0
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif x==int(width-c) and 0<y<int(height-c): # right edge
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif 0<x<int(width-c) and y==0: # top edge
                compt_viv=0
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv
            elif 0<x<int(width-c) and y==int(height-c): # bottom edge
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv

            #generic cases
            #cells that are not in the borders of the table
            else:
                compt_viv=0
                if dico_case[x-c, y-c]==1:
                    compt_viv+=1
                if dico_case[x-c, y]==1:
                    compt_viv+=1
                if dico_case[x-c, y+c]==1:
                    compt_viv+=1
                if dico_case[x, y-c]==1:
                    compt_viv+=1
                if dico_case[x, y+c]==1:
                    compt_viv+=1
                if dico_case[x+c, y-c]==1:
                    compt_viv+=1
                if dico_case[x+c, y]==1:
                    compt_viv+=1
                if dico_case[x+c, y+c]==1:
                    compt_viv+=1
                dico_etat[x, y]=compt_viv

            w+=1
        v+=1
    redessiner()
    if flag >0:
        fen1.after(vitesse,play)


def redessiner(): #function redrawing the grid from dico_etat
    global height
    global width
    case=b4.get()
    height=case*c
    width=case*c
    nbcase=(height/c)*(width/c)
    can1.delete(ALL)
    damier()
    t=0
    while t!= width/c:
        u=0
        while u!= height/c:
            x=t*c
            y=u*c
            if dico_etat[x,y]==3:
                dico_case[x,y]=1
                can1.create_rectangle(x, y, x+c, y+c, fill='red')
            elif dico_etat[x,y]==2:
                if dico_case[x,y]==1:
                    can1.create_rectangle(x, y, x+c, y+c, fill='red')
                else:
                    can1.create_rectangle(x, y, x+c, y+c, fill='white')
            elif dico_etat[x,y]<2 or dico_etat[x,y]>3:
                dico_case[x,y]=0
                can1.create_rectangle(x, y, x+c, y+c, fill='white')
            u+=1
        t+=1


def close():          #function to close the window
    fen1.destroy()

def aleatoire(vie):         #returns 1 or 0 randomly depending on our percentage of life
        if random() < vie/100.0:
            return(1)
        else:
            return(0)

def initialiser():          #function initializing the grid
    can1.delete(ALL)
    damier()
    t=0
    vie=b6.get()
    while t!= width/c:
        u=0
        while u!= height/c:
            x=t*c
            y=u*c
            if aleatoire(vie) == 1:
                can1.create_rectangle(x, y, x+c, y+c, fill='red')
                dico_case[x,y]=1
            else:
                can1.create_rectangle(x, y, x+c, y+c, fill='white')
                dico_case[x,y]=0
            u+=1
        t+=1

#the different variables:
#initialization of the window size
width=1000
height=1000
#cell sizes
c=10
flag=0
dico_etat = {} #dictionary containing the number of living cells around each cell
dico_case = {} #dictionary containing the coordinates of each cell and a value of 0 or 1 if they are respectively dead or alive
i=0
while i!= width/c: #assigns a 0(dead) value to each coordinate(cell) (default value)
    j=0
    while j!= height/c:
        x=i*c
        y=j*c
        dico_case[x,y]=0
        j+=1
    i+=1

fen1 = Tk()
fen1.title('Jeu de la vie')
#layout of the elements

can1 = Canvas(fen1, width =50*c, height =50*c, bg ='white')
can1.bind("<Button-1>", click_gauche)
can1.bind("<Button-3>", click_droit)
can1.pack(side =LEFT)

damier()

b1 = Button(fen1, text ='Lancer', command =go, fg='blue',width=20)
b2 = Button(fen1, text ='Arreter', command =stop,fg='blue',width=20)
b1.pack(side =TOP)
b2.pack(side =TOP)
b3= Button(fen1, text = 'Quitter', command=close,fg='blue',width=20)
b3.pack(side=BOTTOM ,padx =0, pady =0)
b4 = Scale(orient= 'horizontal', from_=20, to=50,resolution=5,tickinterval=2,length=150,label='Taille de la grille')
b5 = Button(fen1, text ='Initialiser',command=initialiser,fg='blue',width=20)
b5.pack(side=TOP)
b6 = Scale(orient= 'horizontal', from_=0, to=100,resolution=1,length=150,label='% de Vie')
b7 = Scale(orient= 'horizontal', from_=0, to=100,resolution=5,length=150,label='Vitesse')
b7.set(50)
b6.set(50)
b4.set(50)
b7.pack(side=BOTTOM)
b6.pack(side=BOTTOM)
b4.pack(side=BOTTOM)
fen1.mainloop()
