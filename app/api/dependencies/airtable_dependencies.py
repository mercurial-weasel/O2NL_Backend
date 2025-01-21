from app.services.airtable_services import AirtableService
from app.core.settings import settings

def get_airtable_service():
    return AirtableService(api_key=settings.AIRTABLE_API_KEY)
