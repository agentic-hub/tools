from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshdeskCredentials

class FreshdeskGetallToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")


class FreshdeskGetallTool(BaseTool):
    name: str = "freshdesk_getall"
    description: str = "Tool for freshdesk getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = FreshdeskGetallToolInput
    credentials: Optional[FreshdeskCredentials] = None
