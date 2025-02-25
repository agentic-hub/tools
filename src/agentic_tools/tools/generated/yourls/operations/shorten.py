from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class YourlsCredentials(BaseModel):
    """Credentials for yourls authentication."""
    yourls_api: Optional[Dict[str, Any]] = Field(None, description="yourlsApi")

class YourlsShortenToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[YourlsCredentials] = Field(None, description="Custom credentials for authentication")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    url: Optional[str] = Field(None, description="The URL to shorten")
    short_url: Optional[str] = Field(None, description="The short URL to expand")
    operation: Optional[str] = Field(None, description="Operation")


class YourlsShortenTool(BaseTool):
    name = "yourls_shorten"
    description = "Tool for yourls shorten operation - shorten operation"
    
    def __init__(self, credentials: Optional[YourlsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the yourls shorten operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running yourls shorten operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running yourls shorten operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the yourls shorten operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
