from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Signl4Credentials(BaseModel):
    """Credentials for signl4 authentication."""
    signl4_api: Optional[Dict[str, Any]] = Field(None, description="signl4Api")

class Signl4SendToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[Signl4Credentials] = Field(None, description="Custom credentials for authentication")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    message: Optional[str] = Field(None, description="A more detailed description for the alert")
    operation: Optional[str] = Field(None, description="Operation")


class Signl4SendTool(BaseTool):
    name = "signl4_send"
    description = "Tool for signl4 send operation - send operation"
    
    def __init__(self, credentials: Optional[Signl4Credentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the signl4 send operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running signl4 send operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running signl4 send operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the signl4 send operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
