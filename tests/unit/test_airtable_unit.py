import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.airtable_schemas import AirtableRecordCreate
import logging

client = TestClient(app)
logger = logging.getLogger("app")

@pytest.fixture
def airtable_record():
    return {
        "name": "Test Record",  # Ensure the field name matches the Airtable schema
        "value": 123  # Ensure the field name matches the Airtable schema
    }

def create_airtable_record(test_client, base_id, table_name, record, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    url = f"/api/{base_id}/{table_name}"
    response = test_client.post(url, json=record, headers=headers)
    return response

def test_get_airtable_tables():
    response = client.get("/api/airtable/test_base_id/test_table_name")
    assert response.status_code == 200
    assert "records" in response.json()

def test_get_airtable_tables(test_client: TestClient, airtable_base_id, airtable_table_name, airtable_api_key):
    headers = {
        "Authorization": f"Bearer {airtable_api_key}",
    }
    response = test_client.get(f"/api/{airtable_base_id}/{airtable_table_name}", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json()["records"], list)

def test_create_airtable_record(test_client: TestClient, airtable_base_id, airtable_table_name, airtable_record, airtable_api_key):
    response = create_airtable_record(test_client, airtable_base_id, airtable_table_name, airtable_record, airtable_api_key)
    assert response.status_code == 200
    assert response.json()["fields"]["name"] == "Test Record"
    assert response.json()["fields"]["value"] == 123

def test_update_airtable_record(test_client: TestClient, airtable_base_id, airtable_table_name, airtable_record, airtable_api_key):
    # First, create a record to update
    create_response = create_airtable_record(test_client, airtable_base_id, airtable_table_name, airtable_record, airtable_api_key)
    record_id = create_response.json()["id"]

    # Update the record
    updated_record = {"fields": {"name": "Updated Record", "value": 456}}
    headers = {
        "Authorization": f"Bearer {airtable_api_key}",
        "Content-Type": "application/json",
    }
    update_response = test_client.patch(f"/api/{airtable_base_id}/{airtable_table_name}/{record_id}", json=updated_record, headers=headers)
    assert update_response.status_code == 200
    assert update_response.json()["fields"]["name"] == "Updated Record"
    assert update_response.json()["fields"]["value"] == 456

def test_delete_airtable_record(test_client: TestClient, airtable_base_id, airtable_table_name, airtable_record, airtable_api_key):
    # First, create a record to delete
    create_response = create_airtable_record(test_client, airtable_base_id, airtable_table_name, airtable_record, airtable_api_key)
    record_id = create_response.json()["id"]

    # Delete the record
    headers = {
        "Authorization": f"Bearer {airtable_api_key}",
    }
    delete_response = test_client.delete(f"/api/{airtable_base_id}/{airtable_table_name}/{record_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Record deleted successfully"

def test_full_crud_operations(test_client: TestClient, airtable_base_id, airtable_table_name, airtable_record, airtable_api_key):
        # Create a record
    create_response = create_airtable_record(test_client, airtable_base_id, airtable_table_name, airtable_record, airtable_api_key)
    assert create_response.status_code == 200
    record_id = create_response.json()["id"]

    # Read the created record
    headers = {
        "Authorization": f"Bearer {airtable_api_key}",
    }
    read_response = test_client.get(f"/api/{airtable_base_id}/{airtable_table_name}/{record_id}", headers=headers)
    assert read_response.status_code == 200
    assert read_response.json()["fields"]["name"] == "Test Record"
    assert read_response.json()["fields"]["value"] == 123

    # Update the record
    updated_record = {"fields": {"name": "Updated Record", "value": 456}}
    update_response = test_client.patch(f"/api/{airtable_base_id}/{airtable_table_name}/{record_id}", json=updated_record, headers=headers)
    assert update_response.status_code == 200
    assert update_response.json()["fields"]["name"] == "Updated Record"
    assert update_response.json()["fields"]["value"] == 456

    # Read the updated record
    read_response = test_client.get(f"/api/{airtable_base_id}/{airtable_table_name}/{record_id}", headers=headers)
    assert read_response.status_code == 200
    assert read_response.json()["fields"]["name"] == "Updated Record"
    assert read_response.json()["fields"]["value"] == 456

    # Delete the record
    delete_response = test_client.delete(f"/api/{airtable_base_id}/{airtable_table_name}/{record_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Record deleted successfully"
