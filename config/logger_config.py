from config import environment 
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
# from context import request_context



def get_logger(name: str = __name__):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = AzureLogHandler(connection_string=environment.azurelogging)

        
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger