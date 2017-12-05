[![Datmo Model](https://datmo.com/nmwalsh/datmo_falcon_api/badge.svg)](https://datmo.com/nmwalsh/datmo_falcon_api)


curl 0.0.0.0:8000/predicts -L -X POST -d ‘{“sepal_length”: [6.9], “sepal_width": [3.2], “petal_length": [5.7], ”petal_width": [2.3]}’ -H 'Content-type: application/json’ 


datmo task run "gunicorn --access-logfile - -b 0.0.0.0:8000 falcon_gateway:app" --port 8000

—access-logfile - is for enabling standard output for connection logging in gunicorn, which is disabled by default
-b 0.0.0.0:8000 binds gunicorn to port 8000 of the 0.0.0.0 localhost on the container that the model and gunicorn is running.
falcon_gateway:app allows gunicorn to bind our falcon python app to be recognized as the official WSGI app to serve requests and responses to/from.
—port 8000 is run to open up port 8000 on the docker container, so that it can receive requests from the EC2 instance/external, and return them as well.