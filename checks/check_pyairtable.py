from pyairtable import Api

api_key = "patOBN8J19OI6ENc0.6bcce66c1cd16501013ac7d4fdf0f1f0f06f6d2f629b3279e0d1f08ab9ac42b7"
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
