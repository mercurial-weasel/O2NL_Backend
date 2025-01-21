from app.services.airtable import AirtableService
from app.core.settings import settings

def get_airtable_service():
    return AirtableService(api_key=settings.AIRTABLE_API_KEY, base_id=settings.AIRTABLE_BASE_ID, table_name=settings.AIRTABLE_TABLE_NAME)
