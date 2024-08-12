import logging
import json
import logging.config
from pathlib import Path

def setup_logging(default_path='logging_setup/logging_config.json', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration"""
    path = Path(default_path)
    value = Path(Path.home(), env_key)
    if value.exists():
        path = value
    try:
        with open(path, 'r') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    except Exception as e:
        logging.basicConfig(level=default_level)
        logging.error("Error in logging configuration: %s", e)

def configure_logger(logger_name, level=logging.INFO, add_handler=True):
    """Configure a specific logger"""
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    if add_handler:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

