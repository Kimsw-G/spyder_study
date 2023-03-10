import pandas as pd
wine = pd.read_csv('https://bit.ly/wine_csv_data')

data = wine[['alcohol','sugar','pH']].to_numpy()
target = wine['class'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = \
    train_test_split(data,target,test_size=0.2,random_state=42)
    
sub_input, val_input, sub_target, val_target = \
    train_test_split(train_input,train_target,test_size=0.2,random_state=42)
    
def print_score(model,TEXT):
    print(f"###### {TEXT} #####")
    print(model.score(sub_input, sub_target))
    print(model.score(val_input, val_target))
    

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)
print_score(dt,"dt")

import numpy as np
from sklearn.model_selection import cross_validate
scores = cross_validate(dt, train_input, train_target)
print(scores)
print(np.mean(scores['test_score']))

from sklearn.model_selection import StratifiedKFold
scores = cross_validate(dt, train_input, train_target, cv=StratifiedKFold())
print(scores)
print(np.mean(scores['test_score']))

splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(scores)
print(np.mean(scores['test_score']))
