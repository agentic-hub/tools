from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IterableCredentials(BaseModel):
    """Credentials for iterable authentication."""
    iterable_api: Optional[Dict[str, Any]] = Field(None, description="iterableApi")

class IterableAddToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[IterableCredentials] = Field(None, description="Custom credentials for authentication")
    user_id: Optional[str] = Field(None, description="Unique identifier for a particular user")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    value: Optional[str] = Field(None, description="Value")
    by: Optional[str] = Field(None, description="Identifier to be used")
    list_id: Optional[str] = Field(None, description="Identifier to be used. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    identifier: Optional[str] = Field(None, description="Identifier to be used")
    email: Optional[str] = Field(None, description="Email for a particular user")
    operation: Optional[str] = Field(None, description="Operation")


class IterableAddTool(BaseTool):
    name = "iterable_add"
    description = "Tool for iterable add operation - add operation"
    
    def __init__(self, credentials: Optional[IterableCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the iterable add operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running iterable add operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running iterable add operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the iterable add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
