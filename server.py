from logger import logger
from flask import Flask, jsonify

# For WSGI server
try:
    from cheroot.wsgi import Server as WSGIServer
except ImportError:
    from cherrypy.wsgiserver import CherryPyWSGIServer as WSGIServer


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    response = "Hello World !"
    return response


@app.route("/coralie", methods=['GET'])
def get_nofilter_articles():
    return jsonify({"Message": "Coucou mon amour"})


##################################################
# END API part
##################################################
if __name__ == "__main__":
    logger.info('Starting Flask Server')
    server = WSGIServer(('0.0.0.0', 5000),
                        app,
                        numthreads=30)

    try:
        server.start()
    except KeyboardInterrupt:
        logger.critical("KeyboardInterrupt")
server.stop()
