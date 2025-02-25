from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GetresponseCredentials(BaseModel):
    """Credentials for getResponse authentication."""
    get_response_api: Optional[Dict[str, Any]] = Field(None, description="getResponseApi")
    get_response_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="getResponseOAuth2Api")

class GetresponseUpdateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GetresponseCredentials] = Field(None, description="Custom credentials for authentication")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for a particular contact")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GetresponseUpdateTool(BaseTool):
    name = "getresponse_update"
    description = "Tool for getResponse update operation - update operation"
    
    def __init__(self, credentials: Optional[GetresponseCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the getResponse update operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running getResponse update operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running getResponse update operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the getResponse update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
