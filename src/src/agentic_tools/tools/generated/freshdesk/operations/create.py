from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshdeskCreateToolInput(BaseModel):
    requester: Optional[str] = Field(None, description="Requester Identification")
    email: Optional[str] = Field(None, description="Primary email address of the contact. If you want to associate additional email(s) with this contact, use the other_emails attribute.")
    ticketId: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the contact")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    source: Optional[str] = Field(None, description="The channel through which the ticket was created")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    status: Optional[str] = Field(None, description="Status")
    priority: Optional[str] = Field(None, description="Priority")
    contactId: Optional[str] = Field(None, description="Contact ID")
    requesterIdentificationValue: Optional[str] = Field(None, description="Value of the identification selected")


class FreshdeskCreateTool(BaseTool):
    name = "freshdesk_create"
    description = "Tool for freshdesk create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the freshdesk create operation."""
        # Implement the tool logic here
        return f"Running freshdesk create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshdesk create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
