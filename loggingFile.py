import logging

def loggingFunction():

    logger = logging.getLogger('__name__')
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler('AlleBotLog.log', mode= 'w')
    fileHandler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(name)s - %(levelname)s: - %(message)s')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger

