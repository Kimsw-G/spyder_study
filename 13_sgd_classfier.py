import pandas as pd
fish = pd.read_csv('https://bit.ly/fish_csv_data')

# 특성
fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
# 샘플
fish_target = fish['Species'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = \
    train_test_split(fish_input, fish_target, random_state=42)
    
def print_score(model,TEXT):
    print(f"###### {TEXT} #####")
    print(model.score(train_scaled, train_target))
    print(model.score(test_scaled, test_target))
    

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.linear_model import SGDClassifier
sc = SGDClassifier(loss='log_loss',max_iter=11,tol=None,random_state=42)
sc.fit(train_scaled,train_target)
print_score("iter=10")


sc.partial_fit(train_scaled, train_target)
print_score("partial_once")

import numpy as np
sc = SGDClassifier(loss='log_loss', random_state=42)
train_score = []
test_score = []
classes = np.unique(train_target)

for _ in range(0,300):
    sc.partial_fit(train_scaled, train_target, classes=classes)
    train_score.append(sc.score(train_scaled, train_target))
    test_score.append(sc.score(test_scaled, test_target))
    
import matplotlib.pyplot as plt
plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()