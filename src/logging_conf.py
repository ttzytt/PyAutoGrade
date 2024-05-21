import logging
from helpers import *

class _Logger(CfgFileRelated):
    def get_logger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # Create file handlerget
        file_handler = logging.FileHandler(self.temp_files_abs_path + '/log.log')
        file_handler.setLevel(logging.DEBUG)  # Log debug level and above to file

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Log info level and above to console

        # Create formatter and add it to the handlers
        formatter = logging.Formatter("[%(filename)s:%(lineno)s - %(funcName)20s() at %(asctime)s %(levelname)s] %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
LOGGER = _Logger().get_logger()