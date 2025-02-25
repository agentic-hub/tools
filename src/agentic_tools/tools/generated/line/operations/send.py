from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LineCredentials(BaseModel):
    """Credentials for line authentication."""
    line_notify_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="lineNotifyOAuth2Api")

class LineSendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[LineCredentials] = Field(None, description="Custom credentials for authentication")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="Message")
    operation: Optional[str] = Field(None, description="Operation")


class LineSendTool(BaseTool):
    name = "line_send"
    description = "Tool for line send operation - send operation"
    
    def __init__(self, credentials: Optional[LineCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the line send operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running line send operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running line send operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the line send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
