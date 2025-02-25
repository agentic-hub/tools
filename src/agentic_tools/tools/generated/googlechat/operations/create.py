from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglechatCredentials(BaseModel):
    """Credentials for googleChat authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")

class GooglechatCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglechatCredentials] = Field(None, description="Custom credentials for authentication")
    message_ui: Optional[Dict[str, Any]] = Field(None, description="Message")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    json_parameters: Optional[bool] = Field(None, description="Whether to pass the message object as JSON")
    space_id: Optional[str] = Field(None, description="Space resource name, in the form \"spaces/*\". Example: spaces/AAAAMpdlehY. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    message_id: Optional[str] = Field(None, description="Resource name of the message to be deleted, in the form \"spaces//messages/\"")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message\" target=\"_blank\">Google Chat Guide</a> To Creating Messages")
    message_json: Optional[str] = Field(None, description="Message input as JSON Object or JSON String")


class GooglechatCreateTool(BaseTool):
    name = "googlechat_create"
    description = "Tool for googleChat create operation - create operation"
    
    def __init__(self, credentials: Optional[GooglechatCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleChat create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleChat create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleChat create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleChat create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
