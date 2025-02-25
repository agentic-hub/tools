from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwakeCredentials(BaseModel):
    """Credentials for twake authentication."""
    twake_cloud_api: Optional[Dict[str, Any]] = Field(None, description="twakeCloudApi")

class TwakeSendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TwakeCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="Message content")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    channel_id: Optional[str] = Field(None, description="Channel's ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class TwakeSendTool(BaseTool):
    name = "twake_send"
    description = "Tool for twake send operation - send operation"
    
    def __init__(self, credentials: Optional[TwakeCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the twake send operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running twake send operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running twake send operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twake send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
