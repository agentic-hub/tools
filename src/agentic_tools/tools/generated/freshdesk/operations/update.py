from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshdeskCredentials

class FreshdeskUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="Contact ID")


class FreshdeskUpdateTool(BaseTool):
    name: str = "freshdesk_update"
    connector_id: str = "nodes-base.freshdesk"
    description: str = "Tool for freshdesk update operation - update operation"
    args_schema: type[BaseModel] | None = FreshdeskUpdateToolInput
    credentials: Optional[FreshdeskCredentials] = None
