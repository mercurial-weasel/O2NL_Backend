import requests

url = "https://api.airtable.com/v0/app4p8WX4X6BRjei8/Testing"
headers = {
    "Authorization": f"Bearer {"patOBN8J19OI6ENc0.6bcce66c1cd16501013ac7d4fdf0f1f0f06f6d2f629b3279e0d1f08ab9ac42b7"}",
    "Content-Type": "application/json"
}
data = {
    "fields": {
        "name": "Damn you",
        "value": 123
    }
}

response = requests.post(url, json=data, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.json())
