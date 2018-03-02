# predict.py
# Script that should consist of a single method (predict) - passing data in a presumed parsimonious syntax to your model for prediction
# 
# In this exaple, predict would require data of the following datatype:
# Pandas DataFrame with features 
# model --> loaded model file in pickle format
# X_test= [[ 6.9, 3.2, 5.7, 2.3]]
import pandas as pd
import random
import sklearn

random.seed(3)


# take input pd data frame and loaded model and return dictionary with classificaiton
def predict(model, X_test):
	# Class map
	Species_class_map = {0:'Iris-setosa', 1:'Iris-versicolor', 2:'Iris-virginica'}

	# Test feature
	y_pred = model.predict(X_test)
	y_pred = [round(value) for value in y_pred]
	prediction_result = {'Species': Species_class_map[y_pred[0]]}
	return prediction_result