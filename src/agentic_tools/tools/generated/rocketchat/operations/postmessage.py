from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RocketchatCredentials(BaseModel):
    """Credentials for rocketchat authentication."""
    rocketchat_api: Optional[Dict[str, Any]] = Field(None, description="rocketchatApi")

class RocketchatPostmessageToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[RocketchatCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    attachments_json: Optional[str] = Field(None, description="Attachments")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    channel: Optional[str] = Field(None, description="The channel name with the prefix in front of it")
    operation: Optional[str] = Field(None, description="Operation")
    text: Optional[str] = Field(None, description="The text of the message to send, is optional because of attachments")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    attachments: Optional[List[Any]] = Field(None, description="Attachments")


class RocketchatPostmessageTool(BaseTool):
    name = "rocketchat_postmessage"
    description = "Tool for rocketchat postMessage operation - postMessage operation"
    
    def __init__(self, credentials: Optional[RocketchatCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the rocketchat postMessage operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running rocketchat postMessage operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running rocketchat postMessage operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the rocketchat postMessage operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
