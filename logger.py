import logging
# import os

from logging.handlers import RotatingFileHandler

# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger()
logger_level = "DEBUG"  # os.environ.get("LOGGER_LEVEL")
path_to_activity = "./" + "logs" + "/"  # os.environ.get("LOG_PATH") + "/"
# on met le niveau du logger à DEBUG, comme ça il écrit tout
logger.setLevel(getattr(logging, logger_level))

# création d'un formateur qui va ajouter le temps, le niveau
# de chaque message quand on écrira un message dans le log
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
file_handler = RotatingFileHandler(path_to_activity + 'server_activity.log',
                                   'a', 10000000, 1)
# on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
# créé précédement et on ajoute ce handler au logger
file_handler.setLevel(getattr(logging, logger_level))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# création d'un second handler qui va rediriger chaque écriture de log
# sur la console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(getattr(logging, logger_level))
logger.addHandler(stream_handler)
