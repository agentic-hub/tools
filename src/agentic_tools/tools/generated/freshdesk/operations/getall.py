from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FreshdeskCredentials(BaseModel):
    """Credentials for freshdesk authentication."""
    freshdesk_api: Optional[Dict[str, Any]] = Field(None, description="freshdeskApi")

class FreshdeskGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[FreshdeskCredentials] = Field(None, description="Custom credentials for authentication")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")


class FreshdeskGetallTool(BaseTool):
    name = "freshdesk_getall"
    description = "Tool for freshdesk getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[FreshdeskCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the freshdesk getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running freshdesk getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running freshdesk getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the freshdesk getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
