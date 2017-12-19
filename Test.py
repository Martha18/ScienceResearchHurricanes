from sklearn import tree

IT1 = [-22.5,	1.25, 8.5]
IT2 = [-5, -0.75,	1.75]
IT3 = [-2.5, 0,	6.25]
IT4 = [8.75,	0.5,	-1]
I1 = [2.5,	0,	-1.5]
I2 = [0,	-0.5,	-1]
I3 = [7.5, -1.75,	-1.25]

avchange = [IT1, IT2, IT3, IT4, I1, I2, I3]
cycoccur = [1, 1, 1, 1, 0, 0, 0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(avchange, cycoccur)
chance = clf.predict([[22, 22, 22]])
if chance == [1]:
    print("ERC Positive")
if chance == [0]:
    print("ERC Negative")
