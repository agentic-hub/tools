from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BaserowCredentials(BaseModel):
    """Credentials for baserow authentication."""
    baserow_api: Optional[Dict[str, Any]] = Field(None, description="baserowApi")

class BaserowGetToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[BaserowCredentials] = Field(None, description="Custom credentials for authentication")
    resource: Optional[str] = Field(None, description="Resource")
    table_id: Optional[str] = Field(None, description="Table to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    database_id: Optional[str] = Field(None, description="Database to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    row_id: Optional[str] = Field(None, description="ID of the row to return")
    operation: Optional[str] = Field(None, description="Operation")


class BaserowGetTool(BaseTool):
    name = "baserow_get"
    description = "Tool for baserow get operation - get operation"
    
    def __init__(self, credentials: Optional[BaserowCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the baserow get operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running baserow get operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running baserow get operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the baserow get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
