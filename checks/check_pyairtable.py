from pyairtable import Api
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("AIRTABLE_API_KEY")
base_id = os.getenv("AIRTABLE_BASE_ID")
table_name = os.getenv("AIRTABLE_TABLE_NAME")

api = Api(api_key)
table = api.table(base_id, table_name)

record = {
        "name": "bloody hell it works",  # Match Airtable column names
        "value": 123           # Match Airtable column names
}

response = table.create(record)
print(response)
