# include .env file
include .env
export
# this is usefull with most python apps in dev mode because if stdout is
# buffered logs do not shows in realtime
PYTHONUNBUFFERED=1
export PYTHONUNBUFFERED

clean:
	rm ./logs/server_activity*

build:
	pip install -r requirements.txt

up:
	python ./app/server.py
