from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class VonageCredentials(BaseModel):
    """Credentials for vonage authentication."""
    vonage_api: Optional[Dict[str, Any]] = Field(None, description="vonageApi")

class VonageSendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[VonageCredentials] = Field(None, description="Custom credentials for authentication")
    to: Optional[str] = Field(None, description="The number that the message should be sent to. Numbers are specified in E.164 format.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    message: Optional[str] = Field(None, description="The body of the message being sent")
    from: Optional[str] = Field(None, description="The name or number the message should be sent from")
    operation: Optional[str] = Field(None, description="Operation")


class VonageSendTool(BaseTool):
    name = "vonage_send"
    description = "Tool for vonage send operation - send operation"
    
    def __init__(self, credentials: Optional[VonageCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the vonage send operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running vonage send operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running vonage send operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the vonage send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
