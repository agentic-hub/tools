from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CiscowebexCredentials(BaseModel):
    """Credentials for ciscoWebex authentication."""
    cisco_webex_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="ciscoWebexOAuth2Api")

class CiscowebexGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[CiscowebexCredentials] = Field(None, description="Custom credentials for authentication")
    room_id: Optional[str] = Field(None, description="List messages in a room, by ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    text: Optional[str] = Field(None, description="The message, in plain text")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    message_id: Optional[str] = Field(None, description="ID of the message to delete")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    meeting_id: Optional[str] = Field(None, description="ID of the meeting")


class CiscowebexGetallTool(BaseTool):
    name = "ciscowebex_getall"
    description = "Tool for ciscoWebex getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[CiscowebexCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the ciscoWebex getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running ciscoWebex getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running ciscoWebex getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ciscoWebex getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
