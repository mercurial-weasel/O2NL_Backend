import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AIRTABLE_API_KEY: str = os.getenv("AIRTABLE_API_KEY")
    AIRTABLE_BASE_ID: str = os.getenv("AIRTABLE_BASE_ID")
    AIRTABLE_TABLE_NAME: str = os.getenv("AIRTABLE_TABLE_NAME")

settings = Settings()
