import logging
import os
import asyncio
import asyncpg

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DB_USER = os.environ['db_user']
DB_PASS = os.environ['db_pass']
DB_ENDPOINT = os.environ['db_endpoint']

def lambda_handler(event, context):

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    return


async def run():
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASS, database='ScraperDatabase', host=DB_ENDPOINT)
    values = await conn.fetch('''SELECT * FROM index_raw''')
    logger.info(values)
    await conn.close()


