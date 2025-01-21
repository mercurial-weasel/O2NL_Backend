from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class AirtableRecordCreate(BaseModel):
    name: str
    value: int

class AirtableRecord(BaseModel):
    id: Optional[str] = None
    fields: Dict[str, Any]
    created_time: Optional[str] = None

class AirtableTableResponse(BaseModel):
    records: List[AirtableRecord]
