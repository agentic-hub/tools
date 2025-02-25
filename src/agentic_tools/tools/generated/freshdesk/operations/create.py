from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshdeskCredentials(BaseModel):
    """Credentials for freshdesk authentication."""
    freshdesk_api: Optional[Dict[str, Any]] = Field(None, description="freshdeskApi")

class FreshdeskCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FreshdeskCredentials] = Field(None, description="Custom credentials for authentication")
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
    name = "freshdesk_create"
    description = "Tool for freshdesk create operation - create operation"
    
    def __init__(self, credentials: Optional[FreshdeskCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the freshdesk create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running freshdesk create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running freshdesk create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshdesk create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
