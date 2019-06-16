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
	sudo apt-get install libxml2-dev libxslt-dev #because lxml contains C modules that need to be compiled
	# see here for details https://stackoverflow.com/questions/13019942/why-cant-i-get-pip-install-lxml-to-work-within-a-virtualenv
	pip install -r requirements.txt

server:
	python ./app/server.py

handler:
	python ./app/snips-handler.py

up:
	python ./app/snips-handler.py & python ./app/server.py
