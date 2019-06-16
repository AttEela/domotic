import os
import logging
from logging.handlers import RotatingFileHandler

logger_level = os.environ.get("LOG_LEVEL")
log_format = os.environ.get("LOG_FORMAT")
path_to_activity_log = os.path.join(".",
                                    os.environ.get("LOG_PATH"),
                                    'server_activity.log')


class LogManager:
    def __init__(self, logger_level=logger_level, path_to_activity=path_to_activity_log):
        self.logger = logging.getLogger()
        self.logger.setLevel(getattr(logging, logger_level))
        self.formatter = logging.Formatter(log_format)
        self.file_handler = RotatingFileHandler(filename=path_to_activity_log,
                                                mode='a',
                                                maxBytes=10000,
                                                backupCount=1)
        self.file_handler.setLevel(getattr(logging, logger_level))
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setLevel(getattr(logging, logger_level))
        self.logger.addHandler(self.stream_handler)
