import os
from pyairtable import Table
import logging

# Setup logging to file
logging.basicConfig(filename='airtable_debug.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Airtable credentials
AIRTABLE_API_KEY = "patOBN8J19OI6ENc0.6bcce66c1cd16501013ac7d4fdf0f1f0f06f6d2f629b3279e0d1f08ab9ac42b7"
AIRTABLE_BASE_ID = "app4p8WX4X6BRjei8"
AIRTABLE_TABLE_NAME = "Testing"

def connect_to_airtable():
    logging.debug(f"API Key: {AIRTABLE_API_KEY}")
    logging.debug(f"Base ID: {AIRTABLE_BASE_ID}")
    logging.debug(f"Table Name: {AIRTABLE_TABLE_NAME}")

    try:
        table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME)
        logging.debug("Making a call to Airtable...")
        records = table.all()
        logging.debug(f"Response: {records}")
        return records
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    connect_to_airtable()
