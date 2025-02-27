from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshdeskCredentials

class FreshdeskGetToolInput(BaseModel):
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")


class FreshdeskGetTool(BaseTool):
    name: str = "freshdesk_get"
    description: str = "Tool for freshdesk get operation - get operation"
    args_schema: type[BaseModel] | None = FreshdeskGetToolInput
    credentials: Optional[FreshdeskCredentials] = None
