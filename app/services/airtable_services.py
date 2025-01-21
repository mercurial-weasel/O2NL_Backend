from pyairtable import Api
from app.core.settings import settings
import logging

logger = logging.getLogger("app")

class AirtableService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api = Api(api_key)

    def get_table(self, base_id: str, table_name: str):
        logger.debug(f"Entering get_table for table {table_name}")
        table = self.api.table(base_id, table_name)
        response = table.all()
        logger.debug(f"Response from get_table: {response}")
        logger.debug(f"Exiting get_table for table {table_name}")
        return response

    def read_record(self, base_id: str, table_name: str, record_id: str):
        table = self.api.table(base_id, table_name)
        response = table.get(record_id)
        logger.debug(f"Response from read_record: {response}")
        return response

    def create_record(self, base_id: str, table_name: str, record: dict):
        table = self.api.table(base_id, table_name)
        response = table.create(record)
        logger.debug(f"Response from create_record: {response}")
        return response

    def update_record(self, base_id: str, table_name: str, record_id: str, record: dict):
        table = self.api.table(base_id, table_name)
        response = table.update(record_id, record)
        logger.debug(f"Response from update_record: {response}")
        return response

    def delete_record(self, base_id: str, table_name: str, record_id: str):
        table = self.api.table(base_id, table_name)
        response = table.delete(record_id)
        logger.debug(f"Response from delete_record: {response}")
        return response

airtable_service = AirtableService(api_key=settings.AIRTABLE_API_KEY)
