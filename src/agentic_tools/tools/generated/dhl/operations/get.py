from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DhlCredentials(BaseModel):
    """Credentials for dhl authentication."""
    dhl_api: Optional[Dict[str, Any]] = Field(None, description="dhlApi")

class DhlGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DhlCredentials] = Field(None, description="Custom credentials for authentication")
    tracking_number: Optional[str] = Field(None, description="Tracking Number")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class DhlGetTool(BaseTool):
    name = "dhl_get"
    description = "Tool for dhl get operation - get operation"
    
    def __init__(self, credentials: Optional[DhlCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the dhl get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running dhl get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running dhl get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the dhl get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
