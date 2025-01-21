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

# This file can be removed or updated if it contains other utility functions.
