import logging
import os

def setup_logger():
    log_file = 'test_log.log'
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def log_message(message):
    logging.info(message)
