import time
import random
import string

from tkinter import *

import colorama
from colorama import Fore


colorama.init()
print(Fore.RED)
myPencere = Tk()
myPencere.geometry("400x200+150+150")
L1 = Label(myPencere, text="Kaç haneli şifre oluşturulsun")
L1.pack( side = LEFT)
E1 = Entry(myPencere, bd =1)
E1.pack(side = RIGHT)
def uret():
    basamak = E1.get()
    basamak = int(basamak)
    myMetin = ""
    for x in range(0,basamak):
        myMetin += random.choice(string.ascii_letters+string.digits)
    print("uretilen sifre:::", myMetin)
    L1.config(text=myMetin)
def kaydet():
    E1.config(text="abah")
myLable = Label(myPencere)
myLable.pack()
btnEkle = Button(text="şifre üret", command=uret)
btnEkle.pack()
mainloop()
dosya=open("myfile.txt","w")

