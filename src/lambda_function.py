import logging
import os
import base64
import asyncio
import asyncpg
import json
from dateutil.parser import parse

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
       data = json.loads(payload)
       transformed = transform_wg_data(data)
       print("Loaded payload: " + str(transformed))


def validate_event(data):
    """
    when event has event_name and meta_created_at added
    then we want to make sure these fields exist and are valid
    that is, that they contain the data required

    returns if event is valid and transformation function to call (depending on name space)
    could also return the event name for logging and which function it will call
    """
    ## check what the keys are
    ## 

    pass


def transform_wg_data(data):
    ## could have different event names
    ## depending on the event name then call different versions of this function
    ## should this also validate the data?
    """
    for wg index data v0
    if event is valid and event name is index_v0
    then transform to python data types with this function

    returns: transform data dictionary

    should wrap call in try except to say if data could be transformed
    """
    # some of this is probably not necessary
    transformed_data = dict()
    transformed_data['listing_id'] = int(data['listing_id'])
    transformed_data['link'] = str(data['link'])
    transformed_data['cost'] = int(data['cost'])
    transformed_data['size'] = int(data['size'])
    transformed_data['stadt'] = str(data['stadt'])
    ## will need empty error handling here
    transformed_data['free_from'] = parse(data['free_from'].date())
    transformed_data['free_to'] = parse(data['free_to'].date())
    transformed_data['stay_length'] = int(data['stay_length'])
    transformed_data['scrape_time'] = parse(data['scrape_time'])
    transformed_data['flat_type'] = str(data['flat_type'])
    return transformed_data

def transform_to_postgres_input(transformed_dict):
    """
    transform validated data into data that can be inserted to database

    returns: query string to be inserted
    """
    pass

       

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
