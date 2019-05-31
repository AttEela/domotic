import os
from logger import logger
from flask import Flask, flash, render_template, request, session
# For WSGI server
try:
    from cheroot.wsgi import Server as WSGIServer
except ImportError:
    from cherrypy.wsgiserver import CherryPyWSGIServer as WSGIServer


app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        ip = request.remote_addr
        info_log = ip + " is accessing to the site"
        logger.info(info_log)
        return render_template('login.html')
    else:
        return render_template('remote_control.html')


@app.route('/light_on', methods=['GET'])
def light_on():
    if session.get('logged_in'):
        logger.info("The light has been turned on.")
        return render_template('remote_control.html')
    else:
        logger.info("Attempt to turn on the light without authentification")
        return render_template('redirection.html')


@app.route('/light_off', methods=['GET'])
def light_off():
    if session.get('logged_in'):
        logger.info("The light has been turned off.")
        return render_template('remote_control.html')
    else:
        logger.info("Attempt to turn off the light without authentification")
        return render_template('redirection.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    ip = request.remote_addr
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        info_log = ip + " successfully looged in"
        logger.info(info_log)
        flash('You were successfully logged in!')
    else:
        info_log = ip + " attempted to log in with wrong password"
        logger.warning(info_log)
        flash('wrong password!')
    return home()

##################################################
# END API part
##################################################


if __name__ == "__main__":
    logger.info('Starting Flask Server')
    app.secret_key = os.urandom(12)
    server = WSGIServer(('0.0.0.0', 5000), app, numthreads=30)

    try:
        server.start()
    except KeyboardInterrupt:
        logger.critical("KeyboardInterrupt")
server.stop()
