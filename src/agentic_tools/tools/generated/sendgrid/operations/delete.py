from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SendgridCredentials(BaseModel):
    """Credentials for sendGrid authentication."""
    send_grid_api: Optional[Dict[str, Any]] = Field(None, description="sendGridApi")

class SendgridDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SendgridCredentials] = Field(None, description="Custom credentials for authentication")
    ids: Optional[str] = Field(None, description="ID of the contact. Multiple can be added separated by comma.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    delete_contacts: Optional[bool] = Field(None, description="Whether to delete all contacts on the list")
    email: Optional[str] = Field(None, description="Primary email for the contact")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="ID of the list")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    delete_all: Optional[bool] = Field(None, description="Whether all contacts will be deleted")


class SendgridDeleteTool(BaseTool):
    name = "sendgrid_delete"
    description = "Tool for sendGrid delete operation - delete operation"
    
    def __init__(self, credentials: Optional[SendgridCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the sendGrid delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running sendGrid delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running sendGrid delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the sendGrid delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
