from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BitlyCredentials(BaseModel):
    """Credentials for bitly authentication."""
    bitly_api: Optional[Dict[str, Any]] = Field(None, description="bitlyApi")
    bitly_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="bitlyOAuth2Api")

class BitlyCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[BitlyCredentials] = Field(None, description="Custom credentials for authentication")
    long_url: Optional[str] = Field(None, description="Long URL")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    deeplink: Optional[Dict[str, Any]] = Field(None, description="Deeplinks")
    id: Optional[str] = Field(None, description="Bitlink")
    operation: Optional[str] = Field(None, description="Operation")


class BitlyCreateTool(BaseTool):
    name = "bitly_create"
    description = "Tool for bitly create operation - create operation"
    
    def __init__(self, credentials: Optional[BitlyCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the bitly create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running bitly create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running bitly create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bitly create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
