from fastapi import FastAPI
from app.api.endpoints import airtable_endpoints
from app.core.settings import settings
from dotenv import load_dotenv
import logging

load_dotenv()

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(pathname)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

app = FastAPI()

# Include routes
app.include_router(airtable_endpoints.router, prefix="/api", tags=["Airtable"])

# ...existing code...

if __name__ == "__main__":
    import uvicorn
    logging.info("Starting the FastAPI application")
    uvicorn.run(app, host="0.0.0.0", port=8000)
