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

query = """
INSERT INTO index_raw (listing_id, link, cost, size, stadt, free_from, free_to, stay_length, scrape_time, flat_type)
  VALUES  (630515, 'http://some_link', 400, 18, 'Mitte', '2017-08-27', '2017-09-23', 27, '2017-08-24 07:20:13', 'studio');
"""

async def run():
    conn = await asyncpg.connect(user=DB_USER, password=DB_PASS, database='ScraperDatabase', host=DB_ENDPOINT)
    await conn.execute(query)
    await conn.close()


