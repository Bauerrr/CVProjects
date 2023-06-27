import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy.stats import mode
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import LeaveOneOut
from sklearn.neighbors import KDTree
import time


def eucledian(p1,p2):
    #funkcja wylicza odległość między dwoma punktami
    dist = np.sqrt(np.sum((p1-p2)**2))
    return dist

class KNN:
    def __init__(self, n_neighbors=1, useKDTree=False):
        self.n_neighbors = n_neighbors
        self.useKDTree = useKDTree

    def fit(self,X,y):
        self.X_train = X
        self.y_train = y

    def predict(self,X):
        if self.useKDTree == False:
            self.X_test = X
            op_labels = []
            for i in self.X_test:
                #lista dystansów
                p_dist = []
                for j in range(len(self.X_train)):
                    distances = eucledian(np.array(self.X_train[j,:]),i)
                    #print(distances)
                    #Obliczanie odległości i dodawanie do listy
                    p_dist.append(distances)
                p_dist = np.array(p_dist)
                #sortowanie i zachowanie wybranej ilosci sasiadow
                dist = np.argsort(p_dist)[:self.n_neighbors]
                labels = self.y_train[dist]
                #Wybranie najczęściej występującej klasy
                lab = mode(labels)
                lab = lab.mode[0]
                op_labels.append(lab)
            return op_labels
        else:
            self.X_test = X
            op_labels = []
            tree = KDTree(self.X_train)
            for i in range(len(self.X_test)):
                #Znalezienie najbliższych dystansów do wybranych k sąsiadów
                dist, ind = tree.query(np.array(self.X_test[i,:]).reshape(1,-1), k = self.n_neighbors)
                labels = self.y_train[ind]
                lab = mode(labels[0,:])
                lab = lab.mode[0]
                op_labels.append(lab)
            return op_labels




    def score(self,X,y):
        #Obliczanie za pomocą MSE
        return mean_squared_error(X,y)

#3.1
X, y = datasets.make_classification(n_samples=100,n_features=2,n_informative=2,n_redundant=0,n_repeated=0,random_state=3)

#3.2
knn1 = KNN()
knn1.fit(X,y)

#3.3
#Wartości maksymalne dla danych wymiarów
x_min, x_max = X[:,0].min() -1, X[:,0].max()+1
y_min, y_max = X[:,1].min() -1, X[:,1].max()+1
#Krok dla arange
h = 0.02
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
#Wrzucenie do predicta połączonych w macierz wektorów xx i yy
Z = knn1.predict(np.c_[xx.ravel(),yy.ravel()])
Z = np.reshape(Z,xx.shape)
#Wyświetlenie punktów
plt.scatter(X[:,0], X[:,1], c=y)
#Wyświetlenie konturu dla klas
plt.contour(xx, yy, Z)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.show()

#3.4
iris = datasets.load_iris()
X = iris['data']
y = iris['target']
knn2 = KNN()
knn2.fit(X, y)

#3.5
pca = PCA(n_components=2)
X_r = pca.fit_transform(X)
#3.5a
x_min, x_max = X_r[:,0].min() -1, X_r[:,0].max()+1
y_min, y_max = X_r[:,1].min() -1, X_r[:,1].max()+1

h = 0.02
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
#3.5b
X_o = pca.inverse_transform(np.c_[xx.ravel(),yy.ravel()])
#3.5c
Z = knn2.predict(X_o)
Z = np.reshape(Z,xx.shape)
plt.scatter(X_r[:,0], X_r[:,1], c=y)
plt.contour(xx, yy, Z)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.show()

#3.6
loo = LeaveOneOut()
#Ilość testów dla k
for j in range(1,15):
    i = 0
    knn3 = KNN(j)
    sum_mse = 0
    for train_index, test_index in loo.split(X):
        #rozłożenie wszystkiego na próbki testowe i próbki treningowe za pomocą leave one out
        x_tr, x_te = X[train_index], X[test_index]
        y_tr, y_te = y[train_index], y[test_index]
        knn3.fit(x_tr, y_tr)
        y_pred = knn3.predict(x_te)
        sum_mse += knn3.score(y_te, y_pred)
        i += 1
    #mse dla danego k
    mse_fin = (1/i)*sum_mse
    print("k =",j,"MSE =",mse_fin)

#3.7

knn = KNN(useKDTree=True)
knn.fit(X,y)
dt1 = time.time()
drzewa = knn.predict(X_o)
dt2 = time.time()
print("Czas dla KD-Drzew:", dt2-dt1)
knn2 = KNN()
knn2.fit(X,y)
dnt1 = time.time()
nie_drzewa = knn2.predict(X_o)
dnt2 = time.time()
print("Czas bez KD-Drzew:", dnt2-dnt1)


