from pyairtable import Api
from app.core.settings import settings
import logging

logger = logging.getLogger("app")

class AirtableService:
    def __init__(self, api_key: str, base_id: str, table_name: str):
        self.api_key = api_key
        self.base_id = base_id
        self.table_name = table_name
        self.api = Api(api_key)
        self.table = self.api.table(base_id, table_name)

    def get_table(self):
        logger.debug(f"Entering get_table for table {self.table_name}")
        response = self.table.all()
        logger.debug(f"Response from get_table: {response}")
        logger.debug(f"Exiting get_table for table {self.table_name}")
        return response

    def read_record(self, record_id: str):
        response = self.table.get(record_id)
        logger.debug(f"Response from read_record: {response}")
        return response

    def create_record(self, record: dict):
        response = self.table.create(record)
        logger.debug(f"Response from create_record: {response}")
        return response

    def update_record(self, record_id: str, record: dict):
        response = self.table.update(record_id, record)
        logger.debug(f"Response from update_record: {response}")
        return response

    def delete_record(self, record_id: str):
        response = self.table.delete(record_id)
        logger.debug(f"Response from delete_record: {response}")
        return response

airtable_service = AirtableService(api_key=settings.AIRTABLE_API_KEY, base_id=settings.AIRTABLE_BASE_ID, table_name=settings.AIRTABLE_TABLE_NAME)
