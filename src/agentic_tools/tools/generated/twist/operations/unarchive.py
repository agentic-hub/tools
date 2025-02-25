from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TwistCredentials(BaseModel):
    """Credentials for twist authentication."""
    twist_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="twistOAuth2Api")

class TwistUnarchiveToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[TwistCredentials] = Field(None, description="Custom credentials for authentication")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="The content of the comment")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    conversation_id: Optional[str] = Field(None, description="The ID of the conversation. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    id: Optional[str] = Field(None, description="The ID of the conversation message")
    workspace_id: Optional[str] = Field(None, description="The ID of the workspace. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    thread_id: Optional[str] = Field(None, description="The ID of the thread")
    comment_id: Optional[str] = Field(None, description="The ID of the comment")
    channel_id: Optional[str] = Field(None, description="The ID of the channel")
    operation: Optional[str] = Field(None, description="Operation")


class TwistUnarchiveTool(BaseTool):
    name = "twist_unarchive"
    description = "Tool for twist unarchive operation - unarchive operation"
    
    def __init__(self, credentials: Optional[TwistCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the twist unarchive operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running twist unarchive operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running twist unarchive operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the twist unarchive operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
