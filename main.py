import logging
from logging_setup import setup_logging, configure_logger
setup_logging()
app_logger = configure_logger('MAIN', logging.DEBUG)

def main():
    # TODO: Start the bot
    pass

if __name__ == "__main__":
    app_logger.info('Application started')
    main()
    app_logger.info('Application finished')
