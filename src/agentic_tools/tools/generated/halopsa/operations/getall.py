from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HalopsaCredentials(BaseModel):
    """Credentials for haloPSA authentication."""
    halo_psa_api: Optional[Dict[str, Any]] = Field(None, description="haloPSAApi")

class HalopsaGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HalopsaCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    site_id: Optional[str] = Field(None, description="Site ID")
    user_id: Optional[str] = Field(None, description="User ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    client_id: Optional[str] = Field(None, description="Client ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    simplify: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class HalopsaGetallTool(BaseTool):
    name = "halopsa_getall"
    description = "Tool for haloPSA getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[HalopsaCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the haloPSA getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running haloPSA getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running haloPSA getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the haloPSA getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
