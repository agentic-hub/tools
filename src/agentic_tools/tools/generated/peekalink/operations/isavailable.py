from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PeekalinkCredentials(BaseModel):
    """Credentials for peekalink authentication."""
    peekalink_api: Optional[Dict[str, Any]] = Field(None, description="peekalinkApi")

class PeekalinkIsavailableToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[PeekalinkCredentials] = Field(None, description="Custom credentials for authentication")
    operation: Optional[str] = Field(None, description="Operation")
    url: Optional[str] = Field(None, description="URL")


class PeekalinkIsavailableTool(BaseTool):
    name = "peekalink_isavailable"
    description = "Tool for peekalink isAvailable operation - isAvailable operation"
    
    def __init__(self, credentials: Optional[PeekalinkCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the peekalink isAvailable operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running peekalink isAvailable operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running peekalink isAvailable operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the peekalink isAvailable operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
