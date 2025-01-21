import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv
import logging

# Load test-specific environment variables
load_dotenv(dotenv_path=".env.test")

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(pathname)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("test.log"),
        logging.StreamHandler()
    ]
)

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="session")
def airtable_base_id():
    return os.getenv("AIRTABLE_BASE_ID")

@pytest.fixture(scope="session")
def airtable_table_name():
    return os.getenv("AIRTABLE_TABLE_NAME")

@pytest.fixture(scope="session")
def airtable_api_key():
    return os.getenv("AIRTABLE_API_KEY")
