import matplotlib
import random
import pandas
import sklearn

from sklearn import preprocessing
from sklearn import ensemble
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

df = pandas.read_csv('car.data', header=0)
df.info()

df = df.replace('vhigh', 4)
df = df.replace('high', 3)

car = df.values

X, y = car[:, :6], car[:, 6]

X, y = X.astype(int), y.astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3,)
clf = ensemble.RandomForestClassifier(n_estimators=500)

clf.fit(X_train, y_train)
RandomForestClassifier(bootstrap=True,
                       criterion='gini', max_depth=None, max_features='auto',
                       max_leaf_nodes=None,  min_samples_leaf=1,
                       min_samples_split=2, n_estimators=500, n_jobs=1,
                       oob_score=False, random_state=None, verbose=0)
clf.score(X_test, y_test)

scaler = preprocessing.MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

clf.fit(X_train_scaled, y_train)
clf.score(X_test_scaled, y_test)


y_pred = clf.predict(X_test)
