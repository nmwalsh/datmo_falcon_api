FROM datmo/xgboost:cpu
RUN apt-get update
RUN apt-get install gunicorn
RUN pip install falcon
EXPOSE 8000