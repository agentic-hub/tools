from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SyncromspCredentials

class SyncromspGetToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    customer_id: Optional[str] = Field(None, description="Get specific customer by ID")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    alert_id: Optional[str] = Field(None, description="Get specific RMM alert by ID")
    email: Optional[str] = Field(None, description="Email")
    contact_id: Optional[str] = Field(None, description="Get specific contact by ID")
    ticket_id: Optional[str] = Field(None, description="Get specific customer by ID")
    operation: Optional[str] = Field(None, description="Operation")


class SyncromspGetTool(BaseTool):
    name: str = "syncromsp_get"
    description: str = "Tool for syncroMsp get operation - get operation"
    args_schema: type[BaseModel] | None = SyncromspGetToolInput
    credentials: Optional[SyncromspCredentials] = None
