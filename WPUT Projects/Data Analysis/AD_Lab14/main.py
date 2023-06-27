import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from sklearn import preprocessing
import scipy
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
from itertools import cycle


#Zad 1
X , y = make_classification(
    n_samples=1600,
    n_classes=4,
    n_clusters_per_class=1,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    random_state=15
)
plt.figure()
plt.scatter(X[:,0], X[:,1], c=y)
plt.show()

#Zad 2
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5)

#Zad 3
classifiers = [
    ('OvOSVC_linear', OneVsOneClassifier(svm.SVC(kernel='linear', probability=True))),
    ('OvRSVC_linear', OneVsRestClassifier(svm.SVC(kernel='linear', probability=True))),
    ('OvOSVC_rbf', OneVsOneClassifier(svm.SVC(kernel='rbf', probability=True))),
    ('OvRSVC_rbf', OneVsRestClassifier(svm.SVC(kernel='rbf', probability=True))),
    ('OvOLogisticRegression', OneVsOneClassifier(LogisticRegression())),
    ('OvRLogisticRegression', OneVsRestClassifier(LogisticRegression())),
    ('OvOPerceptron', OneVsOneClassifier(Perceptron())),
    ('OvRPerceptron', OneVsRestClassifier(Perceptron()))
]

#Zad 4

#Słownik średnich do data frame'a
clf_df = {
    'classifier': [],
    'accuracy_score': [],
    'recall_score': [],
    'precision_score': [],
    'f1_score': [],
    'roc_auc': [],
}

for label, clf in classifiers:

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    #Dodanie średnich do słowników
    clf_df['classifier'].append(label)
    clf_df['accuracy_score'].append(accuracy_score(y_test, y_pred))
    clf_df['recall_score'].append(recall_score(y_test, y_pred, average='macro'))
    clf_df['precision_score'].append(precision_score(y_test, y_pred, average='macro'))
    clf_df['f1_score'].append(f1_score(y_test, y_pred, average='macro'))

    y_pred2=preprocessing.label_binarize(y_pred,classes=[0,1,2,3])
    multi_class = label[0:3].lower()
    clf_df['roc_auc'].append(roc_auc_score(y_test, y_pred2, multi_class=multi_class, average='macro'))

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


    # #Wykres krzywej ROC
    # if label[0:3]=='OvR':
    #     prob = clf.predict_proba(X_test)[::,1]
    #     fpr, tpr, thresholds = roc_curve(y_test, prob)
    #     auc = roc_auc_score(y_test, y_pred)
    #     plt.title('ROC Curve of '+label)
    #     plt.plot(fpr, tpr, label='auc = '+str(auc))
    #     plt.plot(fpr, fpr, '--')
    #     plt.xlabel("False Positive Rate")
    #     plt.ylabel("True Positive Rate")
    #     plt.legend()
    #     plt.show()

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

    # tmp[-1] = tmp[-1]*100.0
    # tmp[-2] = tmp[-2]*100.0
    ax.bar(x+pos, tmp, 0.1, label=clf)
    pos += 0.1

plt.xticks(rotation=90)
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()
plt.show()
fig.tight_layout()
