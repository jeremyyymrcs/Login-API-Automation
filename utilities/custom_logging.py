import logging
import colorlog

def clear_custom_log_file():
    with open('my_custom.log', 'w'):
        pass  # This will clear the file by opening it in write mode and immediately closing it

def get_custom_logger(name, log_level=logging.INFO):
    # Clear the log file before configuring the logger
    clear_custom_log_file()

    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Create a formatter
    formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(levelname)s - %(message)s%(reset)s',
        datefmt='%Y-%m-%d %I:%M:%S %p',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )

    # Create a file handler
    file_handler = logging.FileHandler('my_custom.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
