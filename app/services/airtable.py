from app.core.settings import settings
from app.utils.http_client import make_request
import logging

logger = logging.getLogger("app")

class AirtableService:
    def __init__(self, api_key: str, base_id: str, table_name: str):
        self.api_key = api_key
        self.base_id = base_id
        self.table_name = table_name
        self.base_url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_table(self):
        logger.debug(f"Entering get_table for table {self.table_name}")
        response = make_request("GET", self.base_url, headers=self.headers)
        logger.debug(f"Response from get_table: {response}")
        logger.debug(f"Exiting get_table for table {self.table_name}")
        return response["records"]

    def read_record(self, record_id: str):
        url = f"{self.base_url}/{record_id}"
        logger.debug(f"Entering read_record for record {record_id} from table {self.table_name}")
        response = make_request("GET", url, headers=self.headers)
        logger.debug(f"Response from read_record: {response}")
        logger.debug(f"Exiting read_record for record {record_id} from table {self.table_name}")
        return response

    def create_record(self, record: dict):
        logger.debug(f"Entering create_record with data: {record}")
        response = make_request("POST", self.base_url, headers=self.headers, json=record)
        logger.debug(f"Response from create_record: {response}")
        logger.debug(f"Exiting create_record with data: {record}")
        return response

    def update_record(self, record_id: str, record: dict):
        url = f"{self.base_url}/{record_id}"
        logger.debug(f"Entering update_record for record {record_id} with data: {record}")
        response = make_request("PATCH", url, headers=self.headers, json=record)
        logger.debug(f"Response from update_record: {response}")
        logger.debug(f"Exiting update_record for record {record_id} with data: {record}")
        return response

    def delete_record(self, record_id: str):
        url = f"{self.base_url}/{record_id}"
        logger.debug(f"Entering delete_record for record {record_id}")
        response = make_request("DELETE", url, headers=self.headers)
        logger.debug(f"Response from delete_record: {response}")
        logger.debug(f"Exiting delete_record for record {record_id}")
        return response

airtable_service = AirtableService(api_key=settings.AIRTABLE_API_KEY, base_id=settings.AIRTABLE_BASE_ID, table_name=settings.AIRTABLE_TABLE_NAME)
