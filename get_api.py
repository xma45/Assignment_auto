import requests
import logging
import os 
import json

LOG_LEVEL = os.environ['ENV']

logging.basicConfig(level = logging.DEBUG,
                    format = '[%(asctime)s] %(levelname)s %(message)s')
def run():
    response = requests.get('https://6god8pgyzf.execute-api.us-west-2.amazonaws.com/databases')
    logger = logging.getLogger(__name__)
    result = response.json()
    if LOG_LEVEL == "DEV":
        for item in result.get('databases'):
            logger.debug(item)



if __name__ == '__main__':
    run()
