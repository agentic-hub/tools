from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HalopsaCredentials(BaseModel):
    """Credentials for haloPSA authentication."""
    halo_psa_api: Optional[Dict[str, Any]] = Field(None, description="haloPSAApi")

class HalopsaCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HalopsaCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    site_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    summary: Optional[str] = Field(None, description="Summary")
    select_option: Optional[bool] = Field(None, description="Whether client can be selected by ID")
    ticket_type: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    details: Optional[str] = Field(None, description="Details")
    user_id: Optional[str] = Field(None, description="User ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    client_name: Optional[str] = Field(None, description="Enter client name")
    operation: Optional[str] = Field(None, description="Operation")
    client_id: Optional[str] = Field(None, description="Client ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    simplify: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    user_name: Optional[str] = Field(None, description="Enter user name")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    site_name: Optional[str] = Field(None, description="Enter site name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class HalopsaCreateTool(BaseTool):
    name = "halopsa_create"
    description = "Tool for haloPSA create operation - create operation"
    
    def __init__(self, credentials: Optional[HalopsaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the haloPSA create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running haloPSA create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running haloPSA create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the haloPSA create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
