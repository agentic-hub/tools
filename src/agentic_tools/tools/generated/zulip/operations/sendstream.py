from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZulipCredentials(BaseModel):
    """Credentials for zulip authentication."""
    zulip_api: Optional[Dict[str, Any]] = Field(None, description="zulipApi")

class ZulipSendstreamToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ZulipCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="The content of the message")
    stream: Optional[str] = Field(None, description="The destination stream, or a comma-separated list containing the usernames (emails) of the recipients. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    user_id: Optional[str] = Field(None, description="The ID of user to get")
    additional_fields_json: Optional[str] = Field(None, description="JSON format parameters for stream creation")
    stream_id: Optional[str] = Field(None, description="ID of stream to update")
    operation: Optional[str] = Field(None, description="Operation")
    message_id: Optional[str] = Field(None, description="Unique identifier for the message")
    to: Optional[str] = Field(None, description="to")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    topic: Optional[str] = Field(None, description="The topic of the message. Only required if type is stream, ignored otherwise. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class ZulipSendstreamTool(BaseTool):
    name = "zulip_sendstream"
    description = "Tool for zulip sendStream operation - sendStream operation"
    
    def __init__(self, credentials: Optional[ZulipCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the zulip sendStream operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running zulip sendStream operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running zulip sendStream operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zulip sendStream operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
