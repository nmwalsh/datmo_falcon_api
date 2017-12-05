# data_handler.py
# 
# Argument handler that does 4 things.
#
# 1. Decode: deserialize raw input from API POST request received in `falcon_gateway.py`
# 2. Preprocess: convert input data into form required for model, as specified in `predict.py`
# 3. Postprocess: convert prediction from model (from `predict.py`) into form that can be serializable for serving API response
# 4. Encode: serialize postprocessed data into valid JSON-esque format for API response, and pass back to `falcon_gateway.py`

import json
from predict import predict

#raw_json = '{"sepal_length": [6.9], "sepal_width": [3.2], "petal_length": [5.7], "petal_width": [2.3]}'

def invoke_predict(raw_json):
	#convert args_dict to model_usable_data (have to pick model for this first)
	input_dict = json.loads(raw_json)
	# make your feature list here the order in which you need your model to accept input
	feature_list = ['sepal_length','sepal_width','petal_length','petal_width']
	mapped_inputs = [] #initialise list that mapped inputs will be put into from feature list and raw input
	for feature in feature_list:
		mapped_inputs.append(input_dict[feature][0])
	model_usable_data = [mapped_inputs] #convert 1D array to 2D array to satisfy model specific requirements
	

	raw_model_output =  predict(model_usable_data) #requires a predict function that purely returns response. Import up in imports.
	#prediction = json.load(str(raw_model_output)) #convert raw model results to json
	prediction = str(raw_model_output)
	return prediction #currently returns string
