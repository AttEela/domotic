# Domotic

Little home made domotic project.
The idea is to build a web page and use a voice assisitant to control a tv and other things like shutters or lights and host it on a Raspberry Pie.

To see how to do the configutation of the Raspberry Pie, see `https://github.com/AttEela/raspberry`

### Prerequisites

- A Raspberry Pie
- ReSpeaker 2-Mics Pi HAT (for vocal command features)
- Works with Python >= 3.6 and virtualenv (I used virtualenv==16.6.0)

In order to use vocal commands, some configurations should be done on the RPi with Snips assitants.
Please follow the tutorial : `https://docs.snips.ai/getting-started/quick-start-raspberry-pi`  

Therefore, in this project, in order to use the voice command features, the command `sam status` should return this:
```
Connected to device RASPBERRY_NAME
​
OS version ................... Raspbian GNU/Linux 9 (stretch)
Installed assistant .......... Not installed
Status ....................... Installed, not running
​
Service status:
​
snips-analytics .............. 0.55.2 (not running)
snips-asr .................... 0.55.2 (not running)
snips-audio-server ........... 0.55.2 (running)
snips-dialogue ............... 0.55.2 (not running)
snips-hotword ................ 0.55.2 (not running)
snips-nlu .................... 0.55.2 (not running)
snips-skill-server ........... 0.55.2 (not running)
snips-tts .................... 0.55.2 (running)
```


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

### Running the server to enable back-end for the remote:

Launch the server and the snips-intent handler :

```
make up
```

You should see:
```
Running Flask Server on http://localhost:5000
Connected to localhost with result code 0
```

And go check on `http://localhost:SERVER_PORT` (default port is 5000).

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
DOMOTIC_INTENT is related to snips detected intents
