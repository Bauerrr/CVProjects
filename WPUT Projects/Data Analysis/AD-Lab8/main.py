import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.1
def distp(X,C):
    #Odległość Euklidesowa
    return np.sqrt(np.sum((X-C)**2,axis=1))

def distm(X,C):
    #Macierz kowariancji
    V = np.cov(X.T)
    #Odległość Mahalanobisa
    return np.sqrt(np.sum(((X-C)**2)*(1/V),axis=1))

def ksrodki(X,k):
    #Losowa inicjalizacja wektorów
    C = X[np.random.choice(X.shape[0],k,replace=False)]
    #Zmienne pomocnicze
    C_h = np.zeros(C.shape)
    #Macierz sąsiadów
    CX = np.zeros(X.shape[0])
    while np.sum((C-C_h)**2) != 0:
        C_h = C
        #Przydzielenie obiektów do klastrów
        for i in range(X.shape[0]):
            dist = distm(X[i],C)
            CX[i] = np.argmin(dist)
        #Obliczenie nowych wektorów
        for i in range(k):
            C[i] = np.mean(X[CX==i],axis=0)
    return CX,C

#2.2
df = pd.read_csv('autos.csv')
df = df.iloc[:, 1:]
df['body-style'] = pd.Categorical(df["body-style"])
df['body-style'] = df['body-style'].cat.codes
data = df[['length', 'height', 'curb-weight', 'engine-size', 'wheel-base']]
data = data.values[:, 0:5]

C, CX = ksrodki(data,3)

#2.3
plt.cla()
plt.plot(data[C==0,0],data[C==0,1], '.r',
         data[C==1,0],data[C==1,1], '.g',
         data[C==2,0],data[C==2,1], '.b')

plt.plot(CX[:,0],CX[:,1],'.k', markersize=10)
plt.draw()
plt.show()

