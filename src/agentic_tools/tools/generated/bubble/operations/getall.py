from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BubbleCredentials(BaseModel):
    """Credentials for bubble authentication."""
    bubble_api: Optional[Dict[str, Any]] = Field(None, description="bubbleApi")

class BubbleGetallToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[BubbleCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    object_id: Optional[str] = Field(None, description="ID of the object to retrieve")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    type_name: Optional[str] = Field(None, description="Name of data type of the object to create")
    operation: Optional[str] = Field(None, description="Operation")


class BubbleGetallTool(BaseTool):
    name = "bubble_getall"
    description = "Tool for bubble getAll operation - getAll operation"
    
    def __init__(self, credentials: Optional[BubbleCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the bubble getAll operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running bubble getAll operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running bubble getAll operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bubble getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
