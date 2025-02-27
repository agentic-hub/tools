from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshdeskCredentials

class FreshdeskDeleteToolInput(BaseModel):
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")


class FreshdeskDeleteTool(BaseTool):
    name: str = "freshdesk_delete"
    connector_id: str = "nodes-base.freshdesk"
    description: str = "Tool for freshdesk delete operation - delete operation"
    args_schema: type[BaseModel] | None = FreshdeskDeleteToolInput
    credentials: Optional[FreshdeskCredentials] = None
