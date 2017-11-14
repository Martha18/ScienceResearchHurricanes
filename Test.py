from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
fruit = clf.predict([[145, 1]])
if fruit == [1]:
    print("orange")
if fruit == [0]:
    print("apple")