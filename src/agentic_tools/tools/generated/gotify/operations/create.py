from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GotifyCredentials(BaseModel):
    """Credentials for gotify authentication."""
    gotify_api: Optional[Dict[str, Any]] = Field(None, description="gotifyApi")

class GotifyCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GotifyCredentials] = Field(None, description="Custom credentials for authentication")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The message to send, If using Markdown add the Content Type option")
    operation: Optional[str] = Field(None, description="Operation")


class GotifyCreateTool(BaseTool):
    name = "gotify_create"
    description = "Tool for gotify create operation - create operation"
    
    def __init__(self, credentials: Optional[GotifyCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the gotify create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running gotify create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running gotify create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gotify create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
