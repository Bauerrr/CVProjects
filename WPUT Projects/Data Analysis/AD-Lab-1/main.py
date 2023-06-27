import numpy as np

# #tablice:
# b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# c = np.arange(100)
# d = np.linspace(0,2,10)
# e = np.arange(0,105,5)
# print(e)
# b = b.transpose()
# print(b)

# #liczby losowe:
# a = np.round_(np.random.normal(size=20),2)
# b = np.random.randint(1,1000,100)
# c = np.zeros((3,2))
# d = np.ones((3,2))
# e = np.random.randint(0,100,(5,5),dtype='int32')

# #liczby losowe zadania:
# a = np.random.uniform(0,10,100)
# b = np.copy(a.astype(int))
# a = np.round_(a)
# a = a.astype(int)
# c = a - b
# print(c)
# print("Wniosek: występuje różnica w zaokrąglaniu za pomocą round_ i astype, round zaokrągla od 0.5 w górę, kiedy astype po prostu ucina")

# #Selekcja danych:
# b = np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype=np.int32)
# print(b[0,(1,3)])
# print(b[0])
# print(b[:,1])
# a = np.random.randint(0,100,(2,7))
# print(a)
# print(a[:,(0,1,2,3)])

# #Działania matematyczne i logiczne:
# a = np.random.randint(1,10,(3,3))
# b = np.random.randint(1,10,(3,3))
# # print(a+b)
# # print(np.add(a,b))
# # print(a-b)
# # print(np.subtract(a,b))
# # print(a*b)
# # print(np.multiply(a,b))
# # print(np.dot(a,b))
# # print(np.matmul(a,b))
# # print(a/b)
# # print(np.divide(a,b))
# # print(a**b)
# # print(np.power(a,b))
# print(a.all()>=4 and a.all()<=1)
#
# #np.matrix.sum

# #Dane statystyczne:
# b = np.array([[1,2,3,4,5],[6,7,8,9,10]],dtype=np.int32)
# print(np.sum(b))
# print(np.min(b))
# print(np.max(b))
# print(np.std(b))
# print(np.mean(b,0))
# print(np.mean(b,1))

# #Rzutowanie wymiarów:
# a = np.arange(50)
# #a = a.reshape((10,5))
# a = np.resize(a,(10,5))
# b = np.arange(5)
# b2 = b[:,np.newaxis]
# c = np.arange(4)
# print(b2+c)
# print("ravel zmienia macierz w wektor")
# print("""funkcja newaxis pozwala nam zmienić wymiar macierzy lub wektora o 1 w górę,
# dzięki czemu możemy podnieść wymiar jednego wektora i zsumować go z drugim""")

#Sortowanie danych:
# a = np.random.randint(0,100,[5,5])
# b = -np.sort(-a)
# c = np.sort(a, 0)
# print(c)
# print(b)
#Zadania:
# dtype = [('id',int), ('skrot', 'S2'), ('nazwa', 'S20')]
# b = np.array([(1,'MZ','mazowieckie'),(2,'ZP', 'zachodniopomorskie'), (3,'ML', 'małopolskie')])
# print(b[b[:,1].argsort()])
# print(b[1,2])

# Zadania podsumowujące:
def zad1():
    """
    Utwórz macierz składającą się z pięciu kolumn i 10 wierszy losowo wy-branych liczb całkowitych z zakresu od 0 do 100
    i policz sumę głównej przekątnej tej macierzy, używając funkcji trace a następnie wyświetl wartości używając funkcji diag.
    """
    A = np.random.randint(0,100,(5,10))
    print(A)
    aTrace = np.trace(A)
    print(np.diag(A))

def zad2():
    """
    Utwórz dwie tablice wymiaru 5 × 5 z losowo wybranych liczb dziesiętnych
     z rozkładu normalnego i przemnóż je przez siebie
    """
    A = np.random.normal(size=(5,5))
    B = np.random.normal(size=(5,5))
    print(A*B)

def zad3():
    """
    Utwórz dwie tablice z losowo wybranych liczb całkowitych w zakresie
od 1 do 100. Stwórz z nich macierze o 5 kolumnach i dodaj te macierze
do siebie
    """
    A = np.random.randint(1,100,10)
    B = np.random.randint(1,100,10)
    A = A.reshape(5,2)
    B = B.reshape(5,2)
    print(A+B)

def zad4():
    """
    Stwórz dwie macierzy: jedną o 5 kolumnach i 4 wierszach oraz drugą o
4 kolumnach i 5 wierszach. Dodaj je do siebie używając transformacji
wymiarów za pomocą jednego ze znanych sposobów.
    """
    A = np.random.randint(0,10,(5,4))
    B = np.random.randint(0,10,(4,5))
    A = np.ravel(A)
    B = np.ravel(B)
    print(A+B)

def zad5():
    """
    Pomnóż kolumny 3 i 4, stworzonych przez siebie macierzy.
    """
    A = np.random.randint(0,10,[5,5])
    B = np.random.randint(0,10,[5,5])
    print(A)
    print(B)
    print(A[:,3]*B[:,4])

def zad6():
    """
    Wygeneruj dwie macierze o rozkładzie normalnym (np.random.normal)
i jednostajnym(np.random.uniform).
Policz wartości średnie, odchylenie standardowe, wariancje, sumy, wartości minimalne i maksymalne. Wyniki wyświetl.
    """
    A = np.random.normal(10)
    B = np.random.uniform(10)
    print("A", np.mean(A), np.std(A), np.var(A), np.sum(A), np.min(A), np.max(A))
    print("B", np.mean(B), np.std(B), np.var(B), np.sum(B), np.min(B), np.max(B))

def zad7():
    """
    Wygeneruj dwie macierze kwadratowe a i b (o wymiarach zdecyduj
się samodzielnie), pomnóż je przez siebie używając (a*b) oraz funkcji
dot. zobacz Jaka jest różnica? Napisz kiedy warto wykorzystać funkcję
dot?
    """
    A = np.random.randint(0,10,(4,4))
    B = np.random.randint(0,10,(4,4))
    print(A*B, "mnożenie skalarne")
    print(np.dot(A,B), "mnożenie macierzowe")
    print("* zawsze pomnoży macierze skalarnie, dot przeprowadzi odpowiednie mnożenie macierzowe zależnie od wymiaru macierzy")


def zad8():
    """
     Sprawdź funkcję strides oraz as strided. Zastosuj je do wyboru
danych z macierzy np. 5 kolumn z trzech pierwszych wierszy.
    """
    A = np.random.randint(0,10,(5,5))
    print(A)
    B = np.lib.stride_tricks.as_strided(A,shape=(3,5),strides=(20,4))
    print(B)

def zad9():
    """
    Wygeneruj dwie tablice a i b.
Połącz je z użyciem funkcji vstack i stack. Czym one się różnią?
Zastanów się i napisz, w jakich przypadkach warto je zastosować?
    """
    A = np.random.randint(0,10,(2,2))
    B = np.random.randint(0,10,(2,2))
    C = np.stack((A,B))
    D = np.vstack((A,B))
    print(C, "stack wkłada macierze do macierzy większej o jeden wymiar")
    print(D, "vstack kładzie jedną macierz na drugą nie zwiększając wymiaru macierzy którą tworzy")

def zad10():
    """
     Użyj funkcji strides oraz as strided do obliczenia wartości maksymalnej bloków danych z macierzy (zob. rysunek)
    """
    A = np.arange(24).reshape(4,6)
    B = np.lib.stride_tricks.as_strided(A, shape=(6,2,3), strides=(12,24,4))
    print(B)
    print(np.max(B[0,:]), np.max(B[1,:]), np.max(B[4,:]), np.max(B[5,:]))

zad10()