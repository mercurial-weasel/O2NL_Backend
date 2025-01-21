import requests
import logging
from pathlib import Path

# Ensure log directory exists
LOG_DIR = Path("./logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "http_client.log"

# Configure the logging settings
logger = logging.getLogger("http_client")
logger.setLevel(logging.DEBUG)

# Create file handler which logs even debug messages
fh = logging.FileHandler(LOG_FILE)
fh.setLevel(logging.DEBUG)

# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def make_request(method: str, url: str, headers: dict, params: dict = None, json: dict = None):
    logger.debug(f"Entering make_request with method: {method}, url: {url}, headers: {headers}, params: {params}, json: {json}")
    if json:
        json = {"fields": json}
    logger.debug(f"[utils/http_client.py] Making {method} request to {url}")
    logger.debug(f"[utils/http_client.py] Headers: {headers}")
    logger.debug(f"[utils/http_client.py] Payload: {json}")

    response = requests.request(method, url, headers=headers, params=params, json=json)

    logger.debug(f"[utils/http_client.py] Response: {response.json()}")
    logger.debug(f"Exiting make_request with response: {response.json()}")

    response.raise_for_status()
    return response.json()
