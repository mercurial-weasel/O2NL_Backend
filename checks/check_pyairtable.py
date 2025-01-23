from pyairtable import Api
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Airtable API key
api_key = os.getenv("AIRTABLE_API_KEY")

# Define base ID and table name
base_id = "app4p8WX4X6BRjei8"
table_name = "Field_SPT"

# Initialize the API and table
api = Api(api_key)
table = api.table(base_id, table_name)

# Define filter and sort parameters
filter_formula = "AND({POINT_ID} = 'BH501', {Zone} = 'Zone5')"
sort = ["Material"]

# Fetch records with pagination using iterate()
all_records = []
for record in table.iterate(formula=filter_formula, sort=sort, page_size=5):
    all_records.append(record)

# Print the records
print(all_records)

# Print summary
print(f"Total records retrieved: {len(all_records)}")
