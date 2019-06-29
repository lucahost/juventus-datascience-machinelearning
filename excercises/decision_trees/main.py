import math
import matplotlib
import random
import pandas

from sklearn import preprocessing


df = pandas.read_csv('csv.data', header=0)
df.info()


df = df.replace('vhigh', 4)
df = df.replace('high', 3)


car = df.values

X, y = car[:, :6], car[:, 6]

X, y = X.astype(int), y.astype(int)


X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    X, y, test_size=0.3, random_state=0)
clf = ensemble.RandomForestClassifier(n_estimators=500)

clf.fit(X_train, y_train)
RandomForestClassifier(bootstrap=True, compute_importances=None,
                       criterion='gini', max_depth=None, max_features='auto',
                       max_leaf_nodes=None, min_density=None, min_samples_leaf=1,
                       min_samples_split=2, n_estimators=500, n_jobs=1,
                       oob_score=False, random_state=None, verbose=0)
clf.score(X_test, y_test)

scaler = preprocessing.MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

clf.fit(X_train_scaled, y_train)
clf.score(X_test_scaled, y_test)


y_pred = clf.predict(X_test)
