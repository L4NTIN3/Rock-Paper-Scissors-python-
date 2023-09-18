import random
import tkinter 
import tkinter as tk
from tkinter.ttk import *

def pelaa(luku):
    global kierrosmäärä
    global koneenvalinta
    global tulos
    global ottelunvoittaja

    pelaajanvalinta = luku

    pelaaja.set(lista[pelaajanvalinta])

    jopelattu = kierrosmäärä.get()
    kierrosmäärä.set(jopelattu + 1)
    koneenvalinta = random.randrange(3)
    tulos.set(lista[koneenvalinta])

    #kivi = 0
    #sakset = 1
    #paperi = 2

    if koneenvalinta == 0:
        if pelaajanvalinta == 0:
            ottelunvoittaja.set("Tasapeli")
        elif pelaajanvalinta == 1:
            ottelunvoittaja.set("Kone voitti")
        else:
            ottelunvoittaja.set("Pelaaja voitti")

    elif koneenvalinta == 1:
        if pelaajanvalinta == 0:
            ottelunvoittaja.set("Pelaaja voitti")
        elif pelaajanvalinta == 1:
            ottelunvoittaja.set("Tasapeli")
        else:
            ottelunvoittaja.set("Kone voittaa")

    elif koneenvalinta == 2:
        if pelaajanvalinta == 0:
            ottelunvoittaja.set("Kone voittaa")
        elif pelaajanvalinta == 1:
            ottelunvoittaja.set("Pelaaja voitti")
        else:
            ottelunvoittaja.set("Tasapeli")
    else:
        ottelunvoittaja.set("EI voitu määrittää")



#--------------- muuttujat ----------------


ikkuna = tk.Tk()
ikkuna.geometry("1000x700")
ikkuna.title("Kivi Sakset Paperi")

lista = ["kivi", "sakset", "paperi"]
koneenvalinta = 0
tulos = tkinter.StringVar()
ottelunvoittaja = tkinter.StringVar()
kierrosmäärä = tkinter.IntVar()
pelaaja = tkinter.StringVar()

nappityylit: Style = Style()
nappityylit.configure("napit",
                      border=0,
                      bg="#54688a")

Font_tuple = ("Roboto", 20, "bold")
Font_napit = ("Roboto", 12, "bold")



#----------------------layout ----------------------------



canvas = tk.Canvas(ikkuna,
                   bg="red",
                   height=1000,
                   width=1000)
canvas.pack()

pelinNimi = tk.Label(canvas,
                     text="Kivi-sakset-paperi")
pelinNimi.place(relx=0.2,
                rely=0.05,
                height=75,
                width=300)
pelinKuvaus = tk.Label(canvas,
                       text="En aio selittää sääntöjä",
                       border=0)
pelinKuvaus.place(relx=0.5,
                  rely=0.05,
                  height=75,
                  width=300)

#tulokset näyttävien kenttien teko ja sijoitus
vastus = tk.Entry(textvariable=tulos,
                  font=Font_tuple,
                  border=0)

vastus.insert(0, "Koneenvalinta")
vastus.place(relx=0.55,
             rely=0.2,
             height=100,
             width=250)

pelaajaScore = tk.Entry(textvariable=pelaaja,
                        font=Font_tuple,
                        border=0)
pelaajaScore.insert(0, "Pelaajanvalinta")
pelaajaScore.place(relx=0.2,
             rely=0.2,
             height=100,
             width=250,)

kierrokset = tk.Entry(canvas,
                      font= Font_napit,
                      textvariable=f"{kierrosmäärä}",
                      border=0)

kierrokset.place(relx=0.1,
                rely=0.5,
                height=50,
                width=60)

otteluntulos = tk.Entry(canvas,
                        textvariable=f"{ottelunvoittaja}",
                        font=Font_tuple,
                        border=0)
otteluntulos.insert(0, "Voittaja")
otteluntulos.place(relx=0.3,
                   rely=0.4,
                   height=100,
                   width=400)

#-------------------------- NAPPULAT ----------------------------


kivi = tk.Button(canvas,
                      text="Kivi",
                      height=5,
                      width=15,
                      command=lambda: pelaa(0),
                      font=Font_napit)
kivi.place(relx=0.3, rely=0.8, anchor="center")

sakset = tk.Button(canvas,
                      text="Sakset",
                      width=15,
                      height=5,
                      command=lambda: pelaa(1),
                      font=Font_napit
                      )
sakset.place(relx=0.5, rely=0.8, anchor="center")

paperi = tk.Button(canvas,
                      text="Paperi",
                      width=15,
                      height=5,
                      command=lambda: pelaa(2),
                      font=Font_napit
                      )
paperi.place(relx=0.7, rely=0.8, anchor="center")



ikkuna.mainloop()