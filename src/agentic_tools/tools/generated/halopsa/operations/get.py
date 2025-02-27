from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HalopsaCredentials

class HalopsaGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    site_id: Optional[str] = Field(None, description="Site ID")
    user_id: Optional[str] = Field(None, description="User ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    client_id: Optional[str] = Field(None, description="Client ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    simplify: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class HalopsaGetTool(BaseTool):
    name: str = "halopsa_get"
    description: str = "Tool for haloPSA get operation - get operation"
    args_schema: type[BaseModel] | None = HalopsaGetToolInput
    credentials: Optional[HalopsaCredentials] = None
