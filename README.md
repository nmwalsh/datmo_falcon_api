[![Datmo Model](https://datmo.com/nmwalsh/datmo_falcon_api/badge.svg)](https://datmo.com/nmwalsh/datmo_falcon_api)


# REST API -- Iris Flower Species Classification Model
_Example repo for deploying any Python3 Datmo model as a REST API_

This is our first example of being able to take a static model and deploy it to have a live inference REST API using Datmo. 
The goal of this is to show how easy it is to deploy models with Datmo in a platform agnostic fashion -- deploy on AWS, Azure, GCP, or even baremetal servers, with no need to manage compatabilities beyond standard server interfacing and the REST specification. 

This is a simple model that uses `scikit-learn` in `python3` to predict `species` for a given flower from the [Fisher Iris Flower Dataset].

## Getting Started

To understand how to adapt this code to your Datmo model, refer to the blog post [here] _not yet available_.

## Deployment

* 1. SSH into your server and [install Datmo.](https://datmo.com/get-started)
* 2. Restart your terminal (this allows Docker to have sudo permissions)
* 3.  Use Datmo to clone the model with:
```
$ datmo clone nmwalsh/datmo_falcon_api
```
* 4. Initialize the gunicorn server with:
```
$ datmo task run "usr/local/bin/gunicorn --access-logfile - -b 0.0.0.0:8000 falcon_gateway:app" --port 8000
```

`—access-logfile` is for enabling standard output for connection logging in gunicorn, which is disabled by default

`-b 0.0.0.0:8000` binds gunicorn to port 8000 of the 0.0.0.0 localhost on the container that the model and gunicorn is running. This is designating which port gunicorn should be looking at to receive a data stream from inside of the container.

`falcon_gateway:app` allows gunicorn to bind our falcon python app to be recognized as the official WSGI app to serve requests and responses to/from the server.

`—port 8000` is run to open up port 8000 on the docker container, so that it can receive requests from the physical server and return them as well. This is the outward facing port of the container.

## Try It Out:
If deployed locally, you can try it out with an example set of plant measurements:
```
curl 0.0.0.0:8000/predicts -L -X POST -d '{"sepal_length": [6.9], "sepal_width": [3.2], "petal_length": [5.7], "petal_width": [2.3]}' -H 'Content-type: application/json' 
```
## API Endpoints:
```
GET  | /info
GET  | /predicts
POST | /predicts -d {"key":[val]}
```
## Built With

* [Datmo](https://datmo.com) - Model versioning and env builder
* [Gunicorn](http://gunicorn.org/) - Python WSGI HTTP server framework
* [Falcon](http://falcon.readthedocs.io/en/stable/) - Highly performant baremetal Python API Framework that compiles in C


## License

This project is licensed under the MIT License