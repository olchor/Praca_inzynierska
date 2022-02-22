import numpy as np

#Zmienne, do których są zapisane wartości podane przez użytkownika
x_zakres = int(input('Podaj ile razy powielić komórkę elementarną wzdłuż osi x:\t'))
y_zakres = int(input('Podaj ile razy powielić komórkę elementarną wzdłuż osi y:\t'))
ziarno = int(input('Podaj ziarno(seed):\t'))
procent_defektow = float(input('Podaj w ilu komórkach elementarnych ma występować defekt(w %):\t'))

#Tablice służące do magazynowania współrzędnych atomów
wspolrzedne_x = []
wspolrzedne_y = []

#Pętla generująca współrzędne x i y wszystkich atomów
for i in range(0,x_zakres):

    x = [0.71, 1.42, 2.84, 3.55]

    x[0] = x[0] + 4.26 * i
    x[1] = x[1] + 4.26 * i
    x[2] = x[2] + 4.26 * i
    x[3] = x[3] + 4.26 * i

    for j in range(0, y_zakres):

        y = [1.23, 0.0, 0.0, 1.23]

        y[0] = y[0] + 2.46 * j
        y[1] = y[1] + 2.46 * j
        y[2] = y[2] + 2.46 * j
        y[3] = y[3] + 2.46 * j

        wspolrzedne_x.extend((x[0], x[1], x[2], x[3]))
        wspolrzedne_y.extend((y[0], y[1], y[2], y[3]))

f = open('grafen.data','w')

#Zdefiniowanie dalej wykorzystywanych zmiennych
np.random.seed(ziarno)
liczba_atomow = x_zakres * y_zakres * 4
liczba_defektow = x_zakres * y_zakres * procent_defektow/100
tablica_zer = [0] * (x_zakres*y_zakres)
macierz = np.reshape(np.array(tablica_zer),(x_zakres,y_zakres))

#Pętla wpisująca jedynki w macierz zer
for i in range(0, round(liczba_defektow)):
    while True:
        
        x1 = np.random.randint(2,x_zakres-2)
        y1 = np.random.randint(2,y_zakres-2)
        
        if macierz[x1][y1] == 1:
            continue
        
        sprawdzane_macierze = [
            macierz[x1+1][y1],
            macierz[x1+1][y1+1],
            macierz[x1+1][y1-1],
            macierz[x1][y1+1],
            macierz[x1][y1-1],
            macierz[x1-1][y1+1],
            macierz[x1-1][y1],
            macierz[x1-1][y1-1],
            macierz[x1+2][y1-1],
            macierz[x1+2][y1+1],
            macierz[x1+2][y1-1],
            macierz[x1-2][y1-1],
            macierz[x1+1][y1-2],
            macierz[x1+1][y1+2],
            macierz[x1-1][y1+2],
            macierz[x1-1][y1-2],
            macierz[x1+2][y1],
            macierz[x1-2][y1],
            macierz[x1][y1-2],
            macierz[x1][y1+2]
        ]
        
        #Sprawdzenie warunku, który musi być spełniony, żeby na pewno defekty na siebie nie nachodziły
        if any(sprawdzane_macierze):
            continue

        macierz[x1][y1] = 1
        
        break

macierz = macierz.flatten()

a = -1

for i in macierz:
    
    a += 1
    if i == 1:
       
        #Zmienna o losowej wartości decydująca, dla którego z atomów w komórce elementarnej występuje defekt
        r1 = np.random.randint(1,4)

        #Zmienna o losowej wartości decydująca, dla którego wiązania wcześniej wylosowanego atomu występuje defekt
        r2 = np.random.randint(1,3)

        #Część, która zmienia współrzędne atomów, dla których występuje defekt
        if r1 == 1:
            
            if r2 == 1:
                wspolrzedne_x[a*4] = wspolrzedne_x[a*4] - 0.71
                wspolrzedne_y[a*4] = wspolrzedne_y[a*4] + 0.82
                wspolrzedne_x[a*4-y_zakres*4+3] = wspolrzedne_x[a*4-y_zakres*4+3] + 0.71
                wspolrzedne_y[a*4-y_zakres*4+3] = wspolrzedne_y[a*4-y_zakres*4+3] - 0.82
            
            elif r2 == 2:
                wspolrzedne_x[a*4] = wspolrzedne_x[a*4] - 0.26
                wspolrzedne_y[a*4] = wspolrzedne_y[a*4] - 0.97
                wspolrzedne_x[a*4+1] = wspolrzedne_x[a*4+1] + 0.26
                wspolrzedne_y[a*4+1] = wspolrzedne_y[a*4+1] + 0.97
            
            elif r2 == 3:
                wspolrzedne_x[a*4] = wspolrzedne_x[a*4] - 0.26
                wspolrzedne_y[a*4] = wspolrzedne_y[a*4] + 0.97
                wspolrzedne_x[a*4+5] = wspolrzedne_x[a*4+5] + 0.26
                wspolrzedne_y[a*4+5] = wspolrzedne_y[a*4+5] - 0.97
       
        elif r1 == 2:
            
            if r2 == 1:
                wspolrzedne_x[a*4+3] = wspolrzedne_x[a*4+3] + 0.26
                wspolrzedne_y[a*4+3] = wspolrzedne_y[a*4+3] - 0.97
                wspolrzedne_x[a*4+3-1] = wspolrzedne_x[a*4+3-1] - 0.26
                wspolrzedne_y[a*4+3-1] = wspolrzedne_y[a*4+3-1] + 0.97
           
            elif r2 == 2:
                wspolrzedne_x[a*4+3] = wspolrzedne_x[a*4+3] + 0.26
                wspolrzedne_y[a*4+3] = wspolrzedne_y[a*4+3] + 0.97
                wspolrzedne_x[a*4+3+3] = wspolrzedne_x[a*4+3+3] - 0.26
                wspolrzedne_y[a*4+3+3] = wspolrzedne_y[a*4+3+3] - 0.97
           
            elif r2 == 3:
                wspolrzedne_x[a*4+3] = wspolrzedne_x[a*4+3] + 0.71
                wspolrzedne_y[a*4+3] = wspolrzedne_y[a*4+3] + 0.82
                wspolrzedne_x[a*4+3+y_zakres*4-3] = wspolrzedne_x[a*4+3+y_zakres*4-3] - 0.71
                wspolrzedne_y[a*4+3+y_zakres*4-3] = wspolrzedne_y[a*4+3+y_zakres*4-3] - 0.82
       
        elif r1 == 3:
          
            if r2 == 1:
                wspolrzedne_x[a*4+2] = wspolrzedne_x[a*4+2] - 0.71
                wspolrzedne_y[a*4+2] = wspolrzedne_y[a*4+2] + 0.82
                wspolrzedne_x[a*4+2-1] = wspolrzedne_x[a*4+2-1] + 0.71
                wspolrzedne_y[a*4+2-1] = wspolrzedne_y[a*4+2-1] - 0.82
           
            elif r2 == 2:
                wspolrzedne_x[a*4+2] = wspolrzedne_x[a*4+2] - 0.26
                wspolrzedne_y[a*4+2] = wspolrzedne_y[a*4+2] - 0.97
                wspolrzedne_x[a*4+2-3] = wspolrzedne_x[a*4+2-3] + 0.26
                wspolrzedne_y[a*4+2-3] = wspolrzedne_y[a*4+2-3] + 0.97
           
            elif r2 == 3:
                wspolrzedne_x[a*4+2] = wspolrzedne_x[a*4+2] - 0.26
                wspolrzedne_y[a*4+2] = wspolrzedne_y[a*4+2] + 0.97
                wspolrzedne_x[a*4+2+1] = wspolrzedne_x[a*4+2+1] + 0.26
                wspolrzedne_y[a*4+2+1] = wspolrzedne_y[a*4+2+1] - 0.97
       
        elif r1 == 4:
           
            if r2 == 1:
                wspolrzedne_x[a*4+1] = wspolrzedne_x[a*4+1] + 0.26
                wspolrzedne_y[a*4+1] = wspolrzedne_y[a*4+1] + 0.97
                wspolrzedne_x[a*4+1-1] = wspolrzedne_x[a*4+1-1] - 0.26
                wspolrzedne_y[a*4+1-1] = wspolrzedne_y[a*4+1-1] - 0.97
           
            elif r2 == 2:
                wspolrzedne_x[a*4+1] = wspolrzedne_x[a*4+1] + 0.71
                wspolrzedne_y[a*4+1] = wspolrzedne_y[a*4+1] + 0.82
                wspolrzedne_x[a*4+1+1] = wspolrzedne_x[a*4+1+1] - 0.71
                wspolrzedne_y[a*4+1+1] = wspolrzedne_y[a*4+1+1] - 0.82
            
            elif r2 == 3:
                wspolrzedne_x[a*4+1] = wspolrzedne_x[a*4+1] + 0.26
                wspolrzedne_y[a*4+1] = wspolrzedne_y[a*4+1] - 0.97
                wspolrzedne_x[a*4+1-5] = wspolrzedne_x[a*4+1-5] - 0.26
                wspolrzedne_y[a*4+1-5] = wspolrzedne_y[a*4+1-5] + 0.97

#Informacje niezbędne, do odczytu przez program LAMMPS    
f.write(f'\n\n{liczba_atomow} atoms\n1 atom types\n')
f.write(f'0 {4.26 * x_zakres} xlo xhi\n0 {2.46 * y_zakres} ylo yhi\n-10 10 zlo zhi\n\n')
f.write('Atoms\n\n')

for i in range(0,liczba_atomow):
    
    wspolrzedne_x[i] = round(wspolrzedne_x[i],2)
    wspolrzedne_y[i] = round(wspolrzedne_y[i],2)
    f.write(f'{i+1} 1 {wspolrzedne_x[i]} {wspolrzedne_y[i]} 0.0\n')

f.close