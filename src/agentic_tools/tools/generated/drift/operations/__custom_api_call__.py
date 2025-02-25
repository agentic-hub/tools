from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DriftCredentials(BaseModel):
    """Credentials for drift authentication."""
    drift_api: Optional[Dict[str, Any]] = Field(None, description="driftApi")
    drift_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="driftOAuth2Api")

class Drift__custom_api_call__ToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DriftCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for the contact")
    operation: Optional[str] = Field(None, description="Operation")


class Drift__custom_api_call__Tool(BaseTool):
    name = "drift___custom_api_call__"
    description = "Tool for drift __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def __init__(self, credentials: Optional[DriftCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the drift __CUSTOM_API_CALL__ operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running drift __CUSTOM_API_CALL__ operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running drift __CUSTOM_API_CALL__ operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the drift __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
