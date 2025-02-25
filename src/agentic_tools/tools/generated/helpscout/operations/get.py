from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HelpscoutCredentials(BaseModel):
    """Credentials for helpScout authentication."""
    help_scout_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="helpScoutOAuth2Api")

class HelpscoutGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[HelpscoutCredentials] = Field(None, description="Custom credentials for authentication")
    mailbox_id: Optional[str] = Field(None, description="Mailbox ID")
    customer_id: Optional[str] = Field(None, description="Customer ID")
    type: Optional[str] = Field(None, description="Conversation type")
    resolve_data: Optional[bool] = Field(None, description="By default the response only contain the ID to resource. If this option gets activated, it will resolve the data automatically.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    conversation_id: Optional[str] = Field(None, description="Conversation ID")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class HelpscoutGetTool(BaseTool):
    name = "helpscout_get"
    description = "Tool for helpScout get operation - get operation"
    
    def __init__(self, credentials: Optional[HelpscoutCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the helpScout get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running helpScout get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running helpScout get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the helpScout get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
