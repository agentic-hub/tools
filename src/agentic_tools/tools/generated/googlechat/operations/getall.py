from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglechatCredentials(BaseModel):
    """Credentials for googleChat authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")

class GooglechatGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[GooglechatCredentials] = Field(None, description="Custom credentials for authentication")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    json_parameters: Optional[bool] = Field(None, description="Whether to pass the message object as JSON")
    space_id: Optional[str] = Field(None, description="The name of the space for which to retrieve members, in the form \"spaces/*\". Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    message_id: Optional[str] = Field(None, description="Resource name of the message to be deleted, in the form \"spaces//messages/\"")
    operation: Optional[str] = Field(None, description="Operation")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://developers.google.com/chat/reference/rest/v1/spaces.messages#Message\" target=\"_blank\">Google Chat Guide</a> To Creating Messages")


class GooglechatGetallTool(BaseTool):
    name = "googlechat_getall"
    description = "Tool for googleChat getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[GooglechatCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the googleChat getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running googleChat getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running googleChat getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleChat getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
