from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StackbyCredentials(BaseModel):
    """Credentials for stackby authentication."""
    stackby_api: Optional[Dict[str, Any]] = Field(None, description="stackbyApi")

class StackbyReadToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[StackbyCredentials] = Field(None, description="Custom credentials for authentication")
    table: Optional[str] = Field(None, description="Enter Table Name")
    id: Optional[str] = Field(None, description="ID of the record to return")
    operation: Optional[str] = Field(None, description="Operation")
    stack_id: Optional[str] = Field(None, description="The ID of the stack to access")


class StackbyReadTool(BaseTool):
    name = "stackby_read"
    description = "Tool for stackby read operation - read operation"
    
    def __init__(self, credentials: Optional[StackbyCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the stackby read operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running stackby read operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running stackby read operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the stackby read operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
