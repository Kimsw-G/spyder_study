import numpy as np
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
from sklearn.model_selection import GridSearchCV
params = {'min_impurity_decrease':[0.0001,0.0002,0.0003,0.0004,0.0005]}
gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)
gs.fit(train_input, train_target)

dt = gs.best_estimator_
print(dt.score(train_input, train_target))
print(gs.best_params_)
print(gs.cv_results_['mean_test_score'])
best_index = np.argmax(gs.cv_results_['mean_test_score'])
print(gs.cv_results_['params'][best_index])

params = {'min_impurity_decrease':[0.0001,0.0002,0.0003,0.0004,0.0005],
          'max_depth': range(5,20,1),
          'min_samples_split': range(2,100,10)}
gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)
gs.fit(train_input, train_target)

print(gs.best_params_)
print(np.max(gs.cv_results_['mean_test_score']))
