from sklearn import datasets
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

def wiPCA(x, n_components=1, variance_ratio=False):
    v_r = 0
    #Odjęcie średniej od x w celu łatwiejszej kalkulacji kowariancji
    x_m = x - np.mean(x, axis=0)

    #Obliczenie macierzy kowariancji dla x_m
    cov_mat = np.cov(x_m, rowvar=False)

    #Obliczanie wektorów i wartości własnych
    e_val,e_vec = np.linalg.eigh(cov_mat)

    if variance_ratio == True:
        s_index = np.argsort(e_val)[::-1]
        s_e_val = e_val[s_index]
        v_r = np.cumsum(s_e_val/s_e_val.sum())

    if n_components == 1:
        v = e_vec[:,np.argmax(e_val)]
        tr = np.dot(x,v)
        x_r = np.outer(tr,v)
    else:
        #Sortowanie wartości własnych malejąco
        s_index = np.argsort(e_val)[::-1]
        s_e_val = e_val[s_index]

        #Sortowanie wektorów własnych
        s_e_vec = e_vec[:,s_index]

        #Wybranie odpowiedniej ilości wektorów własnych
        #Ilość wektorów to wybrany wymiar
        e_vec_subset = s_e_vec[:,0:n_components]
        #Końcowa transformacja danych do wybranego wymiaru
        x_r = np.dot(e_vec_subset.transpose(), x_m.transpose()).transpose()
    return x_r, v_r


def wiPCAreconstruction(x_r, ogDataset, nComp):
    x_m = ogDataset - np.mean(ogDataset, axis=0)
    cov_mat = np.cov(x_m, rowvar=False)
    e_val, e_vec = np.linalg.eigh(cov_mat)
    pca_rec = np.dot(x_r[:,:nComp],e_vec.T[:nComp,:])
    pca_rec += np.mean(ogDataset, axis=0)
    return pca_rec, e_val



#Zad 1
#a
a = np.random.RandomState(0)
dots = a.randn(200, 2)
dots2 = np.dot(dots,a.rand(2,2))
#b
plt.figure()
plt.scatter(dots2[:,0],dots2[:,1], c='r')
#c
dots2_r = wiPCA(dots2, 1)[0]
plt.scatter(dots2_r[:,0],dots2_r[:,1], c='g')
plt.show()

#Zad2
#a
iris = datasets.load_iris()
X,y = iris['data'], iris['target']
#b
iris_r = wiPCA(X,2)[0]
#Bez PCA
# plt.figure()
# plt.scatter(X[:,0],X[:,1], c=y)
# plt.show()
#Z PCA
#c
plt.figure()
plt.scatter(iris_r[:,0], iris_r[:,1], c=y)
plt.show()

#Zad 3
#a
digits = datasets.load_digits()
a, b = digits['data'], digits['target']
#b
digits_r, digits_var = wiPCA(a,2, True)
#c
plt.figure()
plt.plot(digits_var)
plt.show()
#d
plt.figure()
plt.scatter(digits_r[:,0],digits_r[:,1],c=b)
plt.show()
#e
digits_rec, e_val = wiPCAreconstruction(digits_r, a, 2)
plt.figure()
plt.scatter(digits_rec[:,0], digits_rec[:,1], c=b)
plt.show()
e_dif = []
for i in range(len(digits_rec)):
    e_dif.append(a[i,0] - digits_rec[i,0])

plt.figure()
plt.plot(e_dif)
plt.show()