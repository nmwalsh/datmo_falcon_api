# data handling
import os
import sys
import json
import pickle
import pandas as pd
import random
import collections
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
random.seed(3)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

# measures
from sklearn.metrics import accuracy_score
import timeit

# CONFIGURATIONS / PARAMETERS to SWEEP

config_dict = {
	"data": {
		"shuffle": True,
		"train_split": 0.65,
		"test_split": 0.35
	},
	"model": {
		"function": "RandomForestClassifier",
		"RandomForestClassifier": {
			"max_depth": 9,
			"n_estimators": 7,
			"max_features": 2
		}
	}
}

# DATA PREPROCESSING

# read the csv file
print("Loading data")
iris = pd.read_csv('Iris.csv', index_col='Id')

# get X,y data
X = iris.as_matrix(iris.columns[0:-1])

lenc = LabelEncoder()
y = iris['Species'].as_matrix()
y = lenc.fit_transform(y)

# shuffle and split into train and test sets
print("Splitting data into train and test set")
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=config_dict['data']['shuffle'], 
														  train_size=config_dict['data']['train_split'],
														  test_size=config_dict['data']['test_split'])

# MODEL FITTING 

# Selecting type of model based on configuration
if config_dict['model']['function'] == 'KNeighborsClassifier':
    model = KNeighborsClassifier(**config_dict['model']['KNeighborsClassifier'])
elif config_dict['model']['function'] == 'RandomForestClassifier':
	model = RandomForestClassifier(**config_dict['model']['RandomForestClassifier'])
else:
    sys.exit()

# Train (fit) the model 
print("Training (fitting) the model to the train data")
def fn():
    model.fit(X_train, y_train)

t = timeit.timeit(fn, number=1)

# Test the model on a validation / test set
y_pred = model.predict(X_test)
y_pred = [round(value) for value in y_pred]
test_accuracy = accuracy_score(y_test, y_pred)

stats_dict = {
	'training_time': t, 
	'test_accuracy': test_accuracy
}

# SAVE EXPERIMENT INFORMATION

SAFE_DIRECTORY_PATH = os.environ['DATMO_TASK_DIR']

# save configurations
print("Saving configurations...")
print(config_dict)
# flatten the config dict 
def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

printable_config_dict = flatten(config_dict)

config_filename = os.path.join(SAFE_DIRECTORY_PATH, 'config.json')
with open(config_filename, 'w') as f:
	f.write(json.dumps(printable_config_dict))

# save trained model 
print("Saving the trained model...")
model_filename = os.path.join(SAFE_DIRECTORY_PATH, 'model.dat')
pickle.dump(model, open(model_filename, 'wb'))

# saving performance metrics 
print("Saving the performance metrics...")
print(stats_dict)
stats_filename = os.path.join(SAFE_DIRECTORY_PATH, 'stats.json')
with open(stats_filename, 'w') as f:
    f.write(json.dumps(stats_dict))
