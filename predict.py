# predict.py
# Script that should consist of a single method (predict) - passing data in a presumed parsimonious syntax to your model for prediction
# 
# In this exaple, predict would require data of the following datatype:
# Pandas DataFrame with features 
# X_test= [[ 6.9, 3.2, 5.7, 2.3]]
import os
import pickle
import pandas as pd
import random
import sklearn

random.seed(3)


# take input pd data frame and return dictionary with classificaiton
def predict(X_test):
	# loading model file
	model_filename = os.path.join('model.dat')
	model = pickle.load(open(model_filename, 'rb'))
	Species_class_map = {0:'Iris-setosa', 1:'Iris-versicolor', 2:'Iris-virginica'}

	# Test feature
	y_pred = model.predict(X_test)
	y_pred = [round(value) for value in y_pred]
	prediction_result = {'Species': Species_class_map[y_pred[0]]}
	return prediction_result