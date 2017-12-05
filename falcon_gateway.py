# falcon_gateway.py

import falcon
import json
from data_handler import invoke_predict

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class InfoResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nThis is an API for a deployed Datmo model, '
                     'where it ______function______.\n'
                     'To learn more about this model, visit the repository online at:'
                     '\n'
                     '     https://datmo.com/nmwalsh/falcon-api-model\n\n')


class PredictsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nThis is the PREDICT endpoint. \n'
        			 'Both inputs and outputs are in the form of serialized JSON. \n'
        		     '\n'
        		     'INPUT:  Purchase Metadata [List of Nums] \n'
        		     'OUTPUT: Prediction [String]\n\n')

    def on_post(self, req, resp): 
        """Handles POST requests"""
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Error',
                ex.message)
 
        try:
            result_json = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                'Malformed JSON',
                'Could not decode the request body. The '
                'JSON was incorrect.')
 
        resp.status = falcon.HTTP_200
        #resp.body = json.dumps(invoke_predict(raw_json), encoding='utf-8') encoding not necessary in python3.
        resp.body = json.dumps(invoke_predict(raw_json))   

# falcon.API instances are callable WSGI apps. Never change this.
app = falcon.API()

# Resources are represented by long-lived class instances. Each Python class becomes a different "URL directory"
info = InfoResource()
predicts = PredictsResource()
# things will handle all requests to the '/things' URL path
app.add_route('/info', info)
app.add_route('/predicts', predicts)
