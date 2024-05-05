import logging

def get_application_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("uvicorn.info")
    return logger
