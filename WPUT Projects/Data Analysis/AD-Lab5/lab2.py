import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Manipulowanie danymi
#zad1
# a1 = pd.date_range(start='2020-03-01', end='2020-03-05')
# a2 = np.random.uniform(0,1,15).reshape(5,3)
# A = pd.DataFrame(data=a2,index=a1, columns=['A','B','C'])
# print(A)
#zad2
# id = np.arange(0,20)
# tab = pd.DataFrame(np.random.randint(0,10,60).reshape(20,3),index=id, columns=['A','B','C'])
# print(tab[0:3], tab[-3:], tab.index.name, tab.columns, tab.to_string(index=False, header=None), sep='\n')
# print(tab.sample(5), tab['A'], tab.loc[:,['A','B']], sep='\n')
# print(tab.iloc[[0,1,2],[0,1]])
# print(tab.iloc[[5]])
# print(tab.iloc[[0,5,6,7],[1,2]])
#zad3
# print(tab[tab>0])
# print(tab.mask(tab>0))
# print(tab[tab>0].loc[:,'A'])
# print(tab.mean(0))
# print(tab.mean(1))
#zad4
# a = pd.DataFrame([[0,1],[2,3]])
# b = pd.DataFrame([[4,5],[6,7]])
# c = pd.concat((a,b))
# c = c.transpose()
# print(c)

#Sortowanie
# df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": ['a', 'b', 'a','b', 'b']}, index=np.arange(5))
# df.index.name='id'
# print(df.sort_values('id',ascending=False))
# print(df.sort_values('y'))

#Grupowanie danych
# slownik = {'Day':['Mon','Tue','Mon','Tue','Mon'],'Fruit':['Apple','Apple','Banana','Banana','Apple'], 'Pound':[10,15,50,40,5], 'Profit':[20,30,25,20,10]}
# df3 = pd.DataFrame(slownik)
# print(df3)
# print(df3.groupby('Day').sum())
# print(df3.groupby(['Day','Fruit']).sum())

#Wypełnianie danych
# df=pd.DataFrame(np.random.randn(20, 3), index=np.arange(20), columns=['A','B','C'])
# df.index.name='id'
# print(df)
# df['B']=1
# print("Przypisuje kolumnie B jedynki")
# df.iloc[1,2]=10
# print("Przypisuje pierwszemu indeksowi w trzeciej kolumnie liczbę 10")
# df[df<0]=-df
# print("Każdą wartość ujemną zmienia na dodatnią")

#Uzupełnianie danych
# df=pd.DataFrame(np.random.randn(20, 3), index=np.arange(20), columns=['A','B','C'])
# df.index.name='id'
# df.iloc[[0,3],1]=np.nan
# print("Dla wartości 1 w wierszach 0 , 3 zmienia ją na nan")
# df.fillna(0, inplace=True)
# print("Zmienia miejsca w których jest NaN na 0")
# df.iloc[[0,3],1]=np.nan
# df=df.replace(to_replace=np.nan,value=-9999)
# print("Zmienia wybraną wartość na inną wybraną wartość")
# df.iloc[[0,3],1]=np.nan
# print(pd.isnull(df))
# print("Wyświetla True w miejscach w których brakuje wartości")

df = pd.DataFrame({'x':[1,2,3,4,5], 'y':['a','b','a','b','b']})

def zad1(df : pd.DataFrame):
    """
    Zgrupować tabele po zmiennej symbolicznej Y, a następnie wyznaczyć
     średnią wartość atrybutu numerycznego X w grupach wyznaczonych przez Y.
    """
    print(df.groupby('y').mean())

def zad2(df : pd.DataFrame):
    """
     Wyznaczyć rozkład liczności atrybutów (value counts).
    """
    print(df.value_counts())
    #print(df.groupby('y').value_counts())

def zad3():
    """
    Wyczytać dane autos.csv, za pomocą polecenia np.loadtxt
    oraz pandas.read csv. Sprawdź różnice.
    """
    lt = np.loadtxt('autos.csv', dtype="str", delimiter=",")
    rc = pd.read_csv('autos.csv')
    print(lt)
    print(rc)
    print("różnica polega na tym że pandas ładniej się wypisuje")

def zad4():
    """
    Zgrupować ramkę danych po zmiennej ’make’ a następnie wyznaczyć
    średnie zużycie paliwa dla każdego z producentów.
    """
    rc = pd.read_csv('autos.csv')
    grouped = rc.groupby(['make']).mean()[['city-mpg','highway-mpg']]
    print(grouped)

def zad5():
    """
    Zgrupować ramkę danych po zmiennej ’make’ liczności
    dla atrybutu ’fuel-type’.
    """
    rc = pd.read_csv('autos.csv')
    grouped = rc.value_counts(['make','fuel-type'])
    print(grouped)

def zad6():
    """
    Dopasować wielomian 1 i 2 stopnia prognozujący wartość zmiennej ’city-mpg’,
    względem ’length’ (np.polyfit , np.polyval).
    """
    rc = pd.read_csv('autos.csv')
    linLength = np.linspace(rc['length'].min(), rc['length'].max(), len(rc['length']))
    w1 = np.polyfit(rc['length'],rc['city-mpg'], 1)
    pol1 = np.polyval(w1,linLength)
    w2 = np.polyfit(rc['length'],rc['city-mpg'], 2)
    pol2 = np.polyval(w2,linLength)
    print(w1)
    print(w2)
    print(pol1)
    print(pol2)

def zad7():
    """
    Wyznaczyć współczynnik korelacji liniowej pomiędzy tymi zmiennymi (scipy.stats).
    """
    rc = pd.read_csv('autos.csv')
    print(stats.spearmanr(rc['city-mpg'],rc['length']))
    #print(stats.pearsonr(rc['city-mpg'],rc['length'])) #oba wykazują podobną korelację

def zad8():
    """
    Zwizualizować wyniki dopasowania, zaznaczając próbki oraz dopasowane krzywe
    na tle próbek dla zmiennych ’city-mpg’, ’length’.
    """
    rc = pd.read_csv('autos.csv')
    linLength = np.linspace(rc['length'].min(), rc['length'].max(), len(rc['length']))

    w1 = np.polyfit(rc['length'],rc['city-mpg'], 1)
    pol1 = np.polyval(w1,linLength)

    w2 = np.polyfit(rc['length'],rc['city-mpg'], 2)
    pol2 = np.polyval(w2,linLength)

    plt.plot(rc['length'], rc['city-mpg'], '.')
    plt.plot(linLength, pol1, label='Aproksymacja 1 stopnia')
    plt.plot(linLength, pol2, label='Aproksymacja 2 stopnia')
    plt.legend()
    plt.show()

def zad9():
    """
    Dla zmiennej ’length’ utworzyć jednowymiarowy estymator funkcji gęstości,
    w tym celu użyć scipy.stats.gaussian kde.
    Zwizualizować wynik przedstawiając jednocześnie próbki i funkcję gęstości.
    Do wykresu dodać legendę. W tym celu użyć (plot(...,label=’...’), legend)
    """
    rc = pd.read_csv('autos.csv')
    linLength = np.linspace(rc['length'].min(), rc['length'].max(), len(rc['length']))
    gkde = stats.gaussian_kde(rc['length'])

    #plt.plot(rc['length'],'.', label='Próbki') #dodanie próbek skutkuje wypłaszczzeniem funkcji gęstości
    plt.plot(gkde(linLength), label='Funkcja gęstości')
    plt.legend()
    plt.show()

def zad10():
    """
    Utworzyć w jednym oknie graficznym dwa wykresy
    ax=subplot(...), ax.plot(...)
    Na drugim wykresie przedstawić analogicznie rozkład dla zmiennej ’width’.
    """
    rc = pd.read_csv('autos.csv')
    fig, ax = plt.subplots(2,1)
    wLength = np.linspace(rc['width'].min(), rc['width'].max(), len(rc['width']))
    gwidth = stats.gaussian_kde(rc['width'])
    ax[1].plot(gwidth(wLength))
    plt.show()

def zad11():
    rc = pd.read_csv('autos.csv')
    xmax = rc['length'].max()
    xmin = rc['length'].min()
    ymax = rc['width'].max()
    ymin = rc['width'].min()


    x,y = np.meshgrid(np.arange(xmin,xmax), np.arange(ymin,ymax))
    pos = np.vstack([x.ravel(),y.ravel()])
    val = np.vstack([rc['length'],rc['width']])
    kernel = stats.gaussian_kde(val)
    z = np.reshape(kernel(pos).T,x.shape)

    ax = plt.contour(x,y,z,cmap='jet')
    plt.plot(rc['length'], rc['width'], '|k', label='Próbki')
    plt.colorbar(ax)
    plt.legend()
    plt.savefig('zadanie11.png')
    plt.savefig('zadanie11.pdf')
    plt.show()

zad11()






