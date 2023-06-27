from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

#Zad 1 - Badanie klasyfikatorów
#1.1
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,
    n_clusters_per_class=2,
    n_redundant=0,
    n_repeated=0,
    random_state=3
)
#1.2
plt.figure()
plt.scatter(X[:,0], X[:,1], c=y)
plt.show()

#1.3
#Lista klasyfikatorów
classifiers = [
    KNeighborsClassifier(),
    QuadraticDiscriminantAnalysis(),
    SVC(probability=True),
    DecisionTreeClassifier(),
    GaussianNB()
]

#Lista nazw klasyfikatorów
clf_labels = [
    "KNeighbors",
    "QDA",
    "SVC(c=1.0)",
    "DecisionTree",
    "GaussianNB"
]

#Słownik średnich do data frame'a
clf_df = {
    'classifier': [],
    'accuracy_score': [],
    'recall_score': [],
    'precision_score': [],
    'f1_score': [],
    'roc_auc': [],
    'train_time': [],
    'test_time': []
}

for clf, label in zip(classifiers,clf_labels):
    # Wyznaczenie liczby podzieleń danych
    dzielenie_danych = 100
    # Przydzielenie list o wielkości podzieleń
    acc = np.zeros(dzielenie_danych)
    rec_sc = np.zeros(dzielenie_danych)
    prec = np.zeros(dzielenie_danych)
    f1 = np.zeros(dzielenie_danych)
    roc = np.zeros(dzielenie_danych)
    train_time = np.zeros(dzielenie_danych)
    test_time = np.zeros(dzielenie_danych)
    for i in range(dzielenie_danych):
        # Dzielenie danych na część uczącą i testującą
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=None, test_size=0.25, shuffle=True,
                                                            random_state=i*2)

        start = time.time()
        clf.fit(X_train, y_train)
        end = time.time()

        train_time[i] = end - start

        start = time.time()
        y_pred = clf.predict(X_test)
        end = time.time()

        # Wpisanie score do odpowiednich list
        test_time[i] = end - start
        acc[i] = accuracy_score(y_test, y_pred)
        rec_sc[i] = recall_score(y_test, y_pred)
        prec[i] = precision_score(y_test, y_pred)
        f1[i] = f1_score(y_test, y_pred)
        roc[i] = roc_auc_score(y_test, y_pred)

    #Dodanie średnich do słowników
    clf_df['classifier'].append(label)
    clf_df['accuracy_score'].append(np.mean(acc))
    clf_df['recall_score'].append(np.mean(rec_sc))
    clf_df['precision_score'].append(np.mean(prec))
    clf_df['f1_score'].append(np.mean(f1))
    clf_df['roc_auc'].append(np.mean(roc))
    clf_df['train_time'].append(np.mean(train_time))
    clf_df['test_time'].append(np.mean(test_time))

    #Wykresy błędów klasyfikacji
    fig ,axs = plt.subplots(1, 3, figsize=(12,6))
    fig.suptitle(label)
    axs[0].set_title("oczekiwane")
    axs[0].scatter(X_test[:,0],X_test[:,1], c=y_test, s=9)
    axs[1].set_title("obliczone")
    axs[1].scatter(X_test[:,0], X_test[:,1], c=y_pred, s=9)
    colours = np.empty(len(y_test), dtype=str)
    #Wyznaczenie kolorów dla błędów
    for i in range(len(y_test)):
        if(y_test[i] != y_pred[i]):
            colours[i] = 'r'
        else:
            colours[i] = 'g'

    axs[2].set_title("różnice")
    axs[2].scatter(X_test[:,0], X_test[:,1], c=colours, s=9)
    plt.show()

    #Wykres krzywej ROC
    prob = clf.predict_proba(X_test)[::,1]
    fpr, tpr, thresholds = roc_curve(y_test, prob)
    auc = roc_auc_score(y_test, prob)
    plt.title('ROC Curve of '+label)
    plt.plot(fpr, tpr, label='auc = '+str(auc))
    plt.plot(fpr, fpr, '--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()
    plt.show()

    x_min, x_max = X_test[:,0].min() - 1, X_test[:,0].max() + 1
    y_min, y_max = X_test[:,1].min() - 1, X_test[:,1].max() + 1
    xx,yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    #Wykres krzywej dyskryminacyjnej
    plt.contourf(xx,yy,Z,alpha=0.2)
    plt.title("Krzywa dyskryminacyjna "+label)
    plt.scatter(X_test[:,0], X_test[:,1], c=y_test, s=20, alpha=0.8)

#Stworzenie data frame ze słownika
classifiers_df = pd.DataFrame.from_dict(clf_df)
print(classifiers_df.to_string())
#Stworzenie wykresu wyników z data frame
x = np.arange(len(classifiers_df.columns)-1)
x_labels = list(classifiers_df.columns)
x_labels.pop(0)

fig, ax = plt.subplots()

pos = 0.0

for i, clf in enumerate(classifiers_df['classifier']):
    tmp = list(classifiers_df.loc[i, classifiers_df.columns != 'classifier'])

    tmp[-1] = tmp[-1]*100.0
    tmp[-2] = tmp[-2]*100.0
    ax.bar(x+pos, tmp, 0.1, label=clf)
    pos += 0.1

plt.xticks(rotation=90)
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()
plt.show()
fig.tight_layout()


#Zadanie 2 - badanie parametrów wybranego klasyfikatora
#2.1
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,
    n_clusters_per_class=2,
    n_redundant=0,
    n_repeated=0,
    random_state=3
)

#2.2
klasyfikator = KNeighborsClassifier()
X_train, X_test, y_train, y_test = train_test_split(X,y)

#2.3
n_range = np.arange(1,20)
p_range = np.arange(2,5)

clf_params = { "KNeighborsClassifier": { "n_neighbors": n_range,
                                         "p": p_range}}

#2.4
acc_scorer = make_scorer(accuracy_score)

grid = GridSearchCV(klasyfikator,
                    clf_params["KNeighborsClassifier"],
                    cv=10,
                    scoring={'Accuracy': acc_scorer},
                    refit='Accuracy')

grid.fit(X_train, y_train)
optimal_params = grid.best_params_

#2.5
n_scores = []

for n in n_range:
    knn = KNeighborsClassifier(n_neighbors=n, p=optimal_params['p'])
    cv_scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    n_scores.append(cv_scores.mean())

plt.plot(n_range, n_scores)
plt.xlabel("parametry")
plt.ylabel("accuracy")
plt.title('KNeighborsClassifier')
plt.tight_layout()
plt.show()

#2.6
# Wyznaczenie liczby podzieleń danych
dzielenie_danych = 100
# Przydzielenie list o wielkości podzieleń
acc = np.zeros(dzielenie_danych)
rec_sc = np.zeros(dzielenie_danych)
prec = np.zeros(dzielenie_danych)
f1 = np.zeros(dzielenie_danych)
roc = np.zeros(dzielenie_danych)
train_time = np.zeros(dzielenie_danych)
test_time = np.zeros(dzielenie_danych)
for i in range(dzielenie_danych):
    # Dzielenie danych na część uczącą i testującą
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=None, test_size=0.25, shuffle=True,
                                                        random_state=i*2)

    start = time.time()
    klasyfikator.fit(X_train, y_train)
    end = time.time()

    train_time[i] = end - start

    start = time.time()
    y_pred = klasyfikator.predict(X_test)
    end = time.time()

    # Wpisanie score do odpowiednich list
    #2.7
    test_time[i] = end - start
    acc[i] = accuracy_score(y_test, y_pred)
    rec_sc[i] = recall_score(y_test, y_pred)
    prec[i] = precision_score(y_test, y_pred)
    f1[i] = f1_score(y_test, y_pred)
    roc[i] = roc_auc_score(y_test, y_pred)

#2.8
#Słownik średnich do data frame'a
clf_df = {
    'classifier': [],
    'accuracy_score': [],
    'recall_score': [],
    'precision_score': [],
    'f1_score': [],
    'roc_auc': [],
    'train_time': [],
    'test_time': []
}

#Dodanie średnich do słowników
clf_df['classifier'].append('KNeighborsClassifier')
clf_df['accuracy_score'].append(np.mean(acc))
clf_df['recall_score'].append(np.mean(rec_sc))
clf_df['precision_score'].append(np.mean(prec))
clf_df['f1_score'].append(np.mean(f1))
clf_df['roc_auc'].append(np.mean(roc))
clf_df['train_time'].append(np.mean(train_time))
clf_df['test_time'].append(np.mean(test_time))

#2.9
#Wykres krzywej ROC
prob = klasyfikator.predict_proba(X_test)[::,1]
fpr, tpr, thresholds = roc_curve(y_test, prob)
auc = roc_auc_score(y_test, prob)
plt.title('ROC Curve of KNeighborsClassifier')
plt.plot(fpr, tpr, label='auc = '+str(auc))
plt.plot(fpr, fpr, '--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()
