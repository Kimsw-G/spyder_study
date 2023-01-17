import numpy as np
import pandas as pd
wine = pd.read_csv('https://bit.ly/wine_csv_data')

data = wine[['alcohol','sugar','pH']].to_numpy()
target = wine['class'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = \
    train_test_split(data,target,test_size=0.2,random_state=42)
    
from sklearn.model_selection import cross_validate
from sklearn.ensemble import GradientBoostingClassifier
gb = GradientBoostingClassifier(random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']),np.mean(scores['test_score']))

#
gb = GradientBoostingClassifier(n_estimators=500, learning_rate=0.2,random_state=42)
scores = cross_validate(gb, train_input, train_target, return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']),np.mean(scores['test_score']))
gb.fit(train_input, train_target)
print(gb.feature_importances_)