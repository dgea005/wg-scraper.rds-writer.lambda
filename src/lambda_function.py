import logging
import os
import base64
import asyncio
import asyncpg
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DB_USER = os.environ['db_user']
DB_PASS = os.environ['db_pass']
DB_ENDPOINT = os.environ['db_endpoint']

# schema will be this
# but should add event_name
# meta_created_at
# event version
    # listing_id INTEGER DEFAULT NULL,
    # link TEXT DEFAULT NULL,
    # cost SMALLINT DEFAULT NULL,
    # size SMALLINT DEFAULT NULL,
    # stadt TEXT DEFAULT NULL,
    # free_from DATE DEFAULT NULL,
    # free_to DATE DEFAULT NULL,
    # stay_length SMALLINT DEFAULT NULL,
    # scrape_time TIMESTAMP DEFAULT NULL,
    # flat_type VARCHAR(50) DEFAULT '---'

def lambda_handler(event, context):
    for record in event['Records']:
       #Kinesis data is base64 encoded so decode here
       payload=base64.b64decode(record["kinesis"]["data"])
       #print("Decoded payload: " + str(payload))
       data = json.loads(str(payload))
       print("Loaded payload: " + data)

# def lambda_handler(event, context):

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(run())
#     return

# query = """
# INSERT INTO index_raw (listing_id, link, cost, size, stadt, free_from, free_to, stay_length, scrape_time, flat_type)
#   VALUES  (630515, 'http://some_link', 400, 18, 'Mitte', '2017-08-27', '2017-09-23', 27, '2017-08-24 07:20:13', 'studio');
# """

# async def run():
#     conn = await asyncpg.connect(user=DB_USER, password=DB_PASS, database='ScraperDatabase', host=DB_ENDPOINT)
#     await conn.execute(query)
#     await conn.close()
