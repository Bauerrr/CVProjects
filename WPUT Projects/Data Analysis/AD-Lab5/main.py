import pandas as pd
import numpy as np

import scipy.sparse as sp

file = pd.read_csv('zoo.csv')
#print(file)

#zadanie 1
def freq(x , prob=True):
    if sp.issparse(x):
        x = pd.DataFrame.sparse.from_spmatrix(x)
    else:
        x = pd.DataFrame(x)
    if prob:
        xi = np.unique(x)
        pi = x.groupby(x.columns[0]).size().div(len(x))
    else:
        xi = np.unique(x)
        pi = x.groupby(x.columns[0]).size()
    return xi, pi


#zad1 = freq(file['type'],False)


#zadanie 2
def freq2(x, y, prob=True):
    if sp.issparse(x):
        x = pd.DataFrame.sparse.from_spmatrix(x)
    else:
        x = pd.DataFrame(x)
    if sp.issparse(y):
        y = pd.DataFrame.sparse.from_spmatrix(y)
    else:
        y = pd.DataFrame(y)
    xi = np.unique(x)
    yi = np.unique(y)
    xy = pd.DataFrame(np.column_stack((x,y)))
    pi = xy.value_counts(normalize=prob)
    return xi, pi, yi



#zadanie 3
def entropy(x):
    x = freq(x)
    en = 0
    for i in range(len(x[1])):
        en += x[1][i] * np.log2(x[1][i])
    return -en


def entropy2(x,y):
    xy = freq2(x,y)
    en = 0
    for i in range(len(xy[1])):
        en += xy[1][i] * np.log2(xy[1][i])
    return -en


def infogain(x,y):
    return entropy(x)+entropy(y)-entropy2(x,y)


#zadanie 4
zad1 = freq(file['legs'],False)
#print(type(file['legs']))
#print(type(bsr_array(file['legs'])))
print(zad1)
# zad2 = freq2(bsr_array(file['type']), bsr_array(file['eggs']), True)
# print(zad2)
print(entropy(file['type']))
print(entropy2(file['type'], file['eggs']))
print(infogain(file['type'], file['eggs']))