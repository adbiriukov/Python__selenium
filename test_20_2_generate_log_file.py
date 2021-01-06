import logging

logging.basicConfig(filename="./selenium_logs/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I: %M:%S %p',  # Date format
                    )


# To send all messages to the log file (if not it's send only warning, error and critical
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message\n")
