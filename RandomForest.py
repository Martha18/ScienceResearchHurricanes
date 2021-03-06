from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
# import pandas
import numpy as np
np.random.seed(0)

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df.head())

df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
print(df.head())

df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
print(df.head())

train, test = df[df['is_train'] == True], df[df['is_train'] == False]

print('Number of observations in the training data:', len(train))
print('Number of observations in the test data:', len(test))

features = df.columns[:4]
print(features)

y = pd.factorize(train['species'])[0]
print(y)

clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features], y)
print(clf.fit(train[features], y))

clf.predict(test[features])
print(clf.predict(test[features]))

print(clf.predict_proba(test[features])[0:10])

preds = iris.target_names[clf.predict(test[features])]
print(preds[0:5])

print(test['species'].head())

pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predict Species'])
print(pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predict Species']))

list(zip(train[features], clf.feature_importances_))
print(list(zip(train[features], clf.feature_importances_)))
