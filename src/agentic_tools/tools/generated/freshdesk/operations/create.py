from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import FreshdeskCredentials

class FreshdeskCreateToolInput(BaseModel):
    requester: Optional[str] = Field(None, description="Requester Identification")
    email: Optional[str] = Field(None, description="Primary email address of the contact. If you want to associate additional email(s) with this contact, use the other_emails attribute.")
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the contact")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    source: Optional[str] = Field(None, description="The channel through which the ticket was created")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    priority: Optional[str] = Field(None, description="Priority")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    requester_identification_value: Optional[str] = Field(None, description="Value of the identification selected")


class FreshdeskCreateTool(BaseTool):
    name: str = "freshdesk_create"
    description: str = "Tool for freshdesk create operation - create operation"
    args_schema: type[BaseModel] | None = FreshdeskCreateToolInput
    credentials: Optional[FreshdeskCredentials] = None
