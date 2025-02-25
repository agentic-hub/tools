from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SyncromspCredentials(BaseModel):
    """Credentials for syncroMsp authentication."""
    syncro_msp_api: Optional[Dict[str, Any]] = Field(None, description="syncroMspApi")

class SyncromspGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SyncromspCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    customer_id: Optional[str] = Field(None, description="Get specific customer by ID")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    alert_id: Optional[str] = Field(None, description="Get specific RMM alert by ID")
    email: Optional[str] = Field(None, description="Email")
    contact_id: Optional[str] = Field(None, description="Get specific contact by ID")
    ticket_id: Optional[str] = Field(None, description="Get specific customer by ID")
    operation: Optional[str] = Field(None, description="Operation")


class SyncromspGetTool(BaseTool):
    name = "syncromsp_get"
    description = "Tool for syncroMsp get operation - get operation"
    
    def __init__(self, credentials: Optional[SyncromspCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the syncroMsp get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running syncroMsp get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running syncroMsp get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the syncroMsp get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
