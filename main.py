# Projekt dla Gminy w ramach praktyk ze studiów
# Projekt zakłada, że słupy nad przejściami dla pieszych w gminie będą wysyłały informacje o prędkości pojazdów do bazy
# w której to algorytm będzie analizował dane pod względem wyszukania z nich możliwych anomali - tzn. piratów drogowych
# których to pomimo informowania ich o zbyt dużej prędkości przed przejściem dla pieszych nie zwalniają


import random
# generowanie losowych danych na potrzeby stworzenia programu


# stworzenie słownika w którym będą zapisane dane z poszczególnych miejscowości należących do gminy
import csv

from tkinter import *
from tkinter import filedialog

def algorytm(filepath):
        dict = {}
        dict2 = {}
        with open(filepath, 'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                        lista = []
                        dict2.update([(str(row[0].split(";")[0]), [])])
                        lista.append(int(row[0].split(";")[1]))
                        for i in row:
                                if row.index(i) == 0:
                                        continue
                                else:
                                        lista.append(int(i))
                        dict.update([(str(row[0].split(";")[0]), lista)])
                file.close()

        #       Zastosowanie algorytmu szukającego piratów drogowych

        for i in dict:
                potencjalni_piraci = 0
                piraci = 0
                zerowanie = 0
                lista_indeksow = []
                for k in range(len(dict[i]) - 2):
                        if (dict[i][k] > 60):
                                potencjalni_piraci += 1
                        if (dict[i][k] > 60 and dict[i][k + 1] > dict[i][k] and dict[i][k + 2] > dict[i][k + 1]):
                                piraci += 1

                dict2[i].append(len(dict[i]))
                dict2[i].append(potencjalni_piraci)
                dict2[i].append(piraci)

        najwięcej = ['Wola Raniżowska', dict2['Wola Raniżowska'][2] / dict2['Wola Raniżowska'][0]]

        for i in dict2:
                if dict2[i][2] / dict2[i][0] > najwięcej[1]:
                        najwięcej[1] = dict2[i][2] / dict2[i][0]
                        najwięcej[0] = i
        najwięcej[1] = najwięcej[1] * 100
        print("Największy odsetek piratów znajduje się w " + str(najwięcej[0]) + ", wynosił on " + str(round(najwięcej[1], 2)) + " %")

def openFile():
        filepath = filedialog.askopenfilename()
        # jeśli dodamy ścieżkę to folder w którym będziemy się pojawiać na początku będzie tym z ścieżki
        algorytm(filepath)

# odczytanie z pliku danych


from tkinter import *

window = Tk()


'''label = Label(window, text="Największy odsetek piratów znajduje się w " + str( najwięcej[0]) + ", wynosił on " + str(round(najwięcej[1],2)) + " %",
              font=('Arial',20,'bold'),
              fg='#00FF00',
              bg="black",
              relief=RAISED,
              width= 70,
              height= 10,
              bd=10,
              padx=20, # odstępy na osi x
              pady=20 # odstępy na osi y
              )  # stworzenie label
label.pack() # dodanie label do okna
# label.place(x=0,y=0) # dodanie label w konkretnym miejscu okna'''

button = Button(text="Open file", command=openFile)
button.pack()

window.mainloop()

