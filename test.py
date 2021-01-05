import logging

logger = logging.getLogger('Test')
logger.setLevel('DEBUG')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(ch_format)
logger.addHandler(ch)


def testing():
    logger.info(f'This is {__name__} module.')



