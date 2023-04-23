import sys

sys.path.append(
    "/Users/phoenix_20/Desktop/My Folder /Coding Stuff/ML /PyMLalgo/PyMLAlgos"
)
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


from Algorithm.RandomForest import RandomForest


def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy


data = datasets.load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

clf = RandomForest(n_trees=6, max_depth=5, n_feats=3)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
acc = accuracy(y_test, y_pred)


print("Accuracy:", acc)