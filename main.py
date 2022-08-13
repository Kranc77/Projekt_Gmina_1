# Projekt dla Gminy w ramach praktyk ze studiów
# Projekt zakłada, że słupy nad przejściami dla pieszych w gminie będą wysyłały informacje o prędkości pojazdów do bazy
# w której to algorytm będzie analizował dane pod względem wyszukania z nich możliwych anomali - tzn. piratów drogowych
# których to pomimo informowania ich o zbyt dużej prędkości przed przejściem dla pieszych nie zwalniają


import random
# generowanie losowych danych na potrzeby stworzenia programu


# stworzenie słownika w którym będą zapisane dane z poszczególnych miejscowości należących do gminy
dict = {'Wola Raniżowska': [],
        'Raniżów':[],
        'Staniszewskie':[],
        'Zielonka':[],
        'Mazury':[],
        'Korczowiska':[],
        'Posuchy':[],
        'Poręby Wolskie':[]
        }
dict2 = {'Wola Raniżowska': [],
        'Raniżów':[],
        'Staniszewskie':[],
        'Zielonka':[],
        'Mazury':[],
        'Korczowiska':[],
        'Posuchy':[],
        'Poręby Wolskie':[]
        }

for i in dict:
        for j in range(random.randint(100,1000)):
                dict[i].append(random.randint(35,120))
for i in dict:
        potencjalni_piraci = 0
        piraci = 0
        zerowanie = 0
        lista_indeksow = []
        for k in range(len(dict[i])-2):
                if (dict[i][k] > 50):
                        potencjalni_piraci += 1
                if (dict[i][k] > 50 and dict[i][k+1] > dict[i][k] and dict[i][k+2]>dict[i][k+1]):
                        piraci+=1


        dict2[i].append(len(dict[i]))
        dict2[i].append(potencjalni_piraci)
        dict2[i].append(piraci)
najwięcej = ['Wola Raniżowska',dict2['Wola Raniżowska'][2]/dict2['Wola Raniżowska'][0]]
for i in dict2:
        if dict2[i][2]/dict2[i][0] > najwięcej[1]:
                najwięcej[1] = dict2[i][2]/dict2[i][0]
                najwięcej[0] = i
najwięcej[1] = najwięcej[1]*100
print("Największy odsetek piratów znajduje się w " + str( najwięcej[0]) + ", wynosił on " + str(round(najwięcej[1],2)) + " %")



