from fastapi import APIRouter, Depends, HTTPException
import logging
from app.core.settings import settings
from app.api.dependencies.airtable_dependencies import get_airtable_service
from app.services.airtable_services import AirtableService
from app.schemas.airtable_schemas import AirtableTableResponse, AirtableRecord, AirtableRecordCreate

# Setup logging to file
logging.basicConfig(filename='airtable_debug.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(pathname)s - %(levelname)s - %(message)s')

router = APIRouter()

@router.get("/{base_id}/{table_name}", response_model=AirtableTableResponse)
def get_table(
    base_id: str,
    table_name: str,
    airtable_service: AirtableService = Depends(get_airtable_service),
):
    logging.debug(f"Entering get_table endpoint for base_id: {base_id}, table_name: {table_name}")
    try:
        data = airtable_service.get_table(base_id, table_name)
        return {"records": data}
    except Exception as e:
        logging.error(f"Error in get_table endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{base_id}/{table_name}/{record_id}", response_model=AirtableRecord)
def read_record(
    base_id: str,
    table_name: str,
    record_id: str,
    airtable_service: AirtableService = Depends(get_airtable_service),
):
    logging.debug(f"Entering read_record endpoint for base_id: {base_id}, table_name: {table_name}, record_id: {record_id}")
    try:
        data = airtable_service.read_record(base_id, table_name, record_id)
        return data
    except Exception as e:
        logging.error(f"Error in read_record endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{base_id}/{table_name}/create", response_model=AirtableRecord)
def create_record(
    base_id: str,
    table_name: str,
    record: AirtableRecordCreate,
    airtable_service: AirtableService = Depends(get_airtable_service),
):
    logging.debug(f"Entering create_record endpoint for base_id: {base_id}, table_name: {table_name} with data: {record}")
    try:
        data = airtable_service.create_record(base_id, table_name, record.model_dump())
        return data
    except Exception as e:
        logging.error(f"Error in create_record endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{base_id}/{table_name}/{record_id}", response_model=AirtableRecord)
def update_record(
    base_id: str,
    table_name: str,
    record_id: str,
    record: AirtableRecord,
    airtable_service: AirtableService = Depends(get_airtable_service),
):
    logging.debug(f"Entering update_record endpoint for base_id: {base_id}, table_name: {table_name}, record_id: {record_id} with data: {record}")
    try:
        update_data = {k: v for k, v in record.fields.items() if v is not None}
        data = airtable_service.update_record(base_id, table_name, record_id, update_data)
        return data
    except Exception as e:
        logging.error(f"Error in update_record endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{base_id}/{table_name}/{record_id}")
def delete_record(
    base_id: str,
    table_name: str,
    record_id: str,
    airtable_service: AirtableService = Depends(get_airtable_service),
):
    logging.debug(f"Entering delete_record endpoint for base_id: {base_id}, table_name: {table_name}, record_id: {record_id}")
    try:
        airtable_service.delete_record(base_id, table_name, record_id)
        return {"message": "Record deleted successfully"}
    except Exception as e:
        logging.error(f"Error in delete_record endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/check-connection")
async def check_airtable_connection():
    logging.debug(f"Entering check_airtable_connection endpoint")

    try:
        airtable_service = AirtableService(api_key=settings.AIRTABLE_API_KEY)
        airtable_service.get_table(settings.AIRTABLE_BASE_ID, settings.AIRTABLE_TABLE_NAME)
        return {"success": True, "message": "Connection successful"}
    except Exception as e:
        logging.error(f"Connection failed: {str(e)}")
        return {"success": False, "message": "Connection failed", "error": str(e)}
