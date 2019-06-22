# include .env file
include .env
export
# this is usefull with most python apps in dev mode because if stdout is
# buffered logs do not shows in realtime
PYTHONUNBUFFERED=1
export PYTHONUNBUFFERED

PYTHON?=venv_domotic/bin/python

build: venv_domotic

venv_domotic: lxml_requirements venv_domotic/bin/activate 

lxml_requirements:
	sudo apt-get install libxml2-dev libxslt-dev #because lxml contains C modules that need to be compiled
	# see here for details https://stackoverflow.com/questions/13019942/why-cant-i-get-pip-install-lxml-to-work-within-a-virtualenv
	touch lxml_requirements

venv_domotic/bin/activate: requirements.txt
	test -d venv_domotic || virtualenv -p /usr/local/bin/python3 venv_domotic
	venv_domotic/bin/pip install -Ur requirements.txt

test: venv_domotic

server: venv_domotic
	$(PYTHON) ./app/server.py

handler: venv_domotic
	$(PYTHON) ./app/snips-handler.py

up: venv_domotic
	$(PYTHON) ./app/snips-handler.py & $(PYTHON) ./app/server.py

clean:
	rm ./logs/server_activity*
	rm -rf ./venv_domotic
