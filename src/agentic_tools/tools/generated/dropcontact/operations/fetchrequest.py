from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DropcontactCredentials(BaseModel):
    """Credentials for dropcontact authentication."""
    dropcontact_api: Optional[Dict[str, Any]] = Field(None, description="dropcontactApi")

class DropcontactFetchrequestToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DropcontactCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    request_id: Optional[str] = Field(None, description="Request ID")
    operation: Optional[str] = Field(None, description="Operation")


class DropcontactFetchrequestTool(BaseTool):
    name = "dropcontact_fetchrequest"
    description = "Tool for dropcontact fetchRequest operation - fetchRequest operation"
    
    def __init__(self, credentials: Optional[DropcontactCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the dropcontact fetchRequest operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running dropcontact fetchRequest operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running dropcontact fetchRequest operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the dropcontact fetchRequest operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
