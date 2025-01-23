from pyairtable import Api, Table
from app.core.settings import settings
import logging
from typing import List, Dict, Optional

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

    def get_filtered_sorted_records(
        self,
        base_id: str,
        table_name: str,
        point_id: Optional[str] = None,
        zone: Optional[str] = None,
        sort_by: Optional[str] = "Material"
    ) -> List[Dict]:
        """
        Retrieve all records from a specified table with optional filtering and sorting.

        Args:
            base_id (str): The base ID.
            table_name (str): The table name.
            point_id (Optional[str]): Filter records by POINT_ID (optional).
            zone (Optional[str]): Filter records by Zone (optional).
            sort_by (Optional[str]): Sort records by a field (default: Material).

        Returns:
            List[Dict]: List of filtered and sorted records.
        """
        logger.debug(f"Get the table")
        table = Table(self.api_key, base_id, table_name)

        logger.debug(f"Setup the filters")

        # Build the filter formula dynamically
        filters = []
        if point_id:
            filters.append(f"{{POINT_ID}} = '{point_id}'")
        if zone:
            filters.append(f"{{Zone}} = '{zone}'")
        filter_formula = "AND(" + ", ".join(filters) + ")" if filters else None

        logger.debug(f"Filters {filters}")
        logger.debug(f"Filter formula: {filter_formula}")

        try:
            # Get records with filtering and sorting
            records = table.all(
                formula=filter_formula,
                sort=[sort_by]
            )
            logger.debug(f"Retrieved {len(records)} records from table {table_name}")
            logger.debug(f"Records: {records}")
            return [record for record in records]
        except Exception as e:
            logger.error(f"Error retrieving records: {e}")
            logger.error(f"Response content: {e.response.content if hasattr(e, 'response') else 'No response content'}")
            raise

airtable_service = AirtableService(api_key=settings.AIRTABLE_API_KEY)
