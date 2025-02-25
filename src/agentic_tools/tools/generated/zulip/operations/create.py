from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ZulipCredentials(BaseModel):
    """Credentials for zulip authentication."""
    zulip_api: Optional[Dict[str, Any]] = Field(None, description="zulipApi")

class ZulipCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[ZulipCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="The content of the message")
    full_name: Optional[str] = Field(None, description="The full name of the new user")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    short_name: Optional[str] = Field(None, description="The short name of the new user. Not user-visible.")
    user_id: Optional[str] = Field(None, description="The ID of user to get")
    email: Optional[str] = Field(None, description="The email address of the new user")
    additional_fields_json: Optional[str] = Field(None, description="JSON format parameters for stream creation")
    password: Optional[str] = Field(None, description="The password of the new user")
    stream_id: Optional[str] = Field(None, description="ID of stream to update")
    operation: Optional[str] = Field(None, description="Operation")
    message_id: Optional[str] = Field(None, description="Unique identifier for the message")
    to: Optional[str] = Field(None, description="to")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    subscriptions: Optional[Dict[str, Any]] = Field(None, description="A list of dictionaries containing the the key name and value specifying the name of the stream to subscribe. If the stream does not exist a new stream is created.")


class ZulipCreateTool(BaseTool):
    name = "zulip_create"
    description = "Tool for zulip create operation - create operation"
    
    def __init__(self, credentials: Optional[ZulipCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the zulip create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running zulip create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running zulip create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the zulip create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
