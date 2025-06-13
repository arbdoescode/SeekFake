from config import environment 
import logging
import json
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorLogExporter

class LoggingHelper:
    _exporter = None
    _connection_string = environment.azurelogging
    
    @staticmethod
    def log_structured(logger, data: dict):
        logger.info(f"{json.dumps(data)}")

    @classmethod
    def _initialize_exporter(cls):
        if cls._exporter is None:
            cls._exporter = AzureMonitorLogExporter(connection_string=cls._connection_string)

    @classmethod
    def get_logger(cls, service_name: str, level=logging.INFO) -> logging.Logger:
        cls._initialize_exporter()

        resource = Resource.create({
            "service.name": service_name
        })

        logger_provider = LoggerProvider(resource=resource)
        logger_provider.add_log_record_processor(
            BatchLogRecordProcessor(cls._exporter)
        )

        otel_handler = LoggingHandler(level=level, logger_provider=logger_provider)

        logger = logging.getLogger(service_name)
        logger.setLevel(level)

        if not logger.hasHandlers():
            logger.addHandler(otel_handler)

        return logger