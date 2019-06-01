import os
from logger import LogManager
from flask import Flask, flash, render_template, request, session
# For WSGI server
try:
    from cheroot.wsgi import Server as WSGIServer
except ImportError:
    from cherrypy.wsgiserver import CherryPyWSGIServer as WSGIServer


app = Flask(__name__)


@app.route('/')
def index():
    if not session.get('logged_in'):
        ip = request.remote_addr
        logger.info("{ip} is accessing to the site".format(ip=ip))
        return render_template('login.html')
    else:
        return render_template('remote_control.html')


@app.route('/light_on', methods=['GET'])
def light_on():
    if session.get('logged_in'):
        logger.info("The light has been turned on.")
        return render_template('remote_control.html')
    else:
        logger.warning("Attempt to turn on the light without authentification")
        return render_template('redirection.html')


@app.route('/light_off', methods=['GET'])
def light_off():
    if session.get('logged_in'):
        logger.info("The light has been turned off.")
        return render_template('remote_control.html')
    else:
        logger.warning("Attempt to turn off the light without authentification")
        return render_template('redirection.html')


@app.route('/login', methods=['POST'])
def admin_login():
    ip = request.remote_addr
    request_usr = request.form['username']
    request_pwd = request.form['password']
    sucess_login = ((request_usr == os.environ.get("FLASK_USR"))
                    & (request_pwd == os.environ.get("FLASK_PWD")))
    if sucess_login:
        session['logged_in'] = True
        logger.info("{ip} successfully looged in".format(ip=ip))
        flash('You were successfully logged in!')
    else:
        logger.warning("{ip} attempted to log in with wrong password".format(ip=ip))
        flash('wrong password!')
    return index()


##################################################
# END API part
##################################################


if __name__ == "__main__":

    log_manager = LogManager()
    logger = log_manager.logger
    logger.info('Running Flask Server on http://localhost:{port}'
                .format(port=os.environ.get("SERVER_PORT")))
    app.secret_key = os.urandom(12)
    server = WSGIServer(('0.0.0.0', int(os.environ.get("SERVER_PORT"))),
                        app,
                        numthreads=int(os.environ.get("SERVER_NUM_THREADS")))

    try:
        server.start()
    except KeyboardInterrupt:
        logger.critical("KeyboardInterrupt")
