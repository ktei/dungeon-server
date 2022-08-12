#!/bin/bash

# export FLASK_APP=main.py
# export FLASK_ENV=development
# flask run -p 4000


gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker --bind 0.0.0.0:4000 -w 1 main:app
