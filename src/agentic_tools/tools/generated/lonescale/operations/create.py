from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LonescaleCredentials(BaseModel):
    """Credentials for loneScale authentication."""
    lone_scale_api: Optional[Dict[str, Any]] = Field(None, description="loneScaleApi")

class LonescaleCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[LonescaleCredentials] = Field(None, description="Custom credentials for authentication")
    list: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    name: Optional[str] = Field(None, description="Name of your list")
    resource: Optional[str] = Field(None, description="Create a new list")
    operation: Optional[str] = Field(None, description="Operation")
    type: Optional[str] = Field(None, description="Type of your list")


class LonescaleCreateTool(BaseTool):
    name = "lonescale_create"
    description = "Tool for loneScale create operation - create operation"
    
    def __init__(self, credentials: Optional[LonescaleCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the loneScale create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running loneScale create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running loneScale create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the loneScale create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
