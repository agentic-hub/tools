from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwssnsCredentials(BaseModel):
    """Credentials for awsSns authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwssnsDeleteToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[AwssnsCredentials] = Field(None, description="Custom credentials for authentication")
    topic: Optional[str] = Field(None, description="By URL")
    operation: Optional[str] = Field(None, description="Operation")


class AwssnsDeleteTool(BaseTool):
    name = "awssns_delete"
    description = "Tool for awsSns delete operation - delete operation"
    
    def __init__(self, credentials: Optional[AwssnsCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the awsSns delete operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running awsSns delete operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running awsSns delete operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsSns delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
