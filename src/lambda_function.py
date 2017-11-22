import logging
import os


logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('testing lambda')

def lambda_handler(event, context):
    logger.info(event)
    logger.info(context)
    return