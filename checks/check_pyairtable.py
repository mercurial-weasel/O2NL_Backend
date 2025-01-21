from pyairtable import Api

api_key = "patOBN8J19OI6ENc0.9babcb77008d8880af171e19588fa874aabe91674f5c947f583b1320a87f24ca"
base_id = "app4p8WX4X6BRjei8"
table_name = "Testing"

api = Api(api_key)
table = api.table(base_id, table_name)

record = {
    "fields": {
        "name": "Test Record",  # Match Airtable column names
        "value": 123           # Match Airtable column names
    }
}

response = table.create(record)
print(response)
