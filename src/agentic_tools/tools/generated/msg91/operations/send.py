from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Msg91Credentials(BaseModel):
    """Credentials for msg91 authentication."""
    msg91_api: Optional[Dict[str, Any]] = Field(None, description="msg91Api")

class Msg91SendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[Msg91Credentials] = Field(None, description="Custom credentials for authentication")
    to: Optional[str] = Field(None, description="The number, with coutry code, to which to send the message")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="The message to send")
    from: Optional[str] = Field(None, description="The number from which to send the message")
    operation: Optional[str] = Field(None, description="Operation")


class Msg91SendTool(BaseTool):
    name = "msg91_send"
    description = "Tool for msg91 send operation - send operation"
    
    def __init__(self, credentials: Optional[Msg91Credentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the msg91 send operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running msg91 send operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running msg91 send operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the msg91 send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
