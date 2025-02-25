from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MessagebirdCredentials(BaseModel):
    """Credentials for messageBird authentication."""
    message_bird_api: Optional[Dict[str, Any]] = Field(None, description="messageBirdApi")

class MessagebirdGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MessagebirdCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class MessagebirdGetTool(BaseTool):
    name = "messagebird_get"
    description = "Tool for messageBird get operation - get operation"
    
    def __init__(self, credentials: Optional[MessagebirdCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the messageBird get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running messageBird get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running messageBird get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the messageBird get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
