# Domotic

Little home made domotic project.
The idea is to build a web page to control a tv and other things like shutter or lights and host it on a Raspberry Pie.


### Prerequisites

Works with Python 3.6.5.


### Installing

First create a `.env` file like `.env_dist`

```
cp .env_dist .env
```
Modify the variables as you wish in the `.env`. See below to know how.

Then install the requirements.

```
make build
```

### Running the tests

Launch the server:

```
make up
```

And go check on `http://localhost:SERVER_PORT` (default is 5000).

Try to log in with anything. It should work only with:
```
user : FLASK_USR (default is atteela)
password : FLASK_PWD (default is azerty)
```

#### Description of variable in .env

LOG_LEVEL is the level of the logger.  
LOG_PATH is the folder where to store the logs in the file `server_activity.log`.  
LOG_FORMAT is the format of logs to parse the logs easily.
FLASK_USR is the username of the web app.
FLASK_PWD is the password of the web app
