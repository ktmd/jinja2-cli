import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')

logging.basicConfig(level=logging.INFO)
logging.debug('This will get logged to DEBUG')

logging.basicConfig(filename='sample_app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')