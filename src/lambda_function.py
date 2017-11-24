import logging
import os
import asyncio
import asyncpg

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    db_user = os.environ['db_user']
    db_pass = os.environ['db_pass']
    db_endpoint = os.environ['db_endpoint']
    logger.info(db_user)
    logger.info(db_endpoint)
    return
