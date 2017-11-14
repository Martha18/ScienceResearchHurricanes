from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
# import pandas
import numpy as np
np.random.seed(0)

iris = load_iris()
df =pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()

df['species'] = pd.Categorical.form_codes(iris.target, iris.target_names)
df.head()

df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df.head()

train, test = df[df['is_train']==True], df[]