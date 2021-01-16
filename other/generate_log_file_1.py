import logging

logging.basicConfig(filename="../files/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I: %M:%S %p',  # Date format
                    # To send all messages to the log file (if not it's send only warning, error and critical
                    level=logging.DEBUG)


logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message\n")
